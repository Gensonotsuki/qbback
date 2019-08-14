from flask import render_template, redirect, url_for, request
from flask_login import logout_user, login_user
from apps.notebook.view.user import usermsg
from apps.notebook.form.userform import RegistForm, LoginForm
from apps.notebook.model.usermodel import UserModel, db


# 注册
@usermsg.route('/regist', endpoint='regist', methods=['GET', 'POST'])
def regist():
    form = RegistForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserModel()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('usermsg.login'))
    return render_template('login_register.html', flag='注册', form=form)


# 登陆
@usermsg.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserModel.query.filter(UserModel.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index.index'))
        else:
            form.password.errors = ['用户名或密码错误']

    return render_template('login_register.html', form=form, flag='登陆')


# 注销
@usermsg.route('/logout', endpoint='logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index.index'))
