from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys#ch4
import time#ch5

class NewVisitorTest(unittest.TestCase):
 
   
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)        

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        
        #Alice has heard about a cool new online to-do app. She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'), 
                'Enter a to-do item')


        #She types 'Buy peacock feathers' into a text box (Alice's hobby is tying fly-fishing lures)

        inputbox.send_keys('Buy peacock feathers')

        #When she hits enter, the page updates, and now the page lists
        inputbox.send_keys(Keys.ENTER)
        #"1: Buy peacock feathers" as an item in a to-do list table
        
        time.sleep(10)#ch5

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows), 'New to-do item did not appear in the table'
        )

        #There is still a text box inviting her ta add another item. She enters 'Use peacock feathers to make a fly' (Alice is very methodical)
        self.fail('finish the test!')

        #The page updates again, and now shows both items in her list

        #Alice wonders whether the site will remember her list. Then she sees that the site has generated a unique URL for her -- there is some explanatory text to that effect.

        #She visits that URL - her To-Do list is still there.

        #Satisfied, she goes back to sleep.


if __name__ == '__main__':
    unittest.main()
