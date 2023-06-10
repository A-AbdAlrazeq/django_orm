from django.shortcuts import render, redirect

from .models import Dojo, Ninja


def index(request):
    context = {
        "all_the_Dojos": Dojo.objects.all(),
        "all_the_Ninjas": Ninja.objects.all(),
    }
    return render(request, "index.html", context)


def create_dojo(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'],
                        state=request.POST['state'])
    return redirect('/')


def create_Ninja(request):
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                         dojo=Dojo.objects.get(id=request.POST['Dojo']),)
    return redirect('/')


def delete_dojo(request, ID):
    dojo = Dojo.objects.get(id=ID)
    dojo.delete()
    return redirect('/')
