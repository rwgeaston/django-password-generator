=====================
Passphrase generator
=====================

Upload some text which will be used to determine word frequencies in your preferred language. Then random passphrases of an appropriate length can be generated.

Setup
-----------

1. Add "password_generator" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'password_generator',
    ]

you also need rest_framework and django_filters in your INSTALLED_APPS

2. Include the password-generator URLconf in your project urls.py like this::

    path('', include('password_generator.urls')),

3. Run `python manage.py migrate` to create the password generator models.

4. Start/Restart the server and POST texts to /words/bulk_add_words/ endpoint. The posted text will be split on spaces and used to determine word frequency. Words which are too short or too long will be ignored.

Payload should be:

{"wordset": "English", "text": "The quick brown fox jumps over the lazy cow"}

If you want a good sample of English language words, there is a useful link "big.txt" here https://norvig.com/spell-correct.html. It might break if you upload all of that at once (not tested). Alternatively provide your own word source. "wordset" doesn't have to exist in advance.

5. GET /wordset/WORDSET/generate_password/ endpoint to get some random words. WORDSET should be a wordset

allowed query params:

- length to choose the number of words in your passphrase.
- words_allowed to say how infrequent words are allowed. By default, 2000 most common words are allowed. words_allowed=10000 will choose from much bigger dictionary.
- min_word_length lets you control the length of words used. default minimum word length is 4.
- max_word_length is similar (default 10)
