from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    img = models.URLField(max_length=250, null=True, blank=True)
    date = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title