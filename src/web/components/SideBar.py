from playwright.sync_api import Page, expect


class SideBar:
    def __init__(self, page: Page):
        self.page = page

        self.menu = page.locator(".mainnav-menu")
        self.menu_body = page.locator(".mainnav-menu-body")
        self.menu_footer = page.locator(".mainnav-menu-footer")

        self.tests_link = self.menu_body.locator(
            "a[href^='/projects/'][href$='/']"
        )
        self.requirements_link = self.menu_body.locator(
            "a[href$='/requirements']"
        )
        self.runs_link = self.menu_body.locator(
            "a[href$='/runs']"
        )
        self.plans_link = self.menu_body.locator(
            "a[href$='/plans']"
        )
        self.steps_link = self.menu_body.locator(
            "a[href$='/steps']"
        )
        self.pulse_link = self.menu_body.locator(
            "a[href$='/pulse']"
        )
        self.defects_link = self.menu_body.locator(
            "a[href$='/defects']"
        )
        self.analytics_link = self.menu_body.locator(
            "a[href$='/analytics']"
        )
        self.branches_link = self.menu_body.locator(
            "a[href$='/branches']"
        )

        self.settings_link = self.menu_body.locator(
            "a:has(svg.md-icon-cog)"
        )

        self.shortcuts_link = self.menu_footer.locator(
            "a:has(svg.md-icon-apple-keyboard-command)"
        )
        self.help_link = self.menu_footer.locator(
            "a:has(svg.md-icon-help-circle-outline)"
        )
        self.notifications_link = self.menu_footer.locator(
            "a:has(svg.md-icon-bell)"
        )
        self.projects_link = self.menu_footer.locator(
            "a[href='/']"
        )
        self.profile_link = self.menu_footer.locator(
            "a:has(img.rounded-full)"
        )

    def is_loaded(self):
        expect(self.menu).to_be_visible()
        expect(self.menu_body).to_be_visible()
        expect(self.menu_footer).to_be_visible()

        expect(self.tests_link).to_be_visible()
        expect(self.requirements_link).to_be_visible()
        expect(self.runs_link).to_be_visible()
        expect(self.plans_link).to_be_visible()
        expect(self.steps_link).to_be_visible()
        expect(self.defects_link).to_be_visible()

    def click_tests(self):
        self.tests_link.click()

    def click_requirements(self):
        self.requirements_link.click()

    def click_runs(self):
        self.runs_link.click()

    def click_plans(self):
        self.plans_link.click()

    def click_steps(self):
        self.steps_link.click()

    def click_pulse(self):
        self.pulse_link.click()

    def click_defects(self):
        self.defects_link.click()

    def click_analytics(self):
        self.analytics_link.click()

    def click_branches(self):
        self.branches_link.click()

    def click_settings(self):
        self.settings_link.click()

    def click_projects(self):
        self.projects_link.click()

    def click_profile(self):
        self.profile_link.click()