# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from .models import Magazine
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def all_magazine(request):
    magazines = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazines})

# Create your views here.
