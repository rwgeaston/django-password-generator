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

2. Include the password-generator URLconf in your project urls.py like this::

    path('', include('password_generator.urls')),

3. Run `python manage.py migrate` to create the password generator models.

4. Start/Restart the server and POST texts to /words/bulk_add_words/ endpoint. The posted text will be split on spaces and used to determine word frequency. Words which are too short or too long will be ignored.

Payload should be:

```json

{
    "wordset": "English",

    "text": "The quick brown fox jumps over the lazy cow"
}
```

Only words between lengths 4 and 10 will be kept (or configure in settings with MAX_WORD_LENGTH AND MIN_WORD_LENGTH).

5. GET /passphrase/ endpoint to get some random words. If you have more than one wordset, specify with ?wordset=

Can also use ?length= to choose the number of words in your passphrase.
