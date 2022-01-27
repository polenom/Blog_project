from django.shortcuts import render,get_object_or_404
from twoproject.models import Post, Comment
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger
from .forms import CommentForm
from taggit.models import Tag
# Create your views here.
def posts(request, tag_slug = None):
    posts = Post.objects.all()
    pageNum = request.GET.get('page')
    tag = None
    if tag_slug:

        tag = get_object_or_404(Tag, slug = tag_slug)
        posts = posts.filter(tags__in = [tag])
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(pageNum)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request,'Bil/post_list.html', {'posts':posts,
                                                 'page_number': pageNum,
                                                 'tag': tag,
                                                 })

def post(request,pk):
    post = get_object_or_404(Post, pk = pk)
    comments = post.adm.filter(active=True)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return render(request,"Bil/post.html", {"post" : post, 'comments': comments,'form': form})

def listing(request):
    post = Post.objects.all()
    paginator = Paginator(post, 4)


def numbers(request, dic):
    return HttpResponse(f'{dic} PRIVET')



def main(arg):
    return HttpResponse('Главная страница')

def blog(arg):
    return  HttpResponse('Блог')

def forMe(arg):
    return HttpResponse('Про себя')
