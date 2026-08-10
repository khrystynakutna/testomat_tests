from faker.proxy import Faker
from playwright.sync_api import Page

from pages.NewProjectsPage import NewProjectsPage
from pages.ProjectPage import ProjectPage


def test_new_project_elements(page:Page, login):
    newProjects = NewProjectsPage(page)
    newProjects.open()
    newProjects.is_loaded()

def test_new_project_creation(page:Page, login):
    newProjects = NewProjectsPage(page)
    newProjects.open()
    newProjects.is_loaded()

    target_project_name = Faker().word()
    newProjects.fill_project_title(target_project_name)
    newProjects.click_create()

    ProjectPage(page).is_loaded()