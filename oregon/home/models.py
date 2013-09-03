from django.db import models

class Word(models.Model):
    english = models.CharField(max_length=15, blank=False, unique=True)

class Morpheme(models.Model):
    """
    Parameters and fit results associated with a variable in the database.

    Not sure if a database is really needed for this, but is a nice-to-have
    """
    word = models.OneToOneField(Word, blank=False, null=False, unique=True)
    bound = models.NullBooleanField(default=True, help_text="Whether the word is *not* \"free-standing\" as it's own word.")

