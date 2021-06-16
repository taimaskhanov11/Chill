import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True
# assert opts.headless  # без графического интерфейса.

browser = Firefox(options=opts,executable_path=r'C:\Users\taima\PycharmProjects\Chill\geckodriver.exe')
browser.get('https://bandcamp.com')
print(browser.find_element_by_class_name('play-btn'))
browser.find_element_by_class_name('play-btn').click()

time.sleep(2)
# quit()
browser.close()
browser.quit()

