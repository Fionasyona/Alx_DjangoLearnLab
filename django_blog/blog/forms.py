from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas."
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]  # author is set automatically in the view
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Post title"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 10,
                "placeholder": "Write your post..."
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        # Handle tags
        tags_str = self.cleaned_data.get('tags', '')
        tag_list = [t.strip() for t in tags_str.split(',') if t.strip()]
        instance.tags.clear()
        for tag_name in tag_list:
            tag_obj, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag_obj)
        return instance


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "avatar")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a comment...'
            }),
        }
