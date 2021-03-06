from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from heatindex.fields import HeatIndexField


# def score(obj, add):
#     return obj.upvotes - obj.downvotes


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=100)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    posted = models.DateTimeField()
    heat = HeatIndexField(score_field=('upvotes', 'downvotes'), timestamp_field='posted')

    @property
    def score(self):
        return self.upvotes - self.downvotes

    class Meta:
        ordering = ('-heat',)

    def __str__(self):
        return self.title
