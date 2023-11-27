"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import (list_posts_view, show_post_view, show_post_slug_view,
                        search_post_view, create_post_view, edit_post_view,
                        delete_post_view) #1
#from blog import views #2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', list_posts_view, name="list_post"), #1
   # path('list/', views.list_posts_view),#2
    path('display/<int:pid>/', show_post_view, name="show_post_by_id"),
    path('show/<slug:s>/', show_post_slug_view, name='show_post_by_slug'),
    path('edit/<slug:s>/', edit_post_view, name='edit_post'),
    path('search/<str:q>/', search_post_view, name="search_name"),
    path('create/post/', create_post_view, name="create_post"),
    path('delete/<int:pid>/', delete_post_view, name='delete_post'),

]
