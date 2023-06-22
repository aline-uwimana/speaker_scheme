from django.shortcuts import render

# Create your views here.




def insert(request):
    return render(request, 'insert.html')

def read(request):
    return render(request, 'read.html')

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')
