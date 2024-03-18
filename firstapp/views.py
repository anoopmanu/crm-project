from django.shortcuts import render

def hello(request):
    return render(request,'index.html')
def dashboard(request):
   dashboard = request.GET.get('dashboard',' ').split(',')
   return render(request, 'dashboard.html',{'dashboard':dashboard})
def archieve(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request, 'archieve.html', {'item_ids': item_ids})

