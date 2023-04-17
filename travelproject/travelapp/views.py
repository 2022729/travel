from django.http import HttpResponse
from django.shortcuts import render
from .models import place
# Create your views here.
def demo(request):
   obj=place.objects.all()
   return render(request,"index.html",{'result':obj})
#def addition(request):
 #  a=int(request.GET['n1'])
  # b=int(request.GET['n2'])
   #addition=a+b
   #sub=a-b
   #mul=a*b
   #div=a/b
   #return render(request,"result.html",{'obj': addition,'x': sub,'y': mul,'z': div})


