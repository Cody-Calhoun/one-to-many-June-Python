from django.shortcuts import render, redirect
from .models import User, Taco

# Create your views here.


def index(request):
    context ={
        'users': User.objects.all(),
        'tacos': Taco.objects.all()
    }
    return render(request, 'index.html', context)

def create_user(request):
    user = User.objects.create(
        name = request.POST['name'],
        weight = request.POST['weight'],
        age = request.POST['age'],
        always_hungry = request.POST['hungry']
    )
    
    
    return redirect('/')

def create_taco(request):
    user_associated = User.objects.get(id=request.POST['user'])
    taco1 = Taco.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        meat = request.POST['meat'],
        spicy = request.POST['spicy'],
        user = user_associated
    )
    return redirect('/')


