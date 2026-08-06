from playwright.sync_api import Page, expect


def login_with_invalid_creds(page: Page):
    page.goto('https://testomat.io/')
    expect(page).to_have_title("AI Test Management Tool | Testomat.io")
    expect(page.get_by_text("Log in", exact=True)).to_be_visible()
    page.get_by_text("Log in", exact=True).click()
    page.locator("#content-desktop #user_email").fill("khrystynakutna.fa@gmail.com")
    page.locator("#content-desktop #user_password").fill("k638Ln!r!2QucYе")
    page.get_by_role("button", name="Sign In").click()
    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid email or password.")