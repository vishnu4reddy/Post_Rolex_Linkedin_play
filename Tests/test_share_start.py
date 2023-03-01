from playwright.sync_api import Page
from Data import imp
Email = imp.username
password = imp.password


def test_share(page: Page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("Rolex")
    page.keyboard.press("Enter")
