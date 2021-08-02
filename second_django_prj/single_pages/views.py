from django.shortcuts import render
from blog.models import ulsanann, yeosuann, busanann, incheonann,daumnews,youtube

def landing(request):
    ulsan = ulsanann.objects.all().order_by('-pk')[:4]

    return render(
        request,
        'single_pages/landing.html',
    {
        'ulsanann': ulsan
    }
)
def ann(request):
    ulsan = ulsanann.objects.all().order_by('-pk')[:4]
    incheon = incheonann.objects.all().order_by('-pk')[:4]
    busan = busanann.objects.all().order_by('-pk')[:4]
    yeosu = yeosuann.objects.all().order_by('-pk')[:4]
    return render(
        request,
        'single_pages/ann.html',
    {
        'ulsanann': ulsan,
        'yeosuann': yeosu,
        'busanann': busan,
        'incheonann': incheon,
    }
)
def news(request):
    daum = daumnews.objects.all().order_by('-pk')[:4]
    youtu = youtube.objects.all().order_by('-pk')[:4]
    return render(
        request,
        'single_pages/news.html',
    {
        'daumnews': daum,
        'youtube': youtu,
    }
)


def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
def algo(request):
    return render(
        request,
        'single_pages/algo.html'
    )
def geomap(request):
    return render(
        request,
        'single_pages/geomap.html'
    )
