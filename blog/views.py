from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import BlogTitle, BlogText
from .models import PostTitle, PostText

from .forms import PostTitleForm, TextForm

# Functions.

def check_topic_owner(object, request):

    """Make sure the topic belongs to the current user."""

    from django.http import Http404

    if object.holder != request.user:

        raise Http404
    
# Views.

def index(request):

    """Home page."""

    return render(request, 'blog/index.html')

@login_required
def all_posts(request):

    """View for the Blog's Posts Page."""

    posts = PostTitle.objects.filter(holder=request.user.id).order_by('pub_date')

    context = {'posts' : posts}

    return render (request, 'blog/all_posts.html', context)

@login_required
def post(request, post_title):

    """View for a single post."""

    post = PostTitle.objects.get(id = post_title)
    texts = post.posttext_set.order_by('pub_date')

    # Verification
    check_topic_owner(post, request)

    context = {'post' : post, 'texts' : texts}

    return render (request, 'blog/post.html', context)

@login_required
def new_post(request):

    """Add a new post."""

    if request.method != 'POST':

        form = PostTitleForm()

    else:

        form = PostTitleForm(data = request.POST)

        if form.is_valid():

            new_post = form.save(commit=False)
            new_post.holder = request.user
            new_post.save()
            return redirect('blog:index')
        
    context = {'form' : form}

    return render(request, 'blog/new_post.html', context)

@login_required
def new_post_text(request, post_title):

    post = PostTitle.objects.get(id = post_title)

    if request.method != 'POST':

        form = TextForm()

    else:

        form = TextForm(data=request.POST)

        if form.is_valid():

            new_posttext= form.save(commit=False)
            new_posttext.post_title = post
            new_posttext.save()

            return redirect('blog:post', post_title = post_title)
        
    context = {'post' : post, 'form' : form}

    return render(request, 'blog/new_post_text.html', context)

@login_required
def edit_text(request, posttext_id):

    text = PostText.objects.get(id = posttext_id)
    title = text.post_title

    # Verification
    check_topic_owner(title, request)

    if request.method != 'POST':

        form = TextForm(instance = text)

    else:

        form = TextForm(instance = text, data = request.POST)

        if form.is_valid():

            form.save()
            return redirect ('blog:post', post_title = title.id)

    context = {'text' : text, 'title' : title, 'form' : form}
    return render(request, 'blog/edit_text.html', context)