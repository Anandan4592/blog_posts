from django.shortcuts import render,redirect
from django.views.generic import ListView ,TemplateView
from .models import Blog
from .forms import BlogForm
from django.utils import timezone
# Create your views here.


class Bloglist(ListView):
    """This is used to show all the contents in Blog table """
    model = Blog
    template_name = 'bloglist.html'
    context_object_name = 'blogposts'


class Addblog(TemplateView):

    """This is used to add contents into the Blog table """

    def get(self, request):
        form = BlogForm()
        return render(request, 'addblog.html', {'form': form})

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bloglist')  
        return render(request, 'addblog.html', {'form': form})
    
class Updateblog(TemplateView):

    """This is used to update contents in the Blog table """

    def get(self, request, id):
        blogpost = Blog.objects.get(id=id)
        form = BlogForm(instance=blogpost)
        return render(request, 'addblog.html', {'form': form})

    def post(self, request, id):
        blogpost = Blog.objects.get(id=id)
        form = BlogForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            blogpost.created_date=timezone.now()
            form.save()
            return redirect('bloglist')
        return render(request, 'addblog.html', {'form': form})
