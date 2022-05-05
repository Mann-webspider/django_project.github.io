# from django.db import models

# Create your models here.
from django.db import models

class onlineFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class offlineFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)