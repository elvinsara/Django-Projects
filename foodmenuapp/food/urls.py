from django.urls import path
from . import views

app_name = 'food'
urlpatterns=[
    path('',views.helloworld,name='helloworld'),
    path('allfood/',views.getAllItems,name='allfood'),
    path('<int:pk>/',views.details,name='details'),
    path('additem/',views.addItem,name='additem'),
    path('update/<int:pk>',views.updateItem,name='updateitem'),
    path('delete/<int:pk>',views.deleteItem,name='deleteitem')
]