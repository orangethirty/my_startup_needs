from django.db import models
from django.utils.text import slugify


class Need(models.Model):
    need = models.CharField(max_length=255)
    slug = models.SlugField(unique=True) #default max_length is 50 chars.
    date_created = models.DateTimeField(auto_now_add = True)
    
    def save(self, *args, **keyargs):
        self.slug = slugify(self.need)
        super(Need, self).save(*args, **keyargs)
        
    def __unicode__(self):
        return self.need