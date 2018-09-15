from rest_framework import serializers

from .models import Word
from .models import Wordset


class WordSerializer(serializers.ModelSerializer):
    wordset = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Word
        fields = '__all__'


class WordsetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wordset
        fields = '__all__'
