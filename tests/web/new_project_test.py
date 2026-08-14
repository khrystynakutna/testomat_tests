from faker.proxy import Faker
from playwright.sync_api import Page

from src.web.components import SideBar
from src.web.pages.NewProjectsPage import NewProjectsPage
from src.web.pages.ProjectPage import ProjectPage


def test_new_project_elements(page:Page, login):
    newProjects = NewProjectsPage(page)
    newProjects.open()
    newProjects.is_loaded()
