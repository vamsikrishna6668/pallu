from django.shortcuts import render
from .models import Wishes
# Create your views here.
def showIndex(request):
    return render(request,"index.html")

def SayWish(request):
    return render(request,"wishes.html")

def SayWishes(request):
    name=request.POST.get("t1")
    relation=request.POST.get("t2")
    textarea=request.POST.get("t3")
    w=Wishes(name=name,relation=relation,textarea=textarea)
    w.save()
    return render(request,"wishes.html",{"msg":"Thank for giving Wishes To Them."})


def Logout(request):
    return render(request,"index.html")


