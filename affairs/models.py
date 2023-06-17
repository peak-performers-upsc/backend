from django.db import models

# Create your models here.
class CurrentAffairs(models.Model):
    Title = models.TextField()
    Content = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Current_affairs'

        