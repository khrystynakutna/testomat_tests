from playwright.sync_api import expect

from components.PageCard import PageCard


class ProjectsPage:

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        expect(self.page.locator(".common-flash-success")).to_be_visible()
        expect(self.page.locator(".common-flash-success")).to_have_text("Signed in successfully")
        expect(self.page.locator(".common-flash-success", has_text="Signed in successfully")).to_be_visible()

    def get_project_card(self, project_name: str) -> PageCard:
        card = self.page.locator("a").filter(has=self.page.locator("h3.text-gray-700",has_text=project_name))

        return PageCard(card)