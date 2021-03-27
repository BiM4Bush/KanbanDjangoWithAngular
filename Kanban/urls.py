from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('notes/', views.notesList, name="noteslist"),
	path('note-detail/<int:pk>/', views.noteDetail, name="note-detail"),
	path('note-create/', views.noteCreate, name="note-create"),

	path('note-update/<int:pk>/', views.noteUpdate, name="note-update"),
	path('note-delete/<int:pk>/', views.noteDelete, name="note-delete"),
]