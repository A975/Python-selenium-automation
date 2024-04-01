#This file includes a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filteration
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List

class BookingFiltration:

    def __init__(self, driver:WebDriver):

        self.driver = driver

    def apply_star_rating(self, *star_values):

        star_filtration_box = self.driver.find_element_by_id('filter_class')
        star_child_elements = star_filtration_box.find_elements_by_css_Selector('*') #Will give us all the elements of this entire webpage
        print(len(star_child_elements))
        
        for star_element in star_child_elements:
            for star_element in star_child_elements:
                if star_element.get_attribute('innerHTML') == f'{star_values} stars':
                    star_element.click()
    
    def sort_price_lowest_first(self):

        search_button = self.driver.find_element_by_css_selector(
            'button[type="submit]'
        )

        search_button.click()
        