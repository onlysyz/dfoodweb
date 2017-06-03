class LoginForm(forms.Form):
    username=forms.UsernameField(required=True,error_messages={'required':"用户名不能为空"})
    password=forms.PasswordField(max_length=120,min_length=6,required=True,error_messages={'required':"密码不能为空"})
