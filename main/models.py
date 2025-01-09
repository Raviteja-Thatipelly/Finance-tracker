from django.db import models

# Create your models here.

# type': type,
#                 'source': source,
#                 'paid_to': paid_to,
#                 'mode_of_payment': mode_of_payment,
#                 "amount": amount,
#                 'currency': currency,
#                 'description': description,
#                 'date': date,
#                 'time_stamp_created': datetime.datetime.now,
#                 'time_stamp_updated': datetime.datetime.now




class transactions(models.Model):
        TRANSACTIONS_TYPES = [
                ('income', 'Income'),
        ('expense', 'Expense'), 
    ]

        type = models.CharField(max_length=10, choices=TRANSACTIONS_TYPES)
        source = models.CharField(max_length=100, null=True, blank=True)
        paid_to = models.CharField(max_length=100, null=True, blank=True)
        mode_of_payment = models.CharField(max_length=50)
        amount= models.DecimalField(max_digits=10, decimal_places=2)
        currency = models.CharField(max_length=10)
        description = models.TextField(null= True, blank=True)
        date = models.DateField()
        time_stamp_created = models.DateTimeField(auto_now_add=True)
        time_stamp_updated = models.DateTimeField(auto_now=True)
    
def __str__(self):
    return f'{self.type.capitalize()}-{self.amount} {self.currency}'