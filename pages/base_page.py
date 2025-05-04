import allure
from playwright.sync_api import Page
from os import getenv


class BasePage:
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url if base_url != "" else getenv("BASE_URL", "")
        self.path = ""

    def open(self):
        self.page.goto(self.base_url + self.path)

    def get_title(self) -> str:
        return self.page.title()

    def current_url(self) -> str:
        return self.page.url

    def reload(self):
        self.page.reload()

    def wait(self, ms: int):
        self.page.wait_for_timeout(ms)

    @allure.step("Take screenshot")
    def take_screenshot(self, path="screenshot.png"):
        self.page.screenshot(path=path)
        allure.attach.file(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
