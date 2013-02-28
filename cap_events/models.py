from django.db import models

from thumbnail_works.fields import EnhancedImageField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^thumbnail_works\.fields\.EnhancedImageField"])

class Tag(models.Model):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return self.tag

class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()

    name = models.CharField(max_length=255, default="")
    slug = models.SlugField(max_length=255, unique=True)

    description = models.TextField(help_text="Where is this event?  And what is it about?")
    publish = models.BooleanField(default=True)

    tags = models.ManyToManyField('cap_events.Tag')

    class Meta:
        ordering = ['-date', '-time']

    @models.permalink
    def get_absolute_url(self):
        return ('get_event', (), {'slug' : self.slug} )


class Image(models.Model):
    event = models.ForeignKey(Event)
    image = EnhancedImageField(
        upload_to = 'uploads',
        process_source = dict(
            size='600x400', sharpen=True, upscale=True, format='JPEG'),
        thumbnails = {
            'avatar': dict(size='280x108'),
        },
        blank=True
    )


