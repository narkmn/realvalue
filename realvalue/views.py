from django.shortcuts import render
from . import utils


def home(request):
    return render(request, 'index.html')


def askinfo(request):
    user_input = request.GET['user_input']
    user_input_type = request.GET['user_input_type']
    dt = utils.autobox(user_input, user_input_type)
    return render(request, 'askinfo.html', dt)


def result(request):
    return render(request, 'result.html')
