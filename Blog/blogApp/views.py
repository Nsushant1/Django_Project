from django.shortcuts import render,get_list_or_404,redirect
from blogApp.forms import BlogForm
from blogApp.models import Blog

# Create your views here.
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, "", {'form': form})

def blog_list(request):
    blog=Blog.objects.all().order_by("-created_at")
    return render(request, "", {"blog":blog})

def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, '', {'form': form})

def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, '', {'blog': blog})


