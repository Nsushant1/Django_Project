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
    return render(request, "", {"blogs":blog})


