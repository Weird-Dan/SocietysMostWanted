from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

"""
IndexView
the hompage
"""
class IndexView(generic.ListView):
    template_name = "smw/index.html"

    def get_queryset(self):
        return Post.objects.order_by('-Wants')[:6]

"""
FlowView
the flow of ideas
"""
class FlowView(generic.ListView):
    template_name = "smw/flow.html"

    def get_queryset(self):
        return Post.objects.order_by("-Post_Date")

"""
CategoryView
the view of all categories
"""
class CategoryView(generic.ListView):
    template_name = "smw/categories.html"

    def get_queryset(self):
        return Category.objects.all()

"""
Cat (short for Category) view
the flow of one Category
"""
def Cat(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    post = cat.post_set.all();
    return render(request, "smw/flow.html", {"object_list":post, "category":cat})

"""
Idea view
a detailed view of a post
"""
def Idea(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.Views = post.Views+1
    post.save()
    comments = post.comment_set.all()
    return render(request, "smw/idea.html", {"post":post, "comments":comments})

"""
Search View
the flow view of a Search
"""
def search(request):
    if request.method == 'POST':
        txt = request.POST.get("q", None)
        object_list = Post.objects.filter(Idea__icontains=txt)
        return render(request, "smw/flow.html", {"object_list":object_list, "q":txt})

    return redirect("smw:flow")

class CategoryCreate(CreateView):
    model = Category
    fields =["Category", "Description", "Icon_Image"]

"""
Create Post Form View
"""
class PostCreate(CreateView):
    model = Post
    fields = ["User", "Category","Title", "Idea", "Tags"]

    """
    def form_valid(self, form):
        pst = Post(User=self.request.user, Category=form.Category, Title=form.Title, Idea=form.Idea, Tags=form.Tags)
        pst.save()
        print("created new post ")
        return redirect("smw:index")
    """

"""
AboutView
"""
class AboutView(generic.ListView):
    template_name = "smw/about.html"

    def get_queryset(self):
        return Post.objects.order_by('-Wants')[:6]
