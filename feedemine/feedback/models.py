from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
    feedback_user = models.CharField(max_length=255)
    feedback_description = models.CharField(max_length=1000)
    feedback_item = models.CharField(max_length=300)
    feedback_date = models.DateTimeField()
