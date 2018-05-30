from django.test import TestCase

# Create your tests here.
import datetime
from django.utils.timezone import utc


class FrontEndTestCase(TestCase):
    fixtures = ['myapp/myblog_test_fixture.json',]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
 
        for count in range(1, 11):
            post = Post(title="Test Post %d Title" % count,
                text="foo", author=author)

            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate

            post.save()

    def test_list_only_published(self):
        resp = self.client.get('/')

        for count in range(1, 11):
            title = "Test Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)
