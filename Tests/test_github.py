from playwright.sync_api import Page, expect
import time
from Data import imp, config
Email = config.user_git
password = config.git_pass
number = config.number


def test_share(page: Page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("github")
    page.keyboard.press("Enter")
    page.locator("//a[normalize-space()='+.Git Hub Login']").click()
    page.locator("//input[@id='login_field']").click()
    page.locator("//input[@id='login_field']").fill(Email)
    page.keyboard.press("Tab")
    page.keyboard.type(password)
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    page.get_by_role("link", name="Sign in").click()
    page.locator(
        "//form[@action='/dashboard/ajax_my_repositories?location=left']//button[@name='button'][normalize-space()='Show more']").click()
    page.locator(
        "//ul[2]//li[1]//div[1]//div[1]//a[1]").click()
    page.get_by_role("link", name="Tests").click()
    page.get_by_role("link", name="test_Share.py").click()
    page.locator("//remote-clipboard-copy[@class='d-inline-block btn-octicon']").click()
    # page.locator("")

    time.sleep(10)
