"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from http.client import responses

from django.contrib import admin
from django.http import HttpResponse
from django.template.context_processors import request
from django.urls import path
from django.shortcuts import render



movie_list =[
    {'title':'인사이드 아웃2','director':'디즈니'},
    {'title':'데드폴과 울버린','director':'홍길동'},
    {'title':'슈퍼배드 4','director':'아무개'},
    {'title':'듄 파트2','director':'언년이'},
]
def index(request):
    return HttpResponse('hello')

def book_list(request):
    book_text = ''

    for i in range(0,10):
        book_text +=f'book{i}<br>'

    return HttpResponse(book_text)

def book(request,num):
    book_text = f'book{num}번 페이지 입니다.'

    return HttpResponse(book_text)


def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.')

def python(request):
    return HttpResponse('python 페이지입니다.')

def movies(request):
    # movie_titles = [
    #     f'<a href="/movie/{index}/">{movie["title"]}</a><br>' for index, movie in enumerate(movie_list)]
    #
    #
    # # movie_titles = []
    # # for movie in movie_list:
    # #     movie_titles.append(movie['title'])\
    #
    # responses_text = '<br>'.join(movie_titles)
    #
    # for index, title in enumerate(movie_titles):
    #     responses_text += f'<a href="/movie/{index}/">{title}</a><br>'
    #
    # return HttpResponse(responses_text)
    from django.shortcuts import render
    return render(request, 'movies.html', {'movie_list': movie_list})


def movie_detail(request,index):
    movie = movie_list[index]

    responses_text = f'<h1>{movie["title"]}</h1> <p>감독: {movie["director"]}</p>'
    return HttpResponse(responses_text)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('book_list/', book_list),
    path('book_list/<int:num>/',book),
    path('language/<str:lang>/', language),
    path('language/python/', python),
    path('movie/', movies),
    path('movie/<int:index>/',movie_detail),
]
