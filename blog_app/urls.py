from django.urls import path
from . import views


app_name = 'blog_app'
urlpatterns =[
    path('',views.home, name='home'),
    path('<str:pk>', views.error),
    
    
]