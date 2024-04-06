from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('courses/mine/', views.ManageCourseListView.as_view(),
         name='course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(),
         name='course_delete'),
    path('lesson/list/', views.LessonListView.as_view(), name='lesson_list'),
]