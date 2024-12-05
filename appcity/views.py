from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from appcity.models import City
from .forms import  AddPostForm

menu =[
    {'title':'Главная','url_name':'home'},
    {'title':'Добавить страницу','url_name':'add_city'},
    {'title':'О нас','url_name':'about'},

]
menu2=[
    {'title':'Погода','url_name':'Weather'},
    {'title':'Финансы','url_name':'financ'}
]

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def index(request):
    posts=City.objects.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }

    return render(request, 'city/index.html',context = data)

@login_required
def add_city(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)  # Не забудьте передать request.FILES
        if form.is_valid():
            form.save()  # Сохранение формы автоматически сохранит изображение
            return redirect("home")
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form,
    }
    return render(request, 'city/add_city.html', data)



def about(request):
    data = {
        'menu': menu,
    }

    return render(request,'city/about.html',context=data)

def login(request):
    data = {
        'menu': menu,
        'menu2': menu2,
    }
    return render(request,"city/Login.html",context = data)

def show_post(request, post_slug):
    post = get_object_or_404(City, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'city/post.html', context=data)