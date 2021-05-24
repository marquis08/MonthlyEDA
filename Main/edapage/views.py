from django.shortcuts import render

# Create your views here.
app_name = 'edapage'
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def eda(request):
    return render(request, 'eda.html')