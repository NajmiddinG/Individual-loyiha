from django.shortcuts import render, redirect
from .models import Course, Teacher, Message, Qoshilish
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib import messages
from django.http.response import HttpResponseRedirect


def request_to_training(request):
    try:
        if request.POST:
            data = request.POST
            course_id = Course.objects.get(id=data['selected_course'])
            Qoshilish.objects.create(name=data['name'], phone=data['phone'], course=course_id)
            messages.success(request, f"Siz {course_id.name} kursiga muvafaqqiyatli so'rov yubordingiz!")
        else: messages.warning(request, "Xato so'rov yubordingiz!")
    except: messages.warning(request, "Xatolikga yo'l qo'ydingiz, qayta urinib ko'ring!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def request_to_message(request):
    try:
        if request.POST:
            data = request.POST
            Message.objects.create(name=data['name'], phone=data['phone'], subject=data['subject'], message=data['message'])
            messages.success(request, "Sizning xabaringiz muvaffaqiyatli yuborildi!")
        else: messages.warning(request, "Xato so'rov yubordingiz!")
    except: messages.warning(request, "Xatolikga yo'l qo'ydingiz, qayta urinib ko'ring!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def index(request):
    context = {
        'active': 'index',
        'courses': Course.objects.all().order_by('-date')[:9],
        'teachers': Teacher.objects.all().order_by('-date')[:9],
        }
    return render(request, 'index.html', context=context)

def about(request):
    context = {
        'active': 'about',
        'courses': Course.objects.all().order_by('-date')[:9]
    }
    return render(request, 'about.html', context=context)

def contact(request):
    context = {
        'active': 'contact',
        'courses': Course.objects.all().order_by('-date')[:9]
    }
    return render(request, 'contact.html', context=context)

def course(request):
    count = 9
    pages = Paginator(Course.objects.all().order_by('-date'), count)
    page_number = request.GET.get('page')
    try:
        f = count*(int(page_number)-1)
    except: f = 1
    context = {
        'active': 'course',
        'page_obj': pages.get_page(page_number),
        'count': f,
        'courses': Course.objects.all().order_by('-date')[:9]

        }
    return render(request, 'course.html', context=context)

def detail(request, id):
    context = {
        'active': 'detail',
        'detail': Course.objects.get(id=id),
        'courses': Course.objects.all().order_by('-date')[:9]
    }
    return render(request, 'detail.html', context=context)

def feature(request):
    context = {
        'active': 'feature',
        'courses': Course.objects.all().order_by('-date')[:9]
    }
    return render(request, 'feature.html', context=context)

def team(request):
    context = {
        'active': 'team',
        'teachers': Teacher.objects.all().order_by('-date')[:9],
        'courses': Course.objects.all().order_by('-date')[:9]
    }
    return render(request, 'team.html', context=context)
