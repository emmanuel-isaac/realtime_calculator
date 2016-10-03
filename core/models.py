from django.db import models

# Create your models here.
class CalculatorData(models.Model):
    owner = models.CharField(max_length=250)
    entry = models.CharField(max_length=250)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b. %-d, %-I:%M %p')

    def __str__(self):
        return '[{timestamp}] {owner}: {entry} - {result}'.format(**self.as_dict())

    def as_dict(self):
        return {
            'owner': self.owner,
            'entry': self.entry,
            'result': self.result,
            'timestamp': self.formatted_timestamp,
        }
