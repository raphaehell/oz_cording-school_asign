from django.shortcuts import render

def bolg_list(request):
    blogs= Blog.objects.all()

    context = {'blogs':blogs}
    return render(request,'blog_list.html',context)
