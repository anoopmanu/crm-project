from django.shortcuts import render

def hello(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')

