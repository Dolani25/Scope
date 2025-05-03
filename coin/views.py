from django.shortcuts import render, get_object_or_404

from core.models import Airdrop
# Create your views here.

def module(req, slug):
    airdrop = get_object_or_404(Airdrop, slug=slug)
    return render(req , 'coin/module.html' , {
    'airdrop' : airdrop
    })