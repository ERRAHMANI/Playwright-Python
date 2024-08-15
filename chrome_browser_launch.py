from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.google.com')

    print('chrome successfully opened')
    print(page.title())
    page.get_by_role("combobox").fill("younes")
    #page.get_by_role("submit", name="btnK").click()
    #page.get_by_role("button", name="Sign in").click()
    page.locator("xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
    page.wait_for_timeout(8000)
    expect(page.get_by_role("main")).to_contain_text("younes")
    browser.close()