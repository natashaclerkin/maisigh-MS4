from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm

# Create your views here.


def all_blog_posts(request):
    """
    A view to show all the blog posts
    """

    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_posts.html', context)


def blog_detail(request, slug):
    """
    A view to show individual blog posts
    """

    blog = get_object_or_404(BlogPost, slug=slug)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    """
    Add a blog post to the blog page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is only for store owners.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Successfully added blog post.')
            return redirect(reverse('blog_detail', args=[new_blog.slug]))
        else:
            messages.error(
                request, 'Failed to add blog post. \
                    Please check the form is valid and try again.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, slug):
    """
    Edit a blog post on the blog page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is only for store owners.')
        return redirect(reverse('home'))

    blog = get_object_or_404(BlogPost, slug=slug)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post')
            return redirect(reverse('blog_detail', args=[blog.slug]))
        else:
            messages.error(request, 'Failed to add blog post. \
                Please check the form is valid and try again.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing "{blog.title}" .')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """
    Delete a blog post from the blog page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is only for store owners.')
        return redirect(reverse('home'))

    blog = get_object_or_404(BlogPost, slug=slug)
    blog.delete()
    messages.success(request, f'Successfully deleted "{blog.title}".')
    return redirect(reverse('blogs'))
