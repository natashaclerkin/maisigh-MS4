from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField(max_length=800)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
