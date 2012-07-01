from django.shortcuts import render_to_response
from models import Course
from django.template import RequestContext

def courses(request):
    courses = Course.objects.all()
    ctx = {'courses':courses}
    return render_to_response('courses.html', RequestContext(request, ctx))