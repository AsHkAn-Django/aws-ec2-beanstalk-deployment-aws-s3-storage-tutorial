from django.db import models


class Photo(models.Model):
    """A model for uploading photos with caption."""
    picture = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=260, blank=True, null=True)

    def __str__(self):
        return self.caption

