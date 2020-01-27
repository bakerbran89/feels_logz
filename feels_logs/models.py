from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
	"""A life event"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text

class Entry(models.Model):
	"""Entry from each emotion regarding the event"""
	event = models.ForeignKey(Event, on_delete=models.CASCADE) #entry references an event
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""Return a string representation of the model"""
		if len(self.text)>50:
			return f"{self.text[:50]}..."
		else:
			return self.text