from django.contrib import admin
from .models import Anime, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

class AnimeAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Episode)