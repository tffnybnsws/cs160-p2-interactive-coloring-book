from django.shortcuts import render

def search(request):
    return render(request, 'coloring/search.html')
  
def archive(request):
    return render(request, 'coloring/archive.html')
  
def index(request):
    return render(request, 'coloring/index.html')