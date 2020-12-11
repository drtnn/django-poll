from django.urls import path
from .import views

app_name = 'questions'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:poll_id>/', views.poll, name='poll'),
	path('<int:poll_id>/leave_poll/', views.leave_poll, name='leave_poll'),
]