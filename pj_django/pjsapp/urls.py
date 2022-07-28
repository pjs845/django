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
    path('b_list3/', views.b_list3, name='b_list3'),
    path('b_list5/', views.b_list5, name='b_list5'),
    path('b_list10/', views.b_list10, name='b_list10'),
    path('b_write/', views.b_write, name='b_write'),
    path('b_write/b_write_ok/', views.b_write_ok, name='b_write_ok'),
    path('b_list3/b_content/<int:id>', views.b_content, name='b_content'),
    path('b_list5/b_content/<int:id>', views.b_content, name='b_content'),
    path('b_list10/b_content/<int:id>', views.b_content, name='b_content'),
    path('b_update/<int:id>', views.b_update, name='b_update'),
    path('b_update/b_update_ok/<int:id>', views.b_update_ok, name='b_update_ok'),
    path('b_delete/<int:id>', views.b_delete, name='b_delete'),
]