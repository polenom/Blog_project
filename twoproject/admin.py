from django.contrib import admin
from .models import *
# Register your models here.

class TPadmin(admin.ModelAdmin):
    list_display = ('title','text','created','link')
    list_display_links =  ('title','text')
    search_fields = ('title','text')

admin.site.register(Post, TPadmin)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(Newper)