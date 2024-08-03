from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_laptop_view, name='add_url'),
    path('show/', views.show_laptop_view, name='show_url'),
    path('update/<int:id>/', views.update_laptop_view, name='update_url'),
    path('delete/<int:id>/' , views.delete_laptop_view, name='delete_url')
]