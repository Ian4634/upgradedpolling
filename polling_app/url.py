from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('<str:username>/create_poll/', views.create_poll, name='create_poll'),
    path('<str:username>/create_poll/add/', views.add, name='add'),
    path('poll/<str:owner>/<str:poll_name>/', views.poll, name='poll'),
    path('<str:owner>/commit/', views.commit, name='commit'),
    path('home/inspection/<str:poll_name>/',
         views.inspection, name='inspection'),
    path('thank-filling/', views.thank_filling, name='thank-filling'),
    path('test/<str:poll_name>/', views.inspection1, name='test')

]

urlpatterns += staticfiles_urlpatterns()
