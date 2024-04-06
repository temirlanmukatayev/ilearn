from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Course, Lesson


class OwnerRequiredMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class SetOwnerMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerRequiredMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, SetOwnerMixin):
    template_name = 'courses/manage/course/form.html'


class HomepageView(TemplateView):
    template_name = 'home.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'


class LessonListView(OwnerRequiredMixin, ListView):
    model = Lesson
    template_name = 'courses/manage/lesson/list.html'


class LessonDetailView(OwnerRequiredMixin, DetailView):
    model = Lesson
    template_name = 'courses/manage/lesson/detail.html'


class LessonCreateView(LoginRequiredMixin, SetOwnerMixin, CreateView):
    model = Lesson
    fields = ['module', 'title', 'slug', 'description', 'order',
              'content', 'image', 'file', 'video']
    template_name = 'courses/manage/lesson/form.html'
    success_url = reverse_lazy('lesson_list')


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = Lesson
    fields = ['module', 'title', 'slug', 'description', 'order',
              'content', 'image', 'file', 'video']
    template_name = 'courses/manage/lesson/form.html'
    success_url = reverse_lazy('lesson_list')


class LessonDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Lesson
    template_name = 'courses/manage/lesson/delete.html'
    success_url = reverse_lazy('lesson_list')
