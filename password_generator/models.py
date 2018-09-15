from django.db import models

ABSOLUTE_MAX_WORD_LENGTH = 15  # Never bother keeping really long words


class Wordset(models.Model):
    name = models.CharField(max_length=30, unique=True)  # probably a language so we can generate passwords in different ones


class Word(models.Model):
    word = models.CharField(max_length=ABSOLUTE_MAX_WORD_LENGTH)
    count = models.IntegerField(default=0)
    wordset = models.ForeignKey(Wordset, on_delete=models.CASCADE, related_name='words')
