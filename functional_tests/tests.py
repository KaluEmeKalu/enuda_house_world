from selenium import webdriver
import unittest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the thumbnails on bottom right are small (80px)
        inputbox = self.browser.find_element_by_id('test-cs-post-thumb')
        self.assertAlmostEqual(
            inputbox.size['width'],
            80,
            delta=10
        )

    def test_i_can_make_a_new_post(self):
        import pdb; pdb.set_trace()
        # Edith goes to the home page
        url = self.live_server_url + "/post_create"
        self.browser.get(url)

        # She notices write some contents and clicks save
        post = self.browser.find_element_by_class_name('cs-post-meta')
        post = post.find_element_by_tag_name('a')
        url = post.get_property('href')
        self.assertIn('post_detail', url)
        post.click()
        time.sleep(3)
        comments = self.browser.find_element_by_css_selector(
            '.comment-notes').text
        self.assertIn("Your email address will not be published.", comments)


    def test_can_i_click_post(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)

        # She notices the a post and clicks)
        # import pdb; pdb.set_trace()
        post = self.browser.find_element_by_class_name('cs-post-meta')
        post = post.find_element_by_tag_name('a')
        url = post.get_property('href')
        self.assertIn('post_detail', url)
        post.click()
        time.sleep(3)
        comments = self.browser.find_element_by_css_selector(
            '.comment-notes').text
        self.assertIn("Your email address will not be published.", comments)


    def test_can_i_log_in(self):
        # Eke has heard about a cool new Magazine. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Enuda House
        self.assertIn('Enuda House', self.browser.title)
        self.fail('Finish the test!')

        # She also notices that there is a play to login/register
        # ASSERT LOGIN & REGISTER


        # WHen Eke clicks on register he is taken to the register
        # page


        # After he is logged in and redirected to the homepage

        # Now she sees her information, and a whoel bunch of articles


        # She notices the footer has a place called "Be A Contributor"



        # After clicking on the linkthe page and is asked to be a contributor. 


        # This shows her 


if __name__ == '__main__':
    unittest.main(warnings='ignore')
