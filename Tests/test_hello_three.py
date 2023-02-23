from Tests.test_hello_two import GoogleSearchPage, LinkedInLoginPage
from Data import config
from playwright.sync_api import sync_playwright
number = config.number
password = config.password
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    google_search_page = GoogleSearchPage(page)
    google_search_page.navigate()
    google_search_page.search("Rolex")
    google_search_page.click_first_result()

    linkedin_login_page = LinkedInLoginPage(page)
    page1 = page
    linkedin_login_page.login(number, password)
    linkedin_login_page.share_post()
    page2 = linkedin_login_page.continue_to_linkedin()
    page2 = LinkedInMyNetworkPage(page2)
    page2.go_to_my_network()
    page2.my_network_page_screenshot()
    page2.sign_out()
    browser.close()
