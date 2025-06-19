from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length= 200)
    published_date = models.DateTimeField("published_date")

class Choice (models.Model):
    choice_text = models.CharField(max_length= 200)
    vote = models.IntegerField(default=0)
    question =  models.ForeignKey(Question, on_delete=models.CASCADE)

    
