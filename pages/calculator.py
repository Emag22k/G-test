from pages.base_page import BasePage
from playwright.sync_api import Page
import allure

class CalculatorPage(BasePage):
    def __init__(self, page: Page, base_url: str, path: str):
        super().__init__(page, base_url)
        self.path = path
        self.locators = {
            "dedicated_radio": page.locator('input.gc-switch-button-input[value="dedicated"]'),
            "usd_radio": page.locator('input[type="radio"][value="USD"]')
        }

    @allure.step("Select 'Dedicated servers' radio button")
    def select_dedicated_servers(self):
        self.locators["dedicated_radio"].click()

    @allure.step("Select currency {currency}")
    def select_currency(self, currency: str):
        currency_locator = self.page.locator(f'input[type="radio"][value="{currency}"]')
        currency_locator.click()

    @allure.step("Click price filter")
    def click_price_filter(self):
        button = self.page.locator('button >> text=Price')
        button.click()

    @allure.step("Set price range from {min_price} to {max_price}")
    def set_price_range(self, min_price: str, max_price: str):
        min_input = self.page.locator('input.gc-input[type="number"]').nth(0)
        max_input = self.page.locator('input.gc-input[type="number"]').nth(1)

        min_input.click()
        min_input.press("Control+A")
        min_input.press("Delete")
        min_input.type(min_price, delay=100)
        min_input.press("Enter")

        max_input.click()
        max_input.press("Control+A")
        max_input.press("Delete")
        max_input.type(max_price, delay=100)
        max_input.press("Enter")
