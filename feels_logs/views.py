# Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Entry
from .forms import EventForm, EntryForm
from django.http import Http404

# Project views
# Home page
def index(request):
	"""The home page for Feels Logs"""
	return render(request, 'feels_logs/index.html')

# Checks that event belongs to current user
def check_topic_owner(request, event):
	if event.owner != request.user:
		raise Http404


@login_required #python decorator
def events(request):
	"""Show all events"""
	events = Event.objects.filter(owner=request.user).order_by('date_added')
	context = {'events': events}
	return render(request, 'feels_logs/events.html', context)

@login_required #python decorator	
def event(request, event_id):
	"""Show a single event and all its entires"""
	event = Event.objects.get(id=event_id)
	
	# Make sure the event belongs to the current user
	check_topic_owner(request, event)

	entries = event.entry_set.order_by('-date_added')
	context = {'event': event, 'entries': entries}
	return render(request, 'feels_logs/event.html', context)

@login_required #python decorator	
def new_event(request):
	"""Add a new event."""
	if request.method != 'POST':
		#No data submitted (no http post); create a blank form
		form = EventForm()
	else:
		#POST data submitted; process data
		form = EventForm(data=request.POST)
		if form.is_valid():
			new_event = form.save(commit=False)
			new_event.owner = request.user
			new_event.save()
			return redirect('feels_logs:events')
			
	#Display a blank or invalid form
	context = {'form' : form}
	return render(request, 'feels_logs/new_event.html', context)

@login_required #python decorator	
def new_entry(request, event_id):
	"""Add a new entry for a particular event."""
	event = Event.objects.get(id=event_id)
	
	# Make sure the event belongs to the current user
	check_topic_owner(request, event)
	
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form = EntryForm()
	else:
		#POST data submitted; process data.
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.event = event
			new_entry.save()
			return redirect('feels_logs:event', event_id=event_id)

	#Display a blank or invalid form
	context = {'event': event, 'form': form}
	return render(request, 'feels_logs/new_entry.html', context)


@login_required #python decorator
def edit_entry(request, entry_id):
	"""Edit an existing entry"""
	entry = Entry.objects.get(id=entry_id)
	event = entry.event

	"""if event.owner != request.user:
		raise Http404"""
	# Make sure the event belongs to the current user
	check_topic_owner(request, event)

	if request.method != 'POST':
		# initial request; pre-fill form with the current entry
		form = EntryForm(instance=entry)
	else:
		# POST data submitted; process data
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('feels_logs:event', event_id=event.id)
	context = {'entry': entry, 'event': event, 'form': form}
	return render(request, 'feels_logs/edit_entry.html', context)

@login_required #python decorator
def delete_entry(request, entry_id):
	"""delete an existing entry"""
	entry = Entry.objects.get(id=entry_id)
	event = entry.event

	# Make sure the event belongs to the current user
	check_topic_owner(request, event)
	
	if request.method != 'POST':
		# initial request; pre-fill form with the current entry
		form = EntryForm(instance=entry)
	else:
		# Delete data submitted; process data
		entry.delete()
		return redirect('feels_logs:event', event_id=event.id)
	context = {'entry': entry, 'event': event, 'form': form}
	return render(request, 'feels_logs/delete_entry.html', context)

@login_required #python decorator	
def delete_event(request, event_id):
	"""Delete event - Show a single event and all its entires"""
	event = Event.objects.get(id=event_id)
	
	# Make sure the event belongs to the current user
	check_topic_owner(request, event)

	entries = event.entry_set.order_by('-date_added')

	context = {'event': event, 'entries': entries}

	return render(request, 'feels_logs/delete_event.html', context)


