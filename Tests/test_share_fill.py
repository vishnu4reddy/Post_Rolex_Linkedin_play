
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
    with page.expect_popup() as page1_info:
        page.get_by_role(
            "button", name="Share this page on Linkedin New tab").click()
    page1 = page1_info.value
    page1.get_by_label("Email or Phone").click()
    page1.get_by_label("Email or Phone").fill("9490058514")
    page1.get_by_label("Password").click()
    page1.get_by_label("Password").fill("vishnu161999")
