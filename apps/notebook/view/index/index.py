from flask import render_template, request, redirect, url_for
from flask_login import current_user

from apps.notebook.form.e7form import Nice_Name
from apps.notebook.model import db
from apps.notebook.model.ep7mod import Hero, Nicename
from apps.notebook.view.index import main
from apps.notebook.model.e7set_Model_mongo import E7set


# 首页视图
@main.route('/', endpoint='index', methods=['GET', 'POST'])
def index():
    news = E7set.query_news().sort('article_id')
    hero = Hero.query.all()
    nice = Nicename.query.order_by('-id').all()[:3]
    niceform = Nice_Name(request.form, hero)
    if request.method == 'POST' and niceform.validate():
        nicename = Nicename()
        nicename.set_attrs(niceform.data)
        db.session.add(nicename)
        db.session.commit()
        return redirect(url_for('index.index'))
    try:
        user = current_user.username
        return render_template('index.html', user=user, news=news, form=niceform, nice=nice)
    except:
        return render_template('index.html', news=news, nice=nice)
