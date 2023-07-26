from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from some_generic_sm.posts.models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['title', 'content']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

