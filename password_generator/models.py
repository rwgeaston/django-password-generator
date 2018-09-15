from django.db import models

ABSOLUTE_MAX_WORD_LENGTH = 15  # Never bother keeping really long words


class Wordset(models.Model):
    # probably a language so we can generate passwords in different ones
    name = models.CharField(max_length=30, unique=True)


class Word(models.Model):
    word = models.CharField(max_length=ABSOLUTE_MAX_WORD_LENGTH)
    word_length = models.IntegerField(db_index=True)
    count = models.IntegerField(default=0, db_index=True)
    wordset = models.ForeignKey(Wordset, on_delete=models.CASCADE, related_name='words')
