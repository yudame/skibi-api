from django.db import models
from django.urls import reverse

from apps.common.behaviors import Timestampable


class Link(Timestampable, models.Model):

    blog = models.ForeignKey("blog.Blog", related_name="links", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    href = models.URLField()

    # MODEL PROPERTIES

    # MODEL FUNCTIONS

    def __str__(self):
        return f"{self.title} - {self.blog.title}"
