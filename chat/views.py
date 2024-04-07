from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from courses.models import Course


@login_required
def course_chat_room(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'chat/room.html', {'course': course})
