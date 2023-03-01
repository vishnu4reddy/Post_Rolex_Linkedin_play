# from playwright.sync_api import Page


# class LoginPage:
#     def __init__(self, page: Page):
#         self.page = page

#     def navigate(self):   
#         self.page.goto("https://github.com/login")

#     def login(self, username: str, password: str):
#         self.page.locator('//*[@id="login_field"]').fill(username)
#         self.page.locator('//*[@id="password"]').fill(password)
#         self.page.locator("//input[@name='commit']").click()

#     def select_repository(self, repository_name: str):
#         self.page.locator(
#             "(//button[@name='button'][normalize-space()='Show more'])[1]").click()
#         self.page.locator(
#             f"//ul[2]//li[4]//div[1]//div[1]//a[contains(text(), '{repository_name}')]").click()

#     def open_test_file(self, file_name: str):
#         self.page.get_by_role("link", name="Tests").click()
#         self.page.locator(f"//a[normalize-space()='{file_name}']").click()
#         self.page.locator(
#             "//remote-clipboard-copy[@class='d-inline-block btn-octicon']").click()

#     def open_codespace(self):
#         self.page.get_by_role("link", name="Codespaces").click()
#         self.page.get_by_role("button", name="Codespace configuration").click()
#         self.page.locator(
#             "//button[@data-action='click:options-popover#showEditors']").click()
#         self.page.locator(
#             "//span[normalize-space()='Open in browser']").click()

#     def select_codespace_file(self, folder_name: str, file_name: str):
#         self.page.locator(f"//span[contains(text(),'{folder_name}')]").click()
#         self.page.locator(f"//span[contains(text(),'{file_name}')]").click()
#         self.page.locator(
#             "//div[@class='view-lines monaco-mouse-cursor-text']").click()

#     def run_terminal_command(self, command: str):
#         self.page.locator("//canvas[@class='xterm-cursor-layer']").click()
#         self.page.keyboard.type(command, delay=10)
#         self.page.keyboard.press("Enter")
