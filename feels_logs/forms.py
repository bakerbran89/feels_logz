from django import forms
from .models import Event, Entry

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['text']
		labels = {'text': ''}
		
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': 'Entry:'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
