from django.urls import path

from fileuser import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register),
    path('logout/', views.logout_view)
]