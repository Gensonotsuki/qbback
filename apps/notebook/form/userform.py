from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, validators

from apps.notebook.model.usermodel import UserModel


# 登陆表单
class LoginForm(Form):
    username = StringField(validators=[validators.DataRequired(message='请输入用户名'),
                                       validators.length(min=3, message='用户名长度需要大于3'),
                                       validators.length(max=10, message='用户名长度不能大于10'),
                                       ],
                           label='用户名',
                           render_kw={'class': 'form-control', 'placeholder': '请输入用户名'},
                           )
    password = PasswordField(validators=[validators.DataRequired(message='请填写密码')],
                             label='密码:',
                             render_kw={"class": 'form-control'},
                             )


# 注册表单验证
class RegistForm(LoginForm):
    password2 = PasswordField(validators=[validators.EqualTo('password', message='两次输入密码不一致')],
                              label='请再次输入密码:',
                              render_kw={"class": 'form-control'},
                              )

    def validate_username(self, val):  # 验证用户是否唯一
        user = UserModel.query.filter(UserModel.username == val.data).first()
        if user:
            raise validators.ValidationError(message='该用户名已被注册')
