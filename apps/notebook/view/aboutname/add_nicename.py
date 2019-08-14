from flask import render_template, request, redirect, url_for

from apps.notebook.form.e7form import Nice_Name
from apps.notebook.view.aboutname import nike
from apps.notebook.model import db
from apps.notebook.model.ep7mod import Hero, Nicename


@nike.route('/nikename', endpoint='nikename', methods=['GET', 'POST'])
def addnicename():
    hero = Hero.query.all()
    niceform = Nice_Name(request.form, hero)
    if request.method == 'POST' and niceform.validate():
        nicename = Nicename()
        nicename.set_attrs(niceform.data)
        db.session.add(nicename)
        db.session.commit()
        return redirect(url_for('name.nikename'))
    return render_template('addAttributes.html', form=niceform, flag='添加昵称')
