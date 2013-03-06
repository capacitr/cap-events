from django.contrib import admin

import models

class ImageInline(admin.TabularInline):
    model = models.Image

class EventAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]
    list_display = ['name', 'description', 'date', 'time', 'publish']

    prepopulated_fields = {'slug' : ('name',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'slug']

admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Tag, TagAdmin)
