from rest_framework import serializers

from .models import Word


class WordSerializer(serializers.ModelSerializer):
    wordset = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Word
        fields = '__all__'
