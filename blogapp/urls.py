from django.urls import path
from . import views


urlpatterns = [
	path('',views.index),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('contact/', views.contact, name = 'contact'),
	path('tutorial/', views.tutorial, name = 'tutorial'),



]
