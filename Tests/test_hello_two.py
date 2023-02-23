class GoogleSearchPage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.get_by_role("combobox", name="Search")
        self.first_result = page.locator(
            "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']")

    def navigate(self):
        self.page.goto("https://www.google.com/")

    def search(self, query):
        self.search_box.click()
        self.search_box.fill(query)
        self.page.keyboard.press("Enter")

    def click_first_result(self):
        self.first_result.click()


class LinkedInLoginPage:
    def __init__(self, page):
        self.page = page
        self.email_field = page.get_by_label("Email or Phone")
        self.password_field = page.get_by_label("Password")
        self.sign_in_button = page.locator(
            "#organic-div form").get_by_role("button", name="Sign in")
        self.share_post_button = page.get_by_role(
            "button", name="Share in a post")
        self.continue_to_linkedin_button = page.get_by_role(
            "link", name="Continue to LinkedIn")
        self.my_network_button = page.get_by_role(
            "button", name="vishnu vardhan reddy usirike Me")
        self.sign_out_button = page.get_by_role("link", name="Sign Out")

    def login(self, email, password): 
        self.email_field.click()
        self.email_field.fill(email)
        self.password_field.click()
        self.password_field.fill(password)
        self.sign_in_button.click()

    def share_post(self):
        self.share_post_button.click()

    def continue_to_linkedin(self):
        with self.page.expect_popup() as page_info:
            self.continue_to_linkedin_button.click()
        return page_info.value

    def go_to_my_network(self):
        self.my_network_button.click()

    def sign_out(self):
        self.sign_out_button.click()


GoogleSearchPage()
LinkedInLoginPage()
