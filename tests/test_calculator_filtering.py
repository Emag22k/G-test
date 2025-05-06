import allure
import time
from pytest import fixture
from playwright.sync_api import sync_playwright
from pages.calculator import CalculatorPage
import os

BASE_URL = os.getenv("BASE_URL", "https://gcore.com")

@allure.feature("Server calculator")
@allure.story("Filtering servers by price")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_filters(page):
    calculator = CalculatorPage(page, BASE_URL, "/hosting")
    calculator.open()
    calculator.wait(2000)

    calculator.select_dedicated_servers()
    assert calculator.locators["dedicated_radio"].is_checked(), "Dedicated radio button is not checked"

    calculator.select_currency("USD")
    assert calculator.locators["usd_radio"].is_checked(), "USD radio button is not checked"

    calculator.click_price_filter()
    calculator.set_price_range("83", "100")
    calculator.wait(5000)

    # Check if filtered servers appear
    elements = calculator.page.locator("gcore-cards-list gcore-price-card")
    count = len(elements.all())
    print(f"Найдено серверов: {count}")


    assert count > 0, f"Ожидалось результатов больше 0, но найдено {count}"

    calculator.take_screenshot("filtered_servers.png")

    time.sleep(5)

@fixture
def page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, args=["--incognito"])
        page = browser.new_page()
        yield page
        browser.close()
