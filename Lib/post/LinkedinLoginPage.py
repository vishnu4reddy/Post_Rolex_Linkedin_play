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
