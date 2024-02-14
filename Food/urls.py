
from django.urls import path
from . import views

app_name='Food'

urlpatterns = [
    
    #home
    path('home/', views.IndexClassView.as_view(), name='index'),
    #details for a specific item   
    path('<int:pk>/',views.FoodClassView.as_view(),name='detail'),
    #adding a new item
    path('add/', views.CreateItem.as_view(), name='add_item'),
    #editing a certain item
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    #Deleting a certain item
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

]