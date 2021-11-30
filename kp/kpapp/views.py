from django.http import HttpResponse
from django.shortcuts import render
from .models import place, person


# Create your views here.
# def home(request):
#     return HttpResponse('welcome')

def home(request):
    obj=place.objects.all()
    obj1 = person.objects.all()

    return render(request,'index.html',{'result': obj , 'result1':obj1})
# def contact(request):
#     return HttpResponse('8547687052')
# def calculation(request):
#     x=int(request.GET['n1'])
#     y=int(request.GET['n2'])
#     r1=x+y
#     r2=x*y
#     r3=x/y
#     r4=x-y
#
#     return render(request,'html1.html',{'add':r1,'mul':r2,'div':r3,'sub':r4})
# def thanks(request):
#     return render(request,'html2.html')



