from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from time import localtime, strftime

def index(request):
    return render(request, 'index.html')

def submit(request):
    name = request.POST['name']
    student_id = request.POST['student_id']
    lychee = request.POST['lychee']
    rambutan = request.POST['rambutan']
    jackfruit = request.POST['jackfruit']
    return redirect(f'/checkout/{name}/{student_id}/{lychee}/{rambutan}/{jackfruit}')
    # return HttpResponse(lychee)

def checkout(request, name, student_id, lychee, rambutan, jackfruit):
    context ={
        'name' : name,
        'student_id' : student_id,
        'lychee' : lychee,
        'rambutan' : rambutan,
        'jackfruit' :  jackfruit,
        'time': strftime("%m-%d-%Y  %H:%M %p ", localtime()),
        'count': int(lychee)+int(rambutan)+int(jackfruit)
    }

    return render(request, 'checkout.html', context)