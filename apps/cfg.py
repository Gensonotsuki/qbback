from datetime import timedelta

import redis


def get_path():
    import os
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


class BaseCfg():
    SECRET_KEY = ''  # 设置密钥...最好是个固定字符串
    SESSION_TYPE = 'redis'  # 设置session的类型为Redis
    SESSION_PERMANENT = True  # 关闭浏览器session不过期,默认过期时间为一个月....
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6388')
    TOKEN_EXPIRES = 24 * 3600
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///{get_path()}/e7db.sqlite'  # 数据库地址
    # SQLALCHEMY_BINDS = {'e7db': f'sqlite:///{get_path()}/e7db.sqlite',
    #                     'user': f'sqlite:///{get_path()}/user.sqlite',
    #                     }
    SQLALCHEMY_BINDS = {'e7db': '',
                        'user': '',
                        }
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigOne(BaseCfg):
    DEBUG = True
