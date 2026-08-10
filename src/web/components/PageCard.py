from enum import Enum
from typing import TYPE_CHECKING

from playwright.sync_api import Locator, expect

if TYPE_CHECKING:
    pass

class PageCard:
    def __init__(self, card: Locator):
        self.page = card
        self._link = card
       # self._link = card.locator('a')
        self._title = card.locator('h3.text-gray-700')
        self._test_count = card.locator('p.text-gray-500.text-sm')
        self._avatars = card.locator('img.rounded-full')
        self._badges = card.locator('.project-badges')

    @property
    def title(self) -> str:
        return self._title.text_content().strip()

    @property
    def test_count(self) -> str:
        return self._test_count.text_content().strip()

    @property
    def href(self) -> str:
        return self._link.get_attribute("href")

    def title_has(self, expected_title: str):
        expect(self._title).to_have_text(expected_title)

    def test_count_has(self, expected_count: str):
        expect(self._test_count).to_have_text(expected_count)

    def badges_has(self, expected_badge: Badges):
        expect(self._badges).to_contain_text(expected_badge.value)

    def click(self):
        self._link.click()

class Badges(Enum):
    CLASSICAL = "Classical"
