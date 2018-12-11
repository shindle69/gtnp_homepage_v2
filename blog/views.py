from django.shortcuts import get_object_or_404,render
from .models import Post

# Create your views here.
def blog_list(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'blog/blog_list.html',context)

def blog_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html',{
        'post_list':post_list,
    })
'''
def item(request):
    return render(request,'blog/item.html',)
'''
def root(request):    
    return render(request,'blog/layout.html',)

def company(request):    
    return render(request,'blog/company.html',)

def moto(request):    
    return render(request,'blog/moto.html',)


def iot(request):    
    return render(request,'blog/iot.html',)

def app(request):    
    return render(request,'blog/app.html',)

def web(request):    
    return render(request,'blog/web.html',)

def series(request):    
    return render(request,'blog/series.html',)