from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from .forms import *
from . import services


def home(request):
    code = request.LANGUAGE_CODE
    posts = services.post(code)
    followers = services.followers(code)
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
    ctx = {
        'form': form,
        'posts': posts,
        'followers': followers,
        'welcome': _("TEXT"),
    }
    return render(request, 'index.html', ctx)


