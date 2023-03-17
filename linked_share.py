class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.get_by_role("combobox", name="Search")
        self.rolex_link = page.locator(
            "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']")

    def search_for(self, query):
        self.search_box.fill(query)
        self.search_box.press("Enter")

    def click_rolex_link(self):
        self.rolex_link.click()


class LinkedinLoginPage:
    def __init__(self, page):
        self.page = page
        self.email_field = page.get_by_label("Email or Phone")
        self.password_field = page.get_by_label("Password")
        self.sign_in_button = page.locator(
            "#organic-div form").get_by_role("button", name="Sign in")
        self.share_post_button = page.get_by_role(
            "button", name="Share in a post")

    def login(self, email, password):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.sign_in_button.click()


class LinkedinSharePage:
    def __init__(self, page):
        self.page = page
        self.continue_link = page.get_by_role(
            "link", name="Continue to LinkedIn")
        self.post_button = page.get_by_role(
            "button", name="vishnu vardhan reddy usirike Me")
        self.sign_out_link = page.get_by_role("link", name="Sign Out")

    def click_continue_link(self):
        self.continue_link.click()

    def share_post(self):
        self.post_button.click()

    def sign_out(self):
        self.sign_out_link.click()


class ShareLinkedinPage:
    def __init__(self, page):
        self.home_page = HomePage(page)
        self.login_page = None
        self.share_page = None

    def go_to_home_page(self):
        self.home_page.page.goto("https://www.linkedin.com/")

    def share_on_linkedin(self, query, email, password):
        self.home_page.search_for(query)
        self.home_page.click_rolex_link()

        self.login_page = LinkedinLoginPage(self.home_page.page.expect_popup())
        self.login_page.login(email, password)

        self.share_page = LinkedinSharePage(
            self.login_page.page.expect_popup())
        self.share_page.click_continue_link()
        self.share_page.share_post()
        self.share_page.sign_out()
