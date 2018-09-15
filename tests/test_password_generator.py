from unittest.mock import ANY

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from password_generator.views import sanitise


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
                    {'count': 1, 'id': ANY, 'word': sanitise(word), 'wordset': 'english'}
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
            {'id': ANY, 'wordset': 'english', 'word': 'the', 'count': 3}
        )

        response = self.client.get('/words/?word=brown')
        self.assertEqual(
            response.json()['results'][0],
            {'id': ANY, 'wordset': 'english', 'word': 'brown', 'count': 1}
        )

        response = self.client.get('/words/?word=fantastic')
        self.assertFalse(response.json()['results'])
