from __future__ import unicode_literals

from django.db import models

class Employee(models.Model):
	name = models.ForeignKey('auth.User')
	team = models.CharField(max_length=200)
	email = models.EmailField()
	points_to_give = models.IntegerField()
	points_received = models.IntegerField()

	def __str__(self):
		return self.name.username

	
