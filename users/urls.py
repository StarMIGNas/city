# from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views
from . import views


app_name="users"
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
# urlpatterns = [
#     path('login/', views.LoginUser.as_view(), name='login'),
#     path('logout/', views.logout_user, name='logout'),
# ]

# urlpatterns = [
#     path('login/', views.login_user, name='login'),
#     path('logout/', views.logout_user, name='logout'),
# ]
# admin.site.site_header = "Панель администрирования"
# admin.site.index_title = "Городы"
#
# if settings.DEBUG:#02-12-2024
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)