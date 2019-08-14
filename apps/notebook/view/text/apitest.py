from flask import render_template, request, redirect, url_for
# from sqlalchemy import create_engine, MetaData, Table
from apps.notebook.form.e7form import Hero_Name
from apps.notebook.view.text import test
from apps.notebook.model.ep7mod import Hero


@test.route('/test', endpoint='text', methods=['GET', 'POST'])
def apitest():
    # engine = create_engine('mysql+pymysql://root:111111@localhost/e7db')
    # meta = MetaData(engine)
    # connection = engine.connect()
    # catalyst = Catalyst.query.all()
    # shop = Shop.query.all()
    hn_form = Hero_Name(request.form)
    if request.method == 'POST' and hn_form.validate():
        # id_values = list(cs_form.data.values())
        # catalyst_id = id_values[1:]
        # shop_id = id_values[0]
        # cs_table = Table('catalyst_shops', meta, autoload=True)
        # cs_insert = cs_table.insert()
        # dic = []
        # for i in catalyst_id:
        #     dic.append({'catalyst_id': i, 'shop_id': shop_id})
        # connection.execute(cs_insert, dic)
        return redirect(url_for('test.text'))
    return render_template('test.html', form=hn_form, flag='添加')
