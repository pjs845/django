from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'), #추가
    path('write/', views.write, name='write'), #추가
    path('write/write_ok/', views.write_ok, name='write_ok'), #추가
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/update_ok/<int:id>', views.update_ok, name='update_ok'),
]