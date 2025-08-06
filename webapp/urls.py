from django.urls import path
from . import views


# My urls
urlpatterns = [ 
    path('', views.home, name = 'home'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('wedding/', views.wedding, name = 'wedding'),
    path('birth_day/', views.birth_day, name = 'birth_day'),
    path('conference/', views.conference, name = 'conference'),
    path('corporate/', views.corporate, name = 'corporate'),
    path('our_work/', views.our_work, name = 'our_work'),
    path('team/', views.team, name = 'team'),
    path('special_events/', views.special_events, name = 'special_events'),
    path('career/', views.career, name = 'career'),
    path('contact/', views.contact, name = 'contact'),
    # path('test', views.test, name="test"),
]