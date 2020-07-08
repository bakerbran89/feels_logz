from django.urls import path
from . import views

app_name = 'feels_logs'
urlpatterns = [
	#home page - blank string for default/home
	path('', views.index, name='index'),
	#evenets page
	path('events/', views.events, name='events'),
	#Detail page for a single event
	path('events/<int:event_id>/', views.event, name='event'),
	#page for adding a new event
	path('new_event/', views.new_event, name='new_event'),
	#page for adding a new entry
	path('new_entry/<int:event_id>/', views.new_entry, name='new_entry'),
	#page for editing an entry
	path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
	#page for deleting an entry
	path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
	#page for deleting an event
	path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
	path('leslie/', views.leslie, name='leslie')
]