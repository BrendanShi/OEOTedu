from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('courses_list/', views.course_list, name='courses_list'),  # 链接课程列表页
    path('course_edit/<int:id>/', views.course_edit, name='course_edit'),
    path('course_failed/', views.course_failed, name='course_failed'),
    path('course_delete_stu/<int:id>/', views.course_delete_stu, name='course_delete_stu'),
    path('course_detail/<int:id>/', views.course_detail, name='course_detail'),
    path('like/', views.user_like, name='like'),
    path('post_add/', views.post_add, name='post_add'),
    path('post/detail/<int:id>/', views.post_detail, name='post_detail'),
    # 更新公告
    path('post/update/<int:id>/', views.post_update, name='post_update'),
    path('course_apply/<int:id>/', views.course_apply, name='course_apply'),

    # 删除——艾鹏
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),
    # 人员表——艾鹏
    path('department/<int:id>/', views.profile_list, name='department_detail'),
    path('company/', views.company, name='company'),
    # 部门以及部门详情 ————薛斌
    path('post/section_list/', views.section_list, name='section_list'),
    path('post/section_details/<int:id>/', views.section_details, name='section_details'),
    path('company/', views.company, name='company'),
    #     # 班级详细介绍----王帅
    path('class_list/', views.class_list, name='class_list'),  # 班级列表
    path('class_detail/<int:class_id>/', views.class_detail, name='class_detail'),  # 班级详情
    path('duty_list/', views.duty_list, name='duty_list'),
    # 值日表--小罗小王
    path('stu_note/', views.stu_note, name='stu_note'),
    path('duty_list/',views.duty_list,name='duty_list'),

    path('create_course/', views.course_add, name='create_course'),
    path('course_delete/<int:id>/', views.course_delete, name='course_delete'),
    #最新课程---王凯杰
    path('new/courses/',views.new_course,name='new_course'),
]
