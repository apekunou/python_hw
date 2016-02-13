from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Players
from . import forms
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def base(request):
    template_data = {
    }
    return render(request, 'base.html', template_data)

@login_required()
def players(request):
    form = forms.PlayerEmailFilter()
    if 'email' in request.GET:
        lv_email = request.GET['email']
        player_list = Players.objects.filter(email = lv_email)
    else:
        player_list = Players.objects.all()

    paginator = Paginator(player_list, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        players = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        players = paginator.page(paginator.num_pages)

    template_data = {
        "players": players,
        "form": form,
        "version": "1.0"
    }
    return render(request, 'players.html', template_data)

@login_required()
def players_change_exp(request):
    if 'player_nickname' in request.GET:
        player_nickname = request.GET['player_nickname']
        player = Players.objects.get(nickname =  player_nickname)
        form_exp = forms.PlayerChangeExp(data={"name": player.nickname, "xp": player.xp})
    if request.method == 'POST':
        form_exp = forms.PlayerChangeExp(request.POST)
        if form_exp.is_valid():
            player_nickname = form_exp.cleaned_data["name"]
            player = Players.objects.get(nickname =  player_nickname)
            player.xp = form_exp.cleaned_data["xp"]
            player.save()
            return HttpResponseRedirect("/players")

    template_data = {
        "form": form_exp }

    return render(request, 'players_change_exp.html', template_data)


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/players")
    # Redirect to a success page.