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


def sanitise(word):
    return word.lower()


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
                return JsonResponse({f'Must provide {param}'}, status=status.HTTP_400_BAD_REQUEST)

        wordset_name = request.data['wordset']
        text = request.data['text']

        wordset = Wordset.objects.get_or_create(name=wordset_name)[0]

        new_words = text.split()
        new_word_counts = Counter()

        for word in new_words:
            word = sanitise(word)
            if len(word) <= ABSOLUTE_MAX_WORD_LENGTH:
                new_word_counts[word] += 1

        for word, count in new_word_counts.items():
            word_object = Word.objects.get_or_create(word=word, wordset=wordset)[0]
            word_object.count += count
            word_object.save()

        return JsonResponse({'added': new_word_counts}, status=status.HTTP_201_CREATED)
