from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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

        # Now he sees his information, and a whoel bunch of articles


        # He notices the footer has a place called "Be A Contributor"



        # After clicking on the linkthe page and is asked to be a contributor. 


        # This shows her 


if __name__ == '__main__':
    unittest.main(warnings='ignore')
