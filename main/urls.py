from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('', views.main, name='main'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('create/', views.create, name='create'),
    path('<str:auth>/<str:name>/', views.view, name='view'),
    path('settings/', views.settings, name='settings'),
    path('<str:auth>/<str:name>/add/', views.add, name="add"),
    path('history/', views.history, name="history"),
    path('profile/', views.profile, name="profile"),
    path('<str:auth>/<str:name>/<int:product>/', views.product, name="product"),
]

#handler404 = 'main.views.custom_404'