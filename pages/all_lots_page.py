from pages.base_page import BasePage


class AllLotsPage(BasePage):
    CURRENT_URL_LOCATOR = "https://allcedo.ru/account/lots/list"
    ALL_LOTS = "//div[@class = 'page__tabs']/a[1]"
    FIRST_LOT_LOCATOR = "//div[@class='lot-list-wrap--line lot-list-wrap lot-list-wrap--3 relative-position']/div[1]/div[3]//div[7]/a"

    def get_current_address_page(self):
        url_is = self.get_current_url()
        return str(url_is)

    def click_all_lots(self):
        self.click(self.ALL_LOTS)

    def click_on_the_first_object(self):
        self.click(self.FIRST_LOT_LOCATOR)


