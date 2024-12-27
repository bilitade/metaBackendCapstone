from django.urls import path
from .views import MenuListView, MenuDetailView

urlpatterns = [
    path('menus/', MenuListView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
]
