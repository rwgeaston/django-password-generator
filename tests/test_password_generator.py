import random
from unittest.mock import ANY

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from password_generator.input_sanitise import sanitise

from .test_password_generator_data import big_input
from .test_password_generator_data import big_output


class PasswordGeneratorTest(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.client = APIClient()

    def test_post_words(self):
        first_phrase = 'The quick brown fox jumps over lazy dog'
        response = self.client.post(
            '/words/bulk_add_words/',
            data={
                'wordset': 'english',
                'text': first_phrase
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                'added': {sanitise(word): 1 for word in first_phrase.split()}
            }
        )

        response = self.client.get('/words/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'count': first_phrase.count(' ') + 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'count': 1, 'id': ANY, 'word': sanitise(word),
                        'wordset': 'english', 'word_length': len(sanitise(word))
                    }
                    for word in first_phrase.split()
                ],
            },
        )

        second_phrase = 'the slow red dog jumps over the energetic cow'
        response = self.client.post(
            '/words/bulk_add_words/',
            data={
                'wordset': 'english',
                'text': second_phrase
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                'added': {sanitise(word): second_phrase.count(word) for word in second_phrase.split()}
            }
        )

        # Change these if you change the phrases above
        response = self.client.get('/words/?word=the')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['results'][0],
            {'id': ANY, 'wordset': 'english', 'word': 'the', 'count': 3, 'word_length': 3}
        )

        response = self.client.get('/words/?word=brown')
        self.assertEqual(
            response.json()['results'][0],
            {'id': ANY, 'wordset': 'english', 'word': 'brown', 'count': 1, 'word_length': 5}
        )

        response = self.client.get('/words/?word=fantastic')
        self.assertFalse(response.json()['results'])

    def test_generate_password(self):
        words = 'word word another word this word can be used in a password exceptionally long word as well'
        response = self.client.post(
            '/words/bulk_add_words/',
            data={
                'wordset': 'english',
                'text': words
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        random.seed(1)

        response = self.client.get('/languages/english/generate_password/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'passphrase': 'another password well well', 'permutations_chosen_from': 2401},
        )

        # Only allow short words
        response = self.client.get(
            '/languages/english/generate_password/?min_word_length=2&max_word_length=4&length=3'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'passphrase': 'this used this', 'permutations_chosen_from': 729},
        )

        # Only allow long words
        response = self.client.get(
            '/languages/english/generate_password/?min_word_length=8&max_word_length=15&length=2'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'passphrase': 'exceptionally exceptionally', 'permutations_chosen_from': 4},
        )

        # Only allow very common words
        response = self.client.get(
            '/languages/english/generate_password/?words_allowed=2'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'passphrase': 'another another word word', 'permutations_chosen_from': 16},
        )

    def test_big_dirty_input(self):
        response = self.client.post(
            '/words/bulk_add_words/',
            data={
                'wordset': 'english',
                'text': big_input
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'added': big_output})
