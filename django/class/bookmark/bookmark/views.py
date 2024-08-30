from django.http import HttpResponse
from django.shortcuts import render


def bookmark_list(request):
    # return HttpResponse("<h1>북마크 리스트 페이지 입니다</h1>")
    return  render(request, 'bookmark_list.html')

def bookmark_detail(request,number):
    return render(request, 'bookmark_detail.html',{'number':number})
#모델 먼저 파악하기 /view 함수랑 매핑 어떻게 하는지 복습 중요/url파라메터 어떻게 잡는지