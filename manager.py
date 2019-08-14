from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, MigrateCommand

from apps.notebook.model import db
from apps.notebook import creat_notebook

# 生成app对象
app = creat_notebook()

# 创建数据库,跑一次就注释掉

Migrate(app, db)
# db.create_all()
manager = Manager(app, db)
manager.add_command('db', MigrateCommand)
Bootstrap(app)
print(app.url_map)
if __name__ == '__main__':
    manager.run()
