import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.all_lots_page import AllLotsPage
from pages.create_lot_page import CreateLot
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def login_personal_account(chromedriver, main_page):
    main_page.user_steps_main_page()

    yield
    chromedriver.quit()


@pytest.fixture
def create_draft(chromedriver, main_page, create_lot_page):
    main_page.user_steps_main_page()
    main_page.create_lot_button()
    create_lot_page.steps_create_lot()

    yield
    chromedriver.quit()


@pytest.fixture
def create_lot(chromedriver, main_page, create_lot_page, all_lots_page):
    main_page.user_steps_main_page()
    main_page.create_lot_button()
    create_lot_page.steps_create_lot()
    create_lot_page.click_draft_button()
    all_lots_page.click_all_lots()

    yield
    chromedriver.quit()


@pytest.fixture
def chromedriver():
    s = Service('C:\\Users\\rem6o\\Desktop\\Python\\chromedriver\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    return driver


@pytest.fixture
def main_page(chromedriver):
    return MainPage(chromedriver)


@pytest.fixture
def create_lot_page(chromedriver):
    return CreateLot(chromedriver)


@pytest.fixture()
def all_lots_page(chromedriver):
    return AllLotsPage(chromedriver)