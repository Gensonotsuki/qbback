from wtforms import Form
from wtforms import StringField, IntegerField, validators, TextAreaField, SelectField
from wtforms import HiddenField


class Hero_Name(Form):
    chat1 = StringField(validators=[validators.DataRequired(message='')],
                        label='聊天选项1',
                        render_kw={"class": "form-control",
                                   "placeholder": "请输入英雄聊天1",
                                   })
    chat2 = StringField(validators=[validators.DataRequired(message='')],
                        label='聊天选项2',
                        render_kw={"class": "form-control",
                                   "placeholder": "请输入英雄聊天2",
                                   })

    hero = StringField(validators=[validators.DataRequired(message='请输入英雄名')],
                       label='英雄名',
                       render_kw={"class": "form-control",
                                  "placeholder": "请输入英雄英文名",
                                  }
                       )

    advice = StringField(validators=[validators.DataRequired(message='烦恼咨询')],
                         label='烦恼咨询',
                         render_kw={"class": "form-control",
                                    "placeholder": "烦恼咨询",
                                    }
                         )
    belief = StringField(validators=[validators.DataRequired(message='信仰')],
                         label='信仰',
                         render_kw={"class": "form-control",
                                    "placeholder": "请输入英雄英文名",
                                    }
                         )
    bizarrestory = StringField(validators=[validators.DataRequired(message='猎奇的故事')],
                               label='猎奇的故事',
                               render_kw={"class": "form-control",
                                          "placeholder": "猎奇的故事",
                                          }
                               )

    comfortingcheer = StringField(validators=[validators.DataRequired(message='安慰助阵')],
                                  label='安慰助阵',
                                  render_kw={"class": "form-control",
                                             "placeholder": "安慰助阵",
                                             }
                                  )
    complain = StringField(validators=[validators.DataRequired(message='耍赖')],
                           label='耍赖',
                           render_kw={"class": "form-control",
                                      "placeholder": "耍赖",
                                      }
                           )
    criticism = StringField(validators=[validators.DataRequired(message='批判世界')],
                            label='批判世界',
                            render_kw={"class": "form-control",
                                       "placeholder": "批判世界",
                                       }
                            )
    cutecheer = StringField(validators=[validators.DataRequired(message='撒娇助阵')],
                            label='撒娇助阵',
                            render_kw={"class": "form-control",
                                       "placeholder": "撒娇助阵",
                                       }
                            )

    dream = StringField(validators=[validators.DataRequired(message='怀揣梦想')],
                        label='怀揣梦想',
                        render_kw={"class": "form-control",
                                   "placeholder": "怀揣梦想",
                                   }
                        )
    foodstory = StringField(validators=[validators.DataRequired(message='食物故事')],
                            label='食物故事',
                            render_kw={"class": "form-control",
                                       "placeholder": "食物故事",
                                       }
                            )
    gossip = StringField(validators=[validators.DataRequired(message='八卦')],
                         label='八卦',
                         render_kw={"class": "form-control",
                                    "placeholder": "八卦",
                                    }
                         )
    happymemory = StringField(validators=[validators.DataRequired(message='幸福回忆')],
                              label='幸福回忆',
                              render_kw={"class": "form-control",
                                         "placeholder": "幸福回忆",
                                         }
                              )

    heroiccheer = StringField(validators=[validators.DataRequired(message='英雄助阵')],
                              label='英雄助阵',
                              render_kw={"class": "form-control",
                                         "placeholder": "英雄助阵",
                                         }
                              )
    interestingstory = StringField(validators=[validators.DataRequired(message='冒险故事')],
                                   label='冒险故事',
                                   render_kw={"class": "form-control",
                                              "placeholder": "冒险故事",
                                              }
                                   )
    heroictale = StringField(validators=[validators.DataRequired(message='英雄故事')],
                             label='英雄故事',
                             render_kw={"class": "form-control",
                                        "placeholder": "英雄故事",
                                        }
                             )
    horrorstory = StringField(validators=[validators.DataRequired(message='恐怖故事')],
                              label='恐怖故事',
                              render_kw={"class": "form-control",
                                         "placeholder": "恐怖故事",
                                         }
                              )
    joyfulmemory = StringField(validators=[validators.DataRequired(message='愉快回忆')],
                               label='愉快回忆',
                               render_kw={"class": "form-control",
                                          "placeholder": "愉快回忆",
                                          }
                               )
    myth = StringField(validators=[validators.DataRequired(message='神话')],
                       label='神话',
                       render_kw={"class": "form-control",
                                  "placeholder": "神话",
                                  }
                       )
    occult = StringField(validators=[validators.DataRequired(message='秘术')],
                         label='秘术',
                         render_kw={"class": "form-control",
                                    "placeholder": "秘术",
                                    }
                         )
    realitycheck = StringField(validators=[validators.DataRequired(message='正视现实')],
                               label='正视现实',
                               render_kw={"class": "form-control",
                                          "placeholder": "正视现实",
                                          }
                               )

    sadmemory = StringField(validators=[validators.DataRequired(message='伤心回忆')],
                            label='伤心回忆',
                            render_kw={"class": "form-control",
                                       "placeholder": "伤心回忆",
                                       }
                            )
    selfindulgent = StringField(validators=[validators.DataRequired(message='自我陶醉')],
                                label='自我陶醉',
                                render_kw={"class": "form-control",
                                           "placeholder": "自我陶醉",
                                           }
                                )
    uniquecomment = StringField(validators=[validators.DataRequired(message='四次元发言')],
                                label='四次元发言',
                                render_kw={"class": "form-control",
                                           "placeholder": "四次元发言",
                                           }
                                )


