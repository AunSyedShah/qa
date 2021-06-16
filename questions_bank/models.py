from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=1000, default="")
    option = models.CharField(max_length=100, default="")
    course_code = models.CharField(max_length=10, default="")
    page_number = models.IntegerField(default=0)

    def __str__(self):
        return self.question
