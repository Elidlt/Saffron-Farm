from django.shortcuts import render
from django.http import HttpResponse
from .models import Worker
from django.template import loader

def index(request):
    workerList = Worker.objects.order_by('-id')
    template = loader.get_template("Manage/index.html")
    context = {
        'workerList': workerList,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
def detail(request, name_id):
    return HttpResponse("You're looking at Name %s." % name_id)

def results(request, name_id):
    response = "You're looking at the results of Name %s."
    return HttpResponse(response % name_id)

def vote(request, name_id):
    return HttpResponse("You're voting on Name %s." % name_id)