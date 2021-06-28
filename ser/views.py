from django.shortcuts import render
def services(request):
    context={'ser_active':'active'}
    return render(request,'ser/services.html',context)
# Create your views here.
