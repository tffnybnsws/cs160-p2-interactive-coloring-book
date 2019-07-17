from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
  
def search(request):
    return render(request, 'coloring/search.html')
  
def archive(request):
    return render(request, 'coloring/archive.html')
  
def archive(request):
    return render(request, 'coloring/aphex.html')