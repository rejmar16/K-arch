from django.shortcuts import render, get_object_or_404
from .models import Project, Project_Photo, Vizualizace
from django.utils import timezone

# Create your views here.

def contact_list(request):
    return render(request, 'page/contact_list.html', {})

def rd_list(request):
    rd = Project.objects.order_by('-published_date')
    return render(request, 'page/rd_list.html', {'rd' : rd})

def viz_list(request):
    vizualizace = Vizualizace.objects.order_by('-published_date')
    return render(request, 'page/viz_list.html', {'vizualizace' : vizualizace})

def RD_detail(request, pk, ip,):
    post = get_object_or_404(Project, pk=pk)
    photos = Project_Photo.objects.filter(rodinny_dum=pk).order_by('number')#.order_by('photo_name')
    large = Project_Photo.objects.filter(rodinny_dum=pk).order_by('number').all()[int(ip)-1]
    return render(request, 'page/RD_detail.html', {'post' : post , 'photos' : photos, 'large' : large,})

def rd_filter_RD(request):
    rd = Project.objects.order_by('-published_date')
    return render(request, 'page/rd_filter.html', {'rd' : rd , 'type': 'RD' , 'name' : 'rodinne domy'})

def rd_filter_INTER(request):
    rd = Project.objects.order_by('-published_date')

    return render(request, 'page/rd_filter.html', {'rd' : rd, 'type': 'INTER' , 'name' : 'interiery' })

def rd_filter_JINE(request):
    rd = Project.objects.order_by('-published_date')

    return render(request, 'page/rd_filter.html', {'rd' : rd, 'type': 'JINE' , 'name' : 'jine'})
