from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    '''
    A list of a bunch of items that will be displayed
    ie 28 things to remember when making fondue or something
    '''
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True, null=True,
    )
