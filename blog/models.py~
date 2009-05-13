from django.db import models

class Entry(models.Model):
    entry = models.TextField()
    pubdate = models.DateTimeField('date')
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/entry/%i/" % self.id

