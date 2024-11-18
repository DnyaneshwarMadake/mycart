from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
from django.contrib.auth.decorators import login_required


# from mac.blog.models import Blogpost


# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})

@login_required
def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    total_posts = Blogpost.objects.count()
    return render(request, 'blog/blogpost.html', {'post': post, 'total_posts': total_posts})


def blog_detail(request, post_id):
    # Get the current post
    current_post = get_object_or_404(Post, id=post_id)

    # Get the next post (post with an id greater than the current one)
    next_post = Post.objects.filter(id__gt=current_post.id).order_by('id').first()

    # Get the previous post (post with an id smaller than the current one)
    previous_post = Post.objects.filter(id__lt=current_post.id).order_by('-id').first()

    context = {
        'post': current_post,
        'next_post': next_post,
        'previous_post': previous_post,
    }

    return render(request, 'blogpost.html', context)
