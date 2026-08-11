from faker.proxy import Faker
from playwright.sync_api import Page

from components import SideBar
from pages.NewProjectsPage import NewProjectsPage
from pages.ProjectPage import ProjectPage


def test_new_project_elements(page:Page, login):
    newProjects = NewProjectsPage(page)
    newProjects.open()
    newProjects.is_loaded()
