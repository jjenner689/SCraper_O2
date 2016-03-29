from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


COUNTRIES = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']


def print_cost(driver, country, input_form):

    input_form.send_keys(country, Keys.RETURN)
    tariff_plan = driver.find_element_by_xpath('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')
    print("%s: %s" % (country, tariff_plan.get_attribute('innerHTML')))
    input_form.clear()

def main():

    driver = webdriver.Firefox()
    driver.get('http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk')
    input_form = driver.find_element_by_xpath('//*[@id="countryName"]')
    for country in COUNTRIES:
        print_cost(driver, country, input_form)
    driver.close()


if __name__ == '__main__':
    main()