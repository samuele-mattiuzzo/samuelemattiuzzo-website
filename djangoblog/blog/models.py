from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('post_view', kwargs={
            "year": self.created_at.year,
            "month": self.created_at.month,
            "day": self.created_at.day,
            "slug": self.slug
        })

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]