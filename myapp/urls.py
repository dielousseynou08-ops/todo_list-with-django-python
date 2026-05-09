


from django.urls import path
from . import views


urlpatterns = [
    path('', views.List_todo, name = 'todo' ),
    path('create/', views.todo_create, name= 'todo_create'),
    path('details/<int:id>', views.details, name='detail'),
    path('delete/<int:id>',views.supprimer_todo, name='delete'),
    path('todo/update/<int:id>', views.update_todo, name='update_todo')

    
    
]