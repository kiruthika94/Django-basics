from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #elf instance of class object
    def __str__(self):
        return self.question_text
    def was_published_recently(self.pub_date):
	return now - datetime-timedelta(days=1)<= self.pubdate <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    comments=models.CharField(max_length=200)
