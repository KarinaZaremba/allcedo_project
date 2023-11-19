import pytest
import time

# Тест на проверку публикации лота (после создания черновика)
@pytest.mark.usefixtures("create_lot")
class TestCreateLot:
    def test_create_lot(self, create_lot_page, all_lots_page):
        all_lots_page.click_on_the_first_object()
        create_lot_page.scroll_down()
        create_lot_page.input_geo_position()
        create_lot_page.click_release_button()
        title = create_lot_page.get_title_lot()

        assert title == "Лот успешно создан", "Лот не создан, перепроверьте настройки"