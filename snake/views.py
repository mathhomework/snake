from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, "snake.html")

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form
    })




@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("login")
    return render(request, 'profile.html', {})
