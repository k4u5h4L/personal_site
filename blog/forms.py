from django.forms import ModelForm, Form
from .models import Post, Comment
from users.models import Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'tags']
        exclude = ['author']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['reply_text']
        exclude = ['author', 'parent_post']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ['full_name','location','phone_no','personal_site', 'bio']

class ProfilePicUpdateForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']