from Lib.Share import Share_linkedin
from playwright.sync_api import Page
from Data import config
Email = config.user_git
password = config.git_pass

# Email = imp.username
# password = imp.password
# number = config.number


def test_share(page: Page):
    share_page = Share_linkedin(page)
    share_page.navigate()
    # share_page.Login(Email, password)
    # share_page.main()

    Share_linkedin(page)

    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     context = browser.new_context(record_video_dir="record_videos/")
    #     record_video_size = {"width": 640, "height": 480}
    #     page = context.new_page()
    # page.goto("https://www.google.com/")
    # page.get_by_role("combobox", name="Search").click()
    # page.get_by_role("combobox", name="Search").fill("Rolex")  # Search
    # page.keyboard.press("Enter")  # click
    # page.locator(
    #     "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']").click()  # navigater
    # with page.expect_popup() as page1_info:
    #     page.get_by_role(
    #         "button", name="Share this page on Linkedin New tab").click()  # login
    # page1 = page1_info.value
    # # page1.screenshot(path="screenshot.png", full_page=True)
    # page1.get_by_label("Email or Phone").click()  # email click
    # page1.get_by_label("Email or Phone").fill(number)  # fill Email
    # page1.get_by_label("Password").click()  # click pass
    # page1.get_by_label("Password").fill(password)  # fill pass
    # # page1.screenshot(path="screenshot.png", full_page=True)
    # page1.locator("#organic-div form").get_by_role("button",
    #                                                name="Sign in").click()  # click sign in
    # # click share post
    # page1.get_by_role("button", name="Share in a post").click()
    # page1.locator('//*[@id="ember52"]').click()  # one
    # page1.screenshot(path="screenshot.png", full_page=True)  # two
    # with page1.expect_popup() as page2_info:
    #     page1.get_by_role("link", name="Continue to LinkedIn").click()  # three
    # page2 = page2_info.value
    # page2.get_by_role(
    #     "button", name="vishnu vardhan reddy usirike Me").click()  # four
    # page2.screenshot(path="screenshot.png", full_page=True)
    # page2.get_by_role("link", name="Sign Out").click()  # five
    # # context.close()
