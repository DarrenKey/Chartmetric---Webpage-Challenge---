from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.BigIntegerField('Account ID')
    content = models.JSONField('Content')
    timestamp = models.DateTimeField('Timestamp')
    created_at = models.DateTimeField('Created At')
    modified_at = models.DateTimeField('Modified At')

    def __str__(self):
        return self.name