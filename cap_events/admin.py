from django.contrib import admin

import models

class ImageInline(admin.TabularInline):
    model = models.Image

class EventAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]
    list_display = ['user', 'name', 'description', 'date', 'time', 'show_sites', 'publish']

    prepopulated_fields = {'slug' : ('name',)}


admin.site.register(models.Event, EventAdmin)
