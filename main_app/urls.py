from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/remove_food/<int:food_id>/',
         views.remove_food, name='remove_food'),
    path('dogs/<int:dog_id>/add_walking/',
         views.add_walking, name='add_walking'),

    # associate a food with a dog (M:M)
    path('dogs/<int:dog_id>/assoc_food/<int:food_id>/',
         views.assoc_food, name='assoc_food'),

    # food urls
    path('foods/', views.foods_index, name='all_foods'),
    path('foods/<int:food_id>/', views.food_detail, name='food_detail'),
    path('foods/create/', views.Create_Food.as_view(), name='create_food'),
    path('foods/<int:pk>/update/', views.Update_food.as_view(), name='update_food'),
    path('foods/<int:pk>/delete/', views.Delete_food.as_view(), name='delete_food'),
    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),

]
