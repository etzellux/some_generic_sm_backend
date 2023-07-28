from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from some_generic_sm.posts.models import Post, Comment
from some_generic_sm.posts.forms import PostForm, CommentForm


class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'posts/post_create.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('post_detail', pk=new_post.pk)
        return render(request, 'posts/post_create.html', {'form': form})


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
    

class PostCommentsView(View):
    template_name = 'posts/post_comments.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        return render(request, self.template_name, {'comments': comments, 'post': post})


class PostCreateCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()

        return render(request, 'posts/post_create_comment.html', {'form': form, 'post': post})


class PostDeleteCommentView(LoginRequiredMixin, View):
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, id=pk, user=request.user)
        comment.delete()
        return redirect(reverse('post_comments', args=[comment.post.pk]))

