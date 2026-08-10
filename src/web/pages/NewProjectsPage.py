from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page


class NewProjectsPage:
    def __init__(self, page ):
        self.page = page
        self.form_container = page.locator("#content-desktop [action='/projects']")

    def open(self):
        self.page.goto("/projects/new")

    def is_loaded(self):
        expect(self.form_container).to_be_visible()
        expect(self.form_container.locator("#classical")).to_be_visible()
        expect(self.form_container.locator("#classical")).to_contain_text("Classical")
        expect(self.form_container.locator("#bdd")).to_be_visible()
        expect(self.form_container.locator("#bdd")).to_contain_text("BDD")
        expect(self.form_container.locator("#project_title")).to_be_visible()
        expect(self.form_container.locator("#demo-btn")).to_be_visible()
        expect(self.form_container.locator("#project-create-btn")).to_be_visible()
        expect(self.page.get_by_text("How to start?")).to_be_visible()
        expect(self.page.get_by_text("New Project")).to_be_visible()

    def fill_project_title(self, target_project_name:str):
        self.form_container.locator("#project_title").fill(target_project_name)

    def click_create(self):
        self.form_container.locator("#project-create-btn input").click()
        expect(self.form_container.locator("#project_create-btn input")).to_be_hidden(timeout=10000)

