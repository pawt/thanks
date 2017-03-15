from __future__ import unicode_literals

from django.db import models

class Employee(models.Model):
	name = models.ForeignKey('auth.User')
	points_to_give = models.IntegerField(default=100)
	points_collected = models.IntegerField(default=0)

	def __str__(self):
		return self.name.username

	
