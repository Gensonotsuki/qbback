import pymongo


# 获取集合
def get_collection():
    client = pymongo.MongoClient('', 27017)
    db = client.ep7
    news_set = db.ep7_news_set
    return news_set


class E7set(object):

    def __init__(self, article_id, article_title, article, up_time, url):
        self.article_id = article_id
        self.article_title = article_title
        self.article = article
        self.up_time = up_time
        self.url = url

    def save(self):
        news = {'article_id': self.article_id,
                'article_title': self.article_title,
                'article': self.article,
                'up_time': self.up_time,
                'url': self.url
                }
        col = get_collection()
        col.insert(news)

    @staticmethod
    def query_news():
        news = get_collection().findall()
        return news
