from flask import render_template, request, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table
from apps.notebook.form.e7form import Catalyst_Constellations
from apps.notebook.view.aboutname import nike
from apps.notebook.model.ep7mod import Catalyst, Constellation


@nike.route('/catalyst', endpoint='catalyst', methods=['GET', 'POST'])
def apitest():
    engine = create_engine('mysql+pymysql://root:111111@localhost/e7db')
    meta = MetaData(engine)
    connection = engine.connect()
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
    return render_template('addAttributes.html', form=cc_form, flag='添加催化剂')
