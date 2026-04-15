from django.db import models

class Transaction(models.Model):
    user_name = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    is_fraud = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Simple fraud rule
        if self.amount > 10000:
            self.is_fraud = True
        else:
            self.is_fraud = False
        super().save(*args, **kwargs)

    def _str_(self):
        return self.user_name