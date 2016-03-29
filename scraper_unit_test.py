import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Scraper(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.COUNTRIES = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk')
        self.assertIn("O2", driver.title)
        input_form = driver.find_element_by_xpath('//*[@id="countryName"]')
        for country in self.COUNTRIES:
            self.print_cost(driver, country, input_form)

    def print_cost(self, driver, country, input_form):

        input_form.send_keys(country, Keys.RETURN)
        assert "No results found." not in driver.page_source
        tariff_plan = driver.find_element_by_xpath('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')
        print("%s: %s" % (country, tariff_plan.get_attribute('innerHTML')))
        input_form.clear()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()