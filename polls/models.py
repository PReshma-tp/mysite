import datetime
from django.db import models
from django.utils import timezone 


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length= 200)
    published_date = models.DateTimeField("published_date")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        current_time = timezone.now()
        a_day_before_current_time = timezone.now()-datetime.timedelta(days=1)
        is_published_recent = self.published_date >= a_day_before_current_time and self.published_date<=current_time
        return is_published_recent

class Choice(models.Model):
    choice_text = models.CharField(max_length= 200)
    vote = models.IntegerField(default=0)
    question =  models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


