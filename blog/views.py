from django.shortcuts import render ,get_object_or_404 , redirect
from blog.models import Comment , Post 
from blog.forms import Commentforms
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect ,Http404

# Create your views here.
def blog_home(request , **kwargs):
    currnt_time = timezone.now()
    posts = Post.objects.filter(published_date__lte = currnt_time , status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('tag_name') != None:
        posts=posts.filter(tag__name__in=[kwargs['tag_name']])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username =kwargs['author_username'])
    posts = Paginator( posts, 3)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage :
        posts = posts.get_page(1)
    context = {'posts':posts }
    return render(request, 'blog/blog-home.html' , context)




def blog_single(request , pid):
    if request.method == 'POST':
        form = Commentforms(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your comment has been registered. Then the review will be displayed')
        else:
            messages.add_message(request,messages.ERROR,'your tikct didnt submited')
    currnt_time=timezone.now()
    posts=get_object_or_404(Post,pk=pid,status=1,published_date__lte=currnt_time)
    next_post = Post.objects.filter(id__gt=pid, status=1, published_date__lte=currnt_time).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=pid, status=1, published_date__lte=currnt_time).order_by('-id').first()
    posts.counted_views+=1
    posts.save()
    if posts.login_required==False:
        comments=Comment.objects.filter(post=posts.id,approwed=True)
        form=Commentforms()
        context={'post':posts,'comments':comments,'next_post':next_post,'prev_post':prev_post,'form':form}
        return render(request,'blog/blog-single.html',context)  
    elif posts.login_required==True and request.user.is_authenticated:
        posts.login_required=False
        comments=Comment.objects.filter(post=posts.id,approwed=True)
        form=Commentforms()
        context={'post':posts,'comments':comments,'next_post':next_post,'prev_post':prev_post,'form':form}
        return render(request,'blog/blog-single.html',context)
    return HttpResponseRedirect(reverse('login'))



def blog_category(request,cat_name):
    currnt_time=timezone.now()
    posts=Post.objects.filter(status=1,published_date__lte=currnt_time)
    posts=posts.filter(category__name=cat_name)
    if not posts.exists():
        messages.add_message(request,messages.ERROR,'The desired phrase was not found. Please try again')
        return HttpResponseRedirect('/blog/')  
    context={'posts':posts}
    return render(request,'blog/blog-caregories.html',context)


def blog_search(request):
    current_time = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=current_time)
    if 's' in request.GET:
        s = request.GET.get('s')
        if s:
            posts = posts.filter(content__contains=s)
    if not posts.exists():
        messages.add_message(request,messages.ERROR,'The desired phrase was not found. Please try again')
        return HttpResponseRedirect('/blog/')    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)