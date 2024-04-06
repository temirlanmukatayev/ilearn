from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('course/all/', views.CourseListAllView.as_view(), name='course_all'),
    path('course/list/', views.ManageCourseListView.as_view(),
         name='course_list'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/detail/<pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/edit/<pk>/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('course/delete/<pk>/', views.CourseDeleteView.as_view(),
         name='course_delete'),
    path('lesson/list/', views.LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/detail/<pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/edit/<pk>/', views.LessonUpdateView.as_view(), name='lesson_edit'),
    path('lesson/delete/<pk>/', views.LessonDeleteView.as_view(), name='lesson_delete'),
]