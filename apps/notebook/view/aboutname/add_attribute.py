from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import create_engine, MetaData, Table
from apps.notebook.form.e7form import Catalyst_Constellations, Hero_Constellations, Nice_Name, Catalyst_Shop, Hero_Name
from apps.notebook.model import db
from apps.notebook.view.aboutname import nike
from apps.notebook.model.ep7mod import Catalyst, Constellation, Hero, Nicename, Shop

engine = create_engine('mysql+pymysql://root:WOrinima@47.106.154.216/e7db')
meta = MetaData(engine)
connection = engine.connect()


# 根据星座添加催化剂
@nike.route('/catalyst', endpoint='catalyst', methods=['GET', 'POST'])
@login_required
def addcatalysts():
    user = current_user.username
    catalyst = Catalyst.query.all()
    cstl = Constellation.query.all()
    cc_form = Catalyst_Constellations(request.form, (catalyst, cstl))
    if request.method == 'POST' and cc_form.validate():
        id_values = list(cc_form.data.values())
        catalyst_id = id_values[:3]
        constellation_id = id_values[3]
        cc_table = Table('constellation_catalysts', meta, autoload=True)
        cc_insert = cc_table.insert()
        dic = []
        for i in catalyst_id:
            dic.append({'catalyst_id': i, 'constellation_id': constellation_id})
        connection.execute(cc_insert, dic)
        return redirect(url_for('name.catalyst'))
    return render_template('addAttributes.html', form=cc_form, flag='添加催化剂', user=user)


# 根据英雄名添加星座
@nike.route('/constellation', endpoint='constellation', methods=['GET', 'POST'])
@login_required
def addconstellations():
    user = current_user.username
    # engine = create_engine('mysql+pymysql://root:111111@localhost/e7db')
    # meta = MetaData(engine)
    # connection = engine.connect()
    hero = Hero.query.all()
    cstl = Constellation.query.all()
    hc_form = Hero_Constellations(request.form, (hero, cstl))
    if request.method == 'POST' and hc_form.validate():
        hc_table = Table('hero_constellations', meta, autoload=True)
        hc_insert = hc_table.insert()
        connection.execute(hc_insert, hc_form.data)
        return redirect(url_for('name.constellation'))
    return render_template('addAttributes.html', form=hc_form, flag='添加星座', user=user)


# 添加外号
@nike.route('/nikename', endpoint='nikename', methods=['GET', 'POST'])
@login_required
def addnicename():
    user = current_user.username
    hero = Hero.query.all()
    niceform = Nice_Name(request.form, hero)
    if request.method == 'POST' and niceform.validate():
        nicename = Nicename()
        nicename.set_attrs(niceform.data)
        db.session.add(nicename)
        db.session.commit()
        return redirect(url_for('name.nikename'))
    return render_template('addAttributes.html', form=niceform, flag='添加昵称', user=user)


# 根据野图商店添加催化剂
@nike.route('/cs', endpoint='cs', methods=['GET', 'POST'])
@login_required
def apitest():
    user = current_user.username
    # engine = create_engine('mysql+pymysql://root:111111@localhost/e7db')
    # meta = MetaData(engine)
    # connection = engine.connect()
    catalyst = Catalyst.query.all()
    shop = Shop.query.all()
    cs_form = Catalyst_Shop(request.form, (catalyst, shop))
    if request.method == 'POST' and cs_form.validate():
        id_values = list(cs_form.data.values())
        catalyst_id = id_values[1:]
        shop_id = id_values[0]
        cs_table = Table('catalyst_shops', meta, autoload=True)
        cs_insert = cs_table.insert()
        dic = []
        for i in catalyst_id:
            dic.append({'catalyst_id': i, 'shop_id': shop_id})
        connection.execute(cs_insert, dic)
        return redirect(url_for('name.cs'))
    return render_template('addAttributes.html', form=cs_form, flag='添加商店货物', user=user)


# 添加新的英雄,并把聊天数据写入Excel
@nike.route('/addhero', endpoint='addhero', methods=['GET', 'POST'])
@login_required
def addhero():
    user = current_user.username
    heroname_form = Hero_Name(request.form)

    if request.method == 'POST' and heroname_form.validate():
        heroname = Hero()
        heroname.set_attrs(heroname_form.data)
        db.session.add(heroname)
        db.session.commit()
        return redirect(url_for('index.index'))
    return render_template('addAttributes.html', form=heroname_form, flag='添加昵称', user=user)
