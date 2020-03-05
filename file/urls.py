from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_files, name='home'),
    path('addfile/', views.add_file_view),
    path('addfolder/', views.add_folder_view)
]