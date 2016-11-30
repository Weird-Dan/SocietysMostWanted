from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.core.exceptions import ObjectDoesNotExist
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
        object_list = Post.objects.filter(Idea__icontains=txt)|Post.objects.filter(Title__icontains=txt)|Post.objects.filter(Tags__icontains=txt)
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
    fields = ["Category","Title", "Idea", "Tags"]

    def form_valid(self, form):
        pst = Post(User=self.request.user, Category=form.cleaned_data['Category'], Title=form.cleaned_data['Title'], Idea=form.cleaned_data['Idea'], Tags=form.cleaned_data['Tags'])
        pst.save()
        print("created new post '"+form.cleaned_data['Title']+"'")
        return redirect("smw:index")

"""
AboutView
"""
class AboutView(generic.ListView):
    template_name = "smw/about.html"

    def get_queryset(self):
        return Post.objects.order_by('-Wants')[:6]
"""
create comment
"""
def cmt(request, pk):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        user = request.user
        text = request.POST.get("comment", None)
        try:
            sc = Comment.objects.get(Post=post, User=user, Text=text)
            return redirect("smw:idea", pk=pk)
        except ObjectDoesNotExist:
            comment = Comment(Post=post, User=user, Text=text)
            comment.save()

    return redirect("smw:idea", pk=pk)


def want(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    post.Wants.add(user)
    post.Shlts.remove(user)
    post.save()
    return redirect("smw:idea", pk=pk)

def shlt(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    post.Shlts.add(user)
    post.Wants.remove(user)
    post.save()
    return redirect("smw:idea", pk=pk)
