from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Comment


class UserRegistrationForm(UserCreationForm):
    """用户注册表单"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': '请输入邮箱地址'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入用户名'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入密码'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '请确认密码'
            }),
        } 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    """评论表单"""
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': '请写下您的评论...'
        }),
        max_length=500
    )
    
    class Meta:
        model = Comment
        fields = ['content']


class UserProfileForm(forms.ModelForm):
    """用户资料表单"""
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': '介绍一下自己吧...'
        }),
        max_length=500,
        required=False
    )
    
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '所在城市'
        }),
        max_length=100,
        required=False
    )
    
    website = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': '个人网站（可选）'
        }),
        required=False
    )
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'website', 'avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }


class CommentForm(forms.ModelForm):
    """评论表单"""

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "写下你的评论...",
                    "class": "form-control",
                }
            ),
        }
        labels = {
            "content": "评论内容",
        }


class UserRegistrationForm(UserCreationForm):
    """用户注册表单"""

    email = forms.EmailField(required=True, help_text="必填。请输入有效的邮箱地址")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if (
            email
            and User.objects.filter(email=email).exclude(username=username).exists()
        ):
            raise forms.ValidationError("该邮箱地址已被使用")
        return email


class UserLoginForm(forms.Form):
    """用户登录表单"""

    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "请输入用户名"}
        ),
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "请输入密码"}
        ),
    )
    remember_me = forms.BooleanField(
        label="记住我",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
