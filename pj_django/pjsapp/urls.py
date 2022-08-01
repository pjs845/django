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
    
    path('login/', views.login, name='login'),
    path('login/login_ok/', views.login_ok, name='login_ok'),
    path('logout/', views.logout, name='logout'),
    
    #템플릿 테스트
    path('template1/', views.test1, name='template1'),
    path('template2/', views.test2, name='template2'),
    path('template3/', views.test3, name='template3'),
    path('template4/', views.test4, name='template4'),
    path('template5/', views.test5, name='template5'),
    path('template6/', views.test6, name='template6'),
    path('template7/', views.test7, name='template7'),
    path('template8/', views.test8, name='template8'),
]