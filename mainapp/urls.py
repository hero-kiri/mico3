from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('treatment/', views.treatment, name='treatment'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    # Добавить пути для соханения данных в базу данных емейлов
    path('subscribe/', views.subscribe, name='subscribe_email'),
]


