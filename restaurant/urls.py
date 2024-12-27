
from django.urls import path, include
from .views import MenuView

urlpatterns=[

path('menus/', MenuView.as_view()),
path('menu/<int:pk>', MenuView.as_view()),

]