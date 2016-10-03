from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CalculatorData(models.Model):
    owner = models.ForeignKey(User)
    input = models.CharField(max_length=250)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def __str__(self):
        return "{} - {} at {}".format(input, result, self.formatted_timestamp)

    def as_dict(self):
        return {
            owner: self.owner,
            input: self.input,
            result: self.result,
            timestamp: self.formatted_timestamp,
        }
