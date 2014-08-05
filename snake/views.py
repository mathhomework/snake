import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Max, Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from snake.forms import EmailUserCreationForm
from snake.models import Score


@login_required
def snake(request):
    return render(request, "snake.html")


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form
    })


@csrf_exempt
def user_high_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        my_scores = Score.objects.filter(user=request.user)
        print my_scores
        high_score = my_scores.aggregate(Max('score'))
        # The above, high_score, returns the max score as: {'score__max': 4}
        return HttpResponse(json.dumps(high_score), content_type='application/json')


@csrf_exempt
def send_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        Score.objects.create(game=data['game'], user = request.user, score=data['score'])
        return HttpResponse(json.dumps({'msg': 'Score submitted'}), content_type = 'application/json')


@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("login")
    else:
        my_scores = Score.objects.filter(user=request.user)
        data = {
            "scores": my_scores.order_by("-score"),
            "average": my_scores.aggregate(Avg('score'))
        }
        print data
        return render(request, 'profile.html', data)


def leaderboard(request):
    data = {"scores": Score.objects.order_by("-score")[:5]}
    print data
    return render(request, "leaderboard.html", data)