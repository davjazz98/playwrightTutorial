from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.facebook.com/")
    page.get_by_role("textbox", name="Email or mobile number").fill("barev dzez", timeout=1000000000)
    page.get_by_role("textbox", name="Email or mobile number").press("Tab")
    page.get_by_role("textbox", name="Password").fill("sxalmxalparol", timeout=3000)
    page.get_by_role("button", name="Log In").click()

    # page.pause()
    # ---------------------
    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)

    # playwright = sync_playwright().start()
    # run(playwright)