import pytest

# тест на проверку того, что пользователь успешно зашел в личный кабинет (валидные данные)
@pytest.mark.usefixtures('login_personal_account')
class TestPersonalAccount:
    def test_registered_user(self, main_page):
        get_user_name = main_page.get_user_text()
        assert get_user_name == "Karina Карина", "login failed"

