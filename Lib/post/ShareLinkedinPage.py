from Lib.post.LinkedinLoginPage import LinkedinLoginPage
from Lib.post.LinkedinSharePage import LinkedinSharePage
from Lib.post.HomePage import HomePage


class ShareLinkedin:
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
