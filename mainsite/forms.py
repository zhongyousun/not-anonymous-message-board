from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='你的姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(label='請建立您的ID', max_length=10)
    password = forms.CharField(label='請輸入您的密碼', widget=forms.PasswordInput())
    email = forms.EmailField(label='請輸入您的電子郵件')


class PostForm(forms.Form):
    title = forms.CharField(label='標題', max_length=50)
    post = forms.CharField(label='想留什麼就留什麼', widget=forms.Textarea)