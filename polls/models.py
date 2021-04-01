import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length = 200)
    created_at = models.DateTimeField('data published')
    def __str__(self):
        return self.text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE)
    text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.text