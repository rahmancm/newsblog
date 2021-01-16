from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):

    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(user=user, password=password)

    return render(request, 'login.html')
