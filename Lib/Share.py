class Share_linkedin():
    def __init__(self, page):
        self.page = page
        self.start = page.get_by_role("combobox", name="Search")
        self.start_one = page.get_by_role(
            "combobox", name="Search")  # Search
        self.start_two = page.keyboard
        self.click = page.locator(
            "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']")  # click
        with page.expect_popup() as page1_info:
            self.login = page.get_by_role(
                "button", name="Share this page on Linkedin New tab")
        page1 = page1_info.value
        self.click_username = page1.get_by_label("Email or Phone")
        self.fill_username = page1.get_by_label("Email or Phone")
        self.click_password = page1.get_by_label("Password")
        self.fill_password = page1.get_by_label("Password")
        self.sign_in = page1.locator("#organic-div form").get_by_role("button",
                                                                      name="Sign in")
    #     self.share_post = page1.get_by_role(
    #         "button", name="Share in a post")
    #     self.one = page1.locator('//*[@id="ember52"]')
    #     with page1.expect_popup() as page2_info:
    #         self.two = page1.get_by_role(
    #             "link", name="Continue to LinkedIn")
    #         page2 = page2_info.value
    #         self.three = page2.get_by_role(
    #             "button", name="vishnu vardhan reddy usirike Me")
    #         self.four = page2.get_by_role("link", name="Sign Out")

    def navigate(self):
        self.page.goto("https://www.google.com/")
        self.start.click()
        self.start_one.fill("Rolex")
        self.start_two.press("Enter")
        self.click.click()

    def Login(self, Email, password):
        self.login.click()
        self.fill_username.fill(Email)
        self.fill_password.fill(password)
        self.sign_in.click()

    # def main(self):
    #     self.share_post.click()
    #     self.one.click()
    #     self.two.click()
    #     self.three.click()
    #     self.four.click()
