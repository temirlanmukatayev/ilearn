# iLearn
Web platform for online courses

## Stack:
Django 4.2

Bootstrap 5 and Crispy Forms

DRF
- API for Subjects and Courses

Memcached
- Low-level cache: lesson detail content
- Page cache: All courses, All modules, All lessons

Django Channels, Daphne and Redis
- Online chat - fully asynchronous chat with separate rooms for each course

## Additional features:
- Media and static files support
- Django Debug Toolbar added
