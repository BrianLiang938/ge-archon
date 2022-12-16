from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lookup/<int:item_id>', views.lookup, name='lookup'),
    path('lookup/', views.lookupSearch, name='lookupSearch')
]