from django.test import TestCase
from .models import Editor, Article,tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.gichi = Editor(first_name='gichi', last_name='mu', email='gichimu@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.gichi, Editor))

    def test_save_method(self):
        self.gichi.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

class ArticleTestClass(TestCase):
    #setup method
    def setUp(self):
        #create a new editor and save it
        self.gichi = Editor(first_name='gichi', last_name='mu', email='gichimu@email.com')
        self.gichi.save_editor()
        
        #create anew tag and save it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article= Article(title='test',post='this',editor=self.gichi)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2018-09-16'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)