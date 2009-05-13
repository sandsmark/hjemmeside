from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    version = models.DecimalField(max_digits=3,decimal_places=2)
    screenshot = models.ImageField(upload_to="screenshots")
    sourcecode = models.FileField(upload_to="source")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/apps/app/%i/" % self.id
