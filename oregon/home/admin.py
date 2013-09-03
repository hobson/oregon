from django.contrib import admin
from oregon.home.models import *

class WordAdmin(admin.ModelAdmin):
    pass

class MorphemeAdmin(admin.MorephemeAdmin):
    pass

admin.site.register(Word, WordAdmin)
admin.site.register(Morpheme, MorphemeAdmin)