from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Videoclub


def index(request):
    videoclubs = Videoclub.objects.all()
    #list_students = ", "\
    #   .join([student.name for student in students])
    #return HttpResponse(list_students)
    dictionary = {'videoclubs': videoclubs}
    return render(request, 'videoclub/index.html', dictionary)
