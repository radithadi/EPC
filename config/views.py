from django.shortcuts import render
from django.conf import settings  
    
def error400(request, exception=None):
    return render(request, 'errors/400.html', status=400)

def error403(request, exception=None):
    return render(request, 'errors/403.html', status=403)

def error404(request, exception=None):
    return render(request, 'errors/404.html', status=404)

def error500(request, exception=None):
    return render(request, 'errors/500.html', status=500)