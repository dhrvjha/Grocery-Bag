
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list_view, name='item-list'),
    path('add/', views.item_create_view, name='item-create'),
    path('update/<uuid:item_id>/', views.item_update_view, name='item-update'),
    path('delete/<uuid:item_id>/', views.delete_view, name='item-delete')
    # path('delete/<uuid:pk>/', views.item_delete_view, name='item-delete')
]
