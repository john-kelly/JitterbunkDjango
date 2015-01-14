from django.db import models
from datetime import datetime


class Bunk(models.Model):
    #http://stackoverflow.com/questions/1142378/django-why-do-some-model-fields-clash-with-each-other
    #Django automatically creates a reverse relation from User back to
    #Bunk, which is usually bunk_set. However, because we
    #have two FKs, we must use 'related_name'
    from_user = models.ForeignKey('User', related_name='bunks_from_user')
    to_user = models.ForeignKey('User', related_name='bunks_to_user')

    #default doc: https://docs.djangoproject.com/en/1.7/ref/models/fields/#default
    time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return str(self.id) + ": " + (self.from_user.username +
                                      " Bunked " + self.to_user.username)


class User(models.Model):
    #Need to change this to django User Model
    username = models.CharField(max_length=30)

    #Figure this out in a bit
    #https://docs.djangoproject.com/en/1.7/ref/models/fields/#imagefield
    #photo = models.ImageField();

    def __unicode__(self):
        return self.username
