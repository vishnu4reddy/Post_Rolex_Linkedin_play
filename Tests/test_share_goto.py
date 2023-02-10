from playwright.sync_api import Page, expect
import time
from Data import imp
Email = imp.username
password = imp.password


def test_share(page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("Rolex")
    page.keyboard.press("Enter")
    page.locator(
        "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']").click()