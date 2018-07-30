from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Data(models.Model):
    key = models.CharField(max_length=200)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s : %s' % (self.key, self.value)
