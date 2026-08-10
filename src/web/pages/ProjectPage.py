from playwright.sync_api import Page, expect


class ProjectPage:
    def __init__(self, page:Page):
        self.page = page

    def is_loaded(self):
        #expect(self.page.locator(".sticky-header")).to_be_visible()
        #expect(self.page.locator(".mainnav-menu")).to_be_visible()
        #expect(self.page.locator("[placeholder='First Suite']")).to_be_visible()
        #expect(self.page.get_by_role("button", name="Suite")).to_be_visible()
        #expect(self.page.locator(".detail-view-content")).to_contain_text("Welcome to Testomat.io")
        expect(self.page.locator(".detail-view-content")).to_be_visible()
