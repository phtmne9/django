from django.contrib import admin

from bboard.models import Rubric, Bb



class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Rubric)
admin.site.register(Bb, BbAdmin)
