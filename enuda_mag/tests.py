from django.urls import resolve
from django.test import TestCase
from enuda_mag import views
from enuda_mag import models
from django.core.files.uploadedfile import SimpleUploadedFile


def create_test_blog_post():
    first_blog_post = models.BlogPost()
    first_blog_post.title = "Director Charles Martin Smith tells us the \
                             inside story of the canine masterpiece"
    first_blog_post.subtitle = "The case has come to define more about who \
                                we were as Americans at the dawn of the \
                                21st century—and how ugly we are."
    first_blog_post.content = 'The first (ever) list blog post'
    first_blog_post.save()
    return first_blog_post


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'enuda_mag/index.html')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8').strip()

        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'enuda_mag/index.html')


class PostDetailPageTest(TestCase):

    def test_uses_post_detail_template(self):
        create_test_blog_post()
        response = self.client.get('/post_detail/')
        # import pdb; pdb.set_trace();
        self.assertTemplateUsed(response, 'enuda_mag/post_detail.html')

    def test_post_detail_url_resolves_to_post_view(self):
        found = resolve('/post_detail/')
        self.assertEqual(found.func, views.post_detail)


class UserModelTest(TestCase):

    def test_saving_and_retrieving_users(self):
        user = models.User()
        user.username = "Uche&Hf32jH"
        user.first_name = "Uche"
        user.last_name = "Anya"
        user.save()


class BlogPostModelTest(TestCase):

    def test_saving_and_retrieving_blog_posts(self):
        first_blog_post = models.BlogPost()
        first_blog_post.title = "Director Charles Martin Smith tells us the \
                                 inside story of the canine masterpiece"
        first_blog_post.subtitle = "The case has come to define more about who \
                                    we were as Americans at the dawn of the \
                                    21st century—and how ugly we are."
        first_blog_post.content = 'The first (ever) blog post'
        first_blog_post.save()

        # Making and Saving Image
        test_image = models.Image()
        path = "enuda_mag/static/enuda_mag/img/enudahouselogo3.jpeg"
        test_image.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg')
        test_image.save()
        first_blog_post.image = test_image
        first_blog_post.save()

        # Making Second Blog Post
        second_blog_post = models.BlogPost()
        second_blog_post.content = 'Blog Post the second'
        second_blog_post.save()

        # Making and Saving Second Image
        second_test_image = models.Image()
        path = "enuda_mag/static/enuda_mag/img/enudahouselogo3.jpeg"
        second_test_image.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg')
        second_test_image.save()
        second_blog_post.image = second_test_image
        second_blog_post.save()

        # Tesing Only 2 Blog Posts
        saved_blog_posts = models.BlogPost.objects.all()
        self.assertEqual(saved_blog_posts.count(), 2)

        # Tesing Only 2 Images
        saved_images = models.Image.objects.all()
        self.assertEqual(saved_images.count(), 2)

        first_saved_blog_post = saved_blog_posts[0]
        second_saved_blog_post = saved_blog_posts[1]
        self.assertIn(
            '/home/kalu/Documents/enuda_house_world/media/images/',
            test_image.image.path)
        self.assertEqual(first_saved_blog_post.content,
                         'The first (ever) list blog post')
        self.assertEqual(second_saved_blog_post.content,
                         'Blog Post the second')
