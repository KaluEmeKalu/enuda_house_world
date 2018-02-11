from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id(
            'cs-primary-nav')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

    def test_can_i_log_in(self):
        # Eke has heard about a cool new Magazine. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Enuda House
        self.assertIn('Divit', self.browser.title)
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
