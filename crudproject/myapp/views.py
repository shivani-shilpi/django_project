from django.shortcuts import render

def add_show(request):
    return render(request, 'myapp/addandshow.html')