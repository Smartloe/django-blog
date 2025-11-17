from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


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
