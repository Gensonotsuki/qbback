from apps.notebook.model import BaseModel, db

# 英雄名--星座,中间表
hero_constellations = db.Table('hero_constellations',
                               db.Column('hero_id',
                                         db.Integer,
                                         db.ForeignKey('hero.id')),
                               db.Column('constellation_id',
                                         db.Integer,
                                         db.ForeignKey('constellation.id')),
                               info={'bind_key': 'e7db'})

# 星座--催化剂中间表
constellation_catalyst = db.Table('constellation_catalysts',
                                  db.Column('constellation_id',
                                            db.Integer,
                                            db.ForeignKey('constellation.id')),
                                  db.Column('catalyst_id',
                                            db.Integer,
                                            db.ForeignKey('catalyst.id')),
                                  info={'bind_key': 'e7db'})

# 催化剂--商店中间表
catalyst_shop = db.Table('catalyst_shops',
                         db.Column('catalyst_id', db.Integer, db.ForeignKey('catalyst.id')),
                         db.Column('shop_id', db.Integer, db.ForeignKey('shop.id')),
                         info={'bind_key': 'e7db'})


# 昵称表
class Nicename(BaseModel):
    __tablename__ = 'nicename'
    __bind_key__ = 'e7db'
    nicename = db.Column(db.String(64))
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    constellation = db.relationship('Hero',
                                    lazy='subquery',
                                    backref='nicenames'
                                    )

    def keys(self):
        return 'nicename'

    def __repr__(self):
        return f'{self.heroname}'


# 英雄表
class Hero(BaseModel):
    __tablename__ = 'hero'
    __bind_key__ = 'e7db'
    heroname = db.Column(db.String(64))
    constellation = db.relationship('Constellation', secondary=hero_constellations, backref='heros')
    nicename = db.relationship('Nicename', backref='heros')

    def keys(self):
        return 'heroname'

    def __repr__(self):
        return f'{self.heroname}'


# 星座表
class Constellation(BaseModel):
    __bind_key__ = 'e7db'
    __tablename__ = 'constellation'
    constellation = db.Column(db.String(16))
    # 反查询英雄表
    hero = db.relationship('Hero',
                           lazy='subquery',
                           secondary=hero_constellations,
                           backref=db.backref('constellations', lazy=True)
                           )
    # 反查询 催化剂表
    catalyst = db.relationship('Catalyst',
                               lazy='subquery',
                               secondary=constellation_catalyst,
                               backref=db.backref('constellations', lazy=True)
                               )

    def __repr__(self):
        return f'{self.constellation}'


# 催化剂表
class Catalyst(BaseModel):
    __bind_key__ = 'e7db'
    __tablename__ = 'catalyst'
    catalyst = db.Column(db.String(16))
    # qb的图片地址
    qbaddr1 = db.Column(db.String(64))
    # web端的图片地址
    webaddr2 = db.Column(db.String(64))
    # 反查询星座表
    constellation = db.relationship('Constellation',
                                    lazy='subquery',
                                    secondary=constellation_catalyst,
                                    backref=db.backref('catalysts', lazy=True)
                                    )
    # 反查询 商店表
    shop = db.relationship('Shop',
                           lazy='subquery',
                           secondary=catalyst_shop,
                           backref=db.backref('catalysts', lazy=True)
                           )

    def __repr__(self):
        return f'{self.catalyst}'


# 商店表
class Shop(BaseModel):
    __bind_key__ = 'e7db'
    __tablename__ = 'shop'
    shop = db.Column(db.String(32))
    # 反查询 催化剂表
    catalyst = db.relationship('Catalyst',
                               lazy='subquery',
                               secondary=catalyst_shop,
                               backref=db.backref('shops', lazy=True)
                               )

    def __repr__(self):
        # 打印结果  商店
        return f'{self.shop}'

