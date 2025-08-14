from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.http import HttpResponse
# blog/views.py
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# List all posts (public)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # path: templates/blog/post_list.html
    context_object_name = "posts"
    paginate_by = 10  # optional, remove if not wanted
    ordering = ["-published_date"]

# Show one post (public)
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Create a post (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        # set the author to the currently logged-in user before saving
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

# Update a post (only the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

# Delete a post (only the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def home(request):
    return HttpResponse("Welcome to the blog!")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account was created. Welcome!")
            login(request, user)  # auto-login after register
            return redirect("blog:profile")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("blog:profile")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, "auth/profile.html", {"form": form})
