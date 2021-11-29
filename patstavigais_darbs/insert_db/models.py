from django.db import models



class User(models.Model):

        username = models.CharField(max_length=77)
        e_mail = models.EmailField(max_length=78)
        reason = models.CharField(max_length=78)