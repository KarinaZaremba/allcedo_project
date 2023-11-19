import pytest


#Проверка на создание черновика (отработка создания шаблона)
@pytest.mark.usefixtures("create_draft")
class TestCreateDraft:
    def test_create_draft(self, main_page, create_lot_page, all_lots_page):
        create_lot_page.click_draft_button()
        all_lots_page.click_all_lots()
        current_page = all_lots_page.get_current_address_page()
        assert current_page == "https://allcedo.ru/account/lots/list/all", f"Страница {current_page} не соответствует условию"








