from playwright.sync_api import Page
import time
from Data import config
Email = config.user_git
password = config.git_pass
number = config.number


def github(page: Page):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     context = browser.new_context(
    #         record_video_dir="./record_videos/",
    #         record_video_size={"width": 640, "height": 480}
    #     )
    #     page = context.new_page()
    print("Starting On Earth")
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("github")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshot1.png", full_page=True)
    page.locator("//a[normalize-space()='+.Git Hub Login']").click()
    page.locator("//input[@id='login_field']").click()
    page.locator("//input[@id='login_field']").fill(Email)
    page.keyboard.press("Tab")
    page.keyboard.type(password)
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshot2.png", full_page=True)
    page.get_by_role("link", name="Sign in").click()
    page.locator(
        "//form[@action='/dashboard/ajax_my_repositories?location=left']//button[@name='button'][normalize-space()='Show more']").click()
    page.locator(
        "//ul[2]//li[1]//div[1]//div[1]//a[1]").click()
    page.get_by_role("link", name="Tests").click()
    page.get_by_role("link", name="test_Share.py").click()
    page.locator(
        "//remote-clipboard-copy[@class='d-inline-block btn-octicon']").click()
    page.screenshot(path="screenshot3.png", full_page=True)
    page.get_by_role("link", name="Codespaces").click()
    page.get_by_role("button", name="Codespace configuration").click()
    page.locator(
        "//button[@data-action='click:options-popover#showEditors']").click()
    page.screenshot(path="screenshot4.png", full_page=True)
    for i in range(2):
        page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    # page.get_by_role("menuitem", name="Open in browser")
    # page.get_by_label("Open visual Studio Code").click()
    print("I Am In V.S.Code")
    page.locator(
        "//div[@title='/workspaces/Post_Rolex_Linkedin_play/Tests • Contains emphasized items']//div[@class='monaco-icon-label-container']").click()
    page.locator("div[class='monaco-icon-label file-icon tests-name-dir-icon test_sample.py-name-file-icon name-file-icon py-ext-file-icon ext-file-icon python-lang-file-icon explorer-item monaco-decoration-itemColor--ec98p9 monaco-decoration-itemBadge--ec98p9 monaco-decoration-iconBadge--ec98p9'] div[class='monaco-icon-label-container']").click()
    page.locator(
        "//div[@class='view-lines monaco-mouse-cursor-text']").click()
    page.keyboard.press("Control+A")
    page.screenshot(path="screenshot5.png", full_page=True)
    page.keyboard.press("Backspace")
    page.screenshot(path="screenshot6.png", full_page=True)
    page.keyboard.press("Control+V")
    page.screenshot(path="screenshot7.png", full_page=True)
    page.locator("//canvas[@class='xterm-cursor-layer']").click()
    print("I Am In Terminal")
    page.screenshot(path="screenshot8.png", full_page=True)
    page.keyboard.type("clear", delay=10)
    page.screenshot(path="screenshot9.png", full_page=True)
    page.keyboard.press("Enter")
    page.keyboard.type("pip install pytest", delay=10)
    page.keyboard.press("Enter")
    page.screenshot(path="screenshot10.png", full_page=True)
    # page.locator("//div[contains(@class,'editor-container')]//div[5]//div[19]").click()
    # page.wait_for_selector("//div[contains(@class,'editor-container')]//div[5]//div[19]")
    print("landed On Moon")
    time.sleep(20)
    page.close()
    # context.close()
