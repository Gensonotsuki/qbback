from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf import CSRFProtect

loginmanager = LoginManager()
# bootstrap = Bootstrap()
csrf = CSRFProtect()


# 注册蓝图
def blueprint(app):
    from apps.notebook.view.index import main
    from apps.notebook.view.user import usermsg
    from apps.notebook.view.aboutname import nike
    from apps.notebook.view.text import test
    app.register_blueprint(main)
    app.register_blueprint(usermsg)
    app.register_blueprint(nike)
    app.register_blueprint(test)


# 注册SQL数据库
def regist_db(app):
    from apps.notebook.model import db
    db.init_app(app)


# 创建app
def creat_notebook():
    # 初始化app对象
    note = Flask(__name__)
    # bootstrap.init_app(note)
    # 导入配置文件
    note.config.from_object('apps.cfg.ConfigOne')
    # 注册数据库
    regist_db(note)
    # 注册csrf
    csrf.init_app(note)
    # 注册蓝图
    blueprint(note)

    # 注册登陆状态管理
    loginmanager.init_app(note)
    # 进入需要登陆的页面,而没有登陆自动跳转到登陆页面
    loginmanager.login_view = 'usermsg.login'

    return note
