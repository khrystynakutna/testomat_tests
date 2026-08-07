from playwright.sync_api import Page, expect


def test_login_with_invalid_creds(page: Page):
    page.goto('https://testomat.io/')
    expect(page).to_have_title("AI Test Management Tool | Testomat.io")
    expect(page.get_by_text("Log in", exact=True)).to_be_visible()
    page.get_by_text("Log in", exact=True).click()

    login_user(page, email="khrystynakutna.fa@gmail.com", password="kfghjjk")

    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid email or password.")

def test_search_project(page: Page):
    page.goto('https://testomat.io/')
    page.get_by_text("Log in", exact=True).click()

    login_user(page, email="khrystynakutna.fa@gmail.com", password="k638Ln!r!2QucYT")

    target_project = "python manufacture"
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)

    expect(page.get_by_role("heading", name=target_project)).to_be_visible()
    expect(page.locator("ul li h3", has_text=target_project)).to_be_visible()
    expect(page.locator(selector="ul li h3").filter(has_text=target_project)).to_be_visible()

def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign In").click()
