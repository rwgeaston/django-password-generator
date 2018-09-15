from random import randint
from collections import Counter

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Word
from .models import Wordset
from .models import ABSOLUTE_MAX_WORD_LENGTH
from .serializers import WordSerializer
from .serializers import WordsetSerializer
from .input_sanitise import sanitise


class WordViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = (
        DjangoFilterBackend,
    )
    filter_fields = (
        'word',
    )

    @staticmethod
    @action(methods=['post'], detail=False)
    def bulk_add_words(request):
        for param in ('wordset', 'text'):
            if param not in request.data:
                return JsonResponse({'error': f'Must provide {param}'}, status=status.HTTP_400_BAD_REQUEST)

        wordset_name = request.data['wordset']
        text = request.data['text']

        wordset = Wordset.objects.get_or_create(name=wordset_name)[0]

        new_words = text.split()
        new_word_counts = Counter()

        for word in new_words:
            word = sanitise(word)
            if word and len(word) <= ABSOLUTE_MAX_WORD_LENGTH:
                new_word_counts[word] += 1

        for word, count in new_word_counts.items():
            word_object = Word.objects.get_or_create(word=word, wordset=wordset, word_length=len(word))[0]
            word_object.count += count
            word_object.save()

        return JsonResponse({'added': new_word_counts}, status=status.HTTP_201_CREATED)


class WordsetViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors

    queryset = Wordset.objects.all()
    serializer_class = WordsetSerializer
    lookup_field = 'name'

    @staticmethod
    @action(methods=['get'], detail=True)
    def generate_password(request, name=None):
        min_word_length = int(request.query_params.get('min_word_length', 4))
        max_word_length = int(request.query_params.get('max_word_length', 10))
        phrase_length = int(request.query_params.get('length', 4))
        words_allowed = int(request.query_params.get('words_allowed', 2000))

        words_available = (
            Word.objects.all()
            .filter(wordset__name=name)
            .filter(word_length__gte=min_word_length)
            .filter(word_length__lte=max_word_length)
            .order_by('-count')
        )

        options_count = min(words_available.count(), words_allowed)
        if not options_count:
            return JsonResponse({'error': 'No words configured for this language'}, status=status.HTTP_400_BAD_REQUEST)

        words_used = []
        for _ in range(phrase_length):
            word_index_chosen = randint(0, options_count - 1)
            new_word = words_available[word_index_chosen]
            words_used.append(new_word.word)

        return JsonResponse({
            'passphrase': ' '.join(words_used),
            'permutations_chosen_from': options_count ** phrase_length,
        })
