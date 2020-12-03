from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.core.paginator import Paginator

from django.contrib.auth.models import User


# Create your views here.
# posts = [
#     {
#         'author': 'Rahul Rai',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2020'
#     },
#     {
#         'author': 'Satyam Rai',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'October 30, 2020'
#     },
#     {
#         'author': 'Ravindra Goutam',
#         'title': 'Blog Post 3',
#         'content': 'Third post content',
#         'date_posted': 'October 25, 2020'
#     },
# ]


def home(request):
    objects = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(objects, 3)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'about.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = 'user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class DetailPost(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'update_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
