from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from users.forms import LoginUserForm

menu =[
    {'title':'Главная','url_name':'home'},
    {'title':'Добавить страницу','url_name':'add_city'},
    {'title':'О нас','url_name':'about'},
    {'title':'Войти','url_name':'login'}
]
menu2=[
    {'title':'Войти','url_name':'login'},
    {'title':'Выход','url_name':'logout'}
]

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 print("User logged in:", user.username)  # Отладочный вывод
#                 return HttpResponseRedirect(reverse('home'))
#         else:
#             print("Form is not valid:", form.errors)  # Отладочный вывод
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form, 'menu': menu})
menu =[
    {'title':'Главная','url_name':'home'},
    {'title':'Добавить страницу','url_name':'add_city'},
    {'title':'О нас','url_name':'about'},
]
class LoginUser(LoginView):
    form_class =  LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('home')

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form,'menu':menu})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))