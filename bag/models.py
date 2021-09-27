from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.


class Items(models.Model):
    _pending = 'PENDING'
    _not_available = 'NOT AVAILABLE'
    _bought = 'BOUGHT'
    STATUS_CHOICES = (
        ('PD', _pending),
        ('NT', _not_available),
        ('BT', _bought)
    )

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True, help_text='uuid used for urls')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    quantity = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=25)

    def __str__(self):
        return self.title

    def str_status(self):
        if self.status == 0:
            return 'PENDING'
        if self.status == 1:
            return 'NOT_AVAILABLE'
        return 'BOUGHT'