class Nice_Name(Form):
    nicename = StringField(validators=[validators.DataRequired(message='请输入昵称外号')],
                           label='昵称',
                           render_kw={"class": "form-control",
                                      "placeholder": "请输入昵称"}
                           )
    hero_id = SelectField(label='英雄名',
                          render_kw={"class": "form-control"},
                          validators=[validators.DataRequired(message='选择英雄')],
                          coerce=int,
                          )

    def __init__(self, *args, **kwargs):
        super(Nice_Name, self).__init__(*args, **kwargs)
        k, v = args
        self.hero_id.choices = [(x.id, x.heroname) for x in v]


class Hero_Constellations(Form):
    hero_id = SelectField(label='英雄名',
                          render_kw={"class": "form-control"},
                          validators=[validators.DataRequired(message='选择英雄')],
                          coerce=int,
                          )
    constellation_id = SelectField(label='星座名',
                                   render_kw={"class": "form-control"},
                                   validators=[validators.DataRequired(message='选择星座')],
                                   coerce=int,
                                   )

    def __init__(self, *args, **kwargs):
        super(Hero_Constellations, self).__init__(*args, **kwargs)
        k, v = args
        # 英雄名
        self.hero_id.choices = [(x.id, x.heroname) for x in v[0]]
        self.constellation_id.choices = [(x.id, x.constellation) for x in v[1]]


class Catalyst_Constellations(Form):
    catalyst_id_1 = SelectField(label='催化剂1',
                                render_kw={"class": "form-control"},
                                validators=[validators.DataRequired(message='选择催化剂')],
                                coerce=int,
                                )
    catalyst_id_2 = SelectField(label='催化剂2',
                                render_kw={"class": "form-control"},
                                validators=[validators.DataRequired(message='选择催化剂')],
                                coerce=int,
                                )
    catalyst_id_3 = SelectField(label='催化剂3',
                                render_kw={"class": "form-control"},
                                validators=[validators.DataRequired(message='选择催化剂')],
                                coerce=int,
                                )

    constellation_id = SelectField(label='星座名',
                                   render_kw={"class": "form-control"},
                                   validators=[validators.DataRequired(message='选择星座')],
                                   coerce=int,
                                   )

    def __init__(self, *args, **kwargs):
        super(Catalyst_Constellations, self).__init__(*args, **kwargs)
        k, v = args
        # 英雄名
        self.catalyst_id_1.choices = [(x.id, x.catalyst) for x in v[0]]
        self.catalyst_id_2.choices = [(x.id, x.catalyst) for x in v[0]]
        self.catalyst_id_3.choices = [(x.id, x.catalyst) for x in v[0]]
        self.constellation_id.choices = [(x.id, x.constellation) for x in v[1]]


class Catalyst_Shop(Form):
    shop_id = SelectField(label='商店名',
                          render_kw={"class": "form-control"},
                          validators=[validators.DataRequired(message='选择商店')],
                          coerce=int,
                          )
    catalyst_id_1 = SelectField(label='催化剂1',
                                render_kw={"class": "form-control"},
                                validators=[validators.DataRequired(message='选择催化剂')],
                                coerce=int,
                                )
    catalyst_id_2 = SelectField(label='催化剂2',
                                render_kw={"class": "form-control"},
                                validators=[validators.DataRequired(message='选择催化剂')],
                                coerce=int,
                                )
    catalyst_id_3 = SelectField(label='催化剂3',
                                render_kw={"class": "form-control"},
                                validators=[validators.DataRequired(message='选择催化剂')],
                                coerce=int,
                                )
    catalyst_id_4 = SelectField(label='催化剂4',
                                render_kw={"class": "form-control"},
                                validators=[validators.DataRequired(message='选择催化剂')],
                                coerce=int,
                                )

    def __init__(self, *args, **kwargs):
        super(Catalyst_Shop, self).__init__(*args, **kwargs)
        k, v = args
        # 英雄名
        self.catalyst_id_1.choices = [(x.id, x.catalyst) for x in v[0]]
        self.catalyst_id_2.choices = [(x.id, x.catalyst) for x in v[0]]
        self.catalyst_id_3.choices = [(x.id, x.catalyst) for x in v[0]]
        self.catalyst_id_4.choices = [(x.id, x.catalyst) for x in v[0]]
        self.shop_id.choices = [(x.id, x.shop) for x in v[1]]
