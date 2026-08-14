
from playwright.sync_api import Page

from src.web.components.PageCard import PageCard, Badges
from src.web.pages.ProjectsPage import ProjectsPage


def test_project_card(page: Page, login):

    projects_page = ProjectsPage(page)

    projects_page.is_loaded()

    project = projects_page.get_project_card("python manufacture")

    project.title_has("python manufacture")
    project.test_count_has("0 tests")
    project.badges_has(Badges.CLASSICAL)