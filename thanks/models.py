from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class Employee(models.Model):
    name = models.ForeignKey('auth.User')
    points_to_give = models.IntegerField(default=100)
    points_collected = models.IntegerField(default=0)

    def __str__(self):
        return self.name.username


class Transaction(models.Model):
    giver = models.ForeignKey('thanks.Employee', related_name = "giver")
    receiver = models.ForeignKey('thanks.Employee', related_name = "receiver")
    description = models.TextField(default='')
    points_given = models.IntegerField()
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return "Transaction #" + str(self.id) + str(self.giver) + " -> " + str(self.receiver)

    def make(self):
        self.date = timezone.now()
        self.save()
