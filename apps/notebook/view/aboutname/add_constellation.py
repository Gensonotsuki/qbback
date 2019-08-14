from flask import render_template, redirect, request, url_for
from flask_login import current_user
from sqlalchemy import create_engine, MetaData, Table

from apps.notebook.form.e7form import Hero_Constellations
from apps.notebook.view.aboutname import nike
from apps.notebook.model.ep7mod import Hero, Constellation


@nike.route('/constellation', endpoint='constellation', methods=['GET', 'POST'])
def apitest():
    user = current_user.username
    engine = create_engine('mysql+pymysql://root:111111@localhost/e7db')
    meta = MetaData(engine)
    connection = engine.connect()
    hero = Hero.query.all()
    cstl = Constellation.query.all()
    hc_form = Hero_Constellations(request.form, (hero, cstl))
    if request.method == 'POST' and hc_form.validate():
        hc_table = Table('hero_constellations', meta, autoload=True)
        hc_insert = hc_table.insert()
        connection.execute(hc_insert, hc_form.data)
        return redirect(url_for('index.index'))
    return render_template('addAttributes.html', form=hc_form, flag='添加星座', user=user)
