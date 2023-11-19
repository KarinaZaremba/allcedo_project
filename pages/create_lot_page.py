from pages.base_page import BasePage


class CreateLot(BasePage):

    INPUT_NAME_LOCATOR = "//input[@id = 'name']"
    INPUT_SEARCH_CATEGORY = "//input[@id = 'searchCategory']"
    CHOOSE_CATEGORY = "//div[@class = 'searchCategory-item']"
    PRICE_LOCATOR = "//button[@class = 'btn btn_primary btn_normal btn_bold createLot-form-price__button']"
    MY_PRICE_LOCATOR = "//span[text()='Хочу свои']"
    MIN_PRICE_LOCATOR = "//input[@id='createLotPriceModal-enterPrice-min']"
    MAX_PRICE_LOCATOR = "//input[@id='createLotPriceModal-enterPrice-max']"
    AGREE_BUTTON = "//span[text()='Согласен']"
    TRADING_DATE_LOCATOR = "//input[@id='trading-date']"
    DESCRIPTION_LOCATOR = "//textarea[@id='description']"
    FILE_UPLOAD_LOCATOR = "//input[@id='file-upload']"
    GEO_LOCATOR = "//input[@id='suggest']"
    CORRECT_ADDRESS_LOCATOR = "//div[@class='location-geocoder-select']/div[1]"
    RELEASE_LOT_BUTTON_LOCATOR = "//span[text()='Опубликовать']"
    DRAFT_BUTTON_LOCATOR = "//div[@class = 'createLot-actions']/button[2]"
    PICTURE_LOCATOR = "C:\\Users\\rem6o\\Desktop\\allcedo project\\adidas.png"
    TITLE_POP_UP_LOCATOR = "//div[@class='share__title']"
    ALL_LOTS = "https://allcedo.ru/account/lots/list"

    def input_product_name(self):
        self.send_text(self.INPUT_NAME_LOCATOR, "Adidas")

    def input_search_category(self):
        self.send_text(self.INPUT_SEARCH_CATEGORY, "кроссовки")
        self.click(self.CHOOSE_CATEGORY)

    def click_price(self):
        self.click(self.PRICE_LOCATOR)
    def input_price(self):
        self.click(self.MY_PRICE_LOCATOR)
        self.send_text(self.MAX_PRICE_LOCATOR, "15000")
        self.send_text(self.MIN_PRICE_LOCATOR, "9000")
        self.click(self.AGREE_BUTTON)

    def input_date(self):
        self.clear(self.TRADING_DATE_LOCATOR)
        self.send_text(self.TRADING_DATE_LOCATOR, "2")

    def input_products_description(self):
        self.send_text(self.DESCRIPTION_LOCATOR, "Новые, оригинал. 37 размер")

    def upload_products_photo(self):
        self.for_upload(self.FILE_UPLOAD_LOCATOR)

    def input_geo_position(self):
        self.for_geo(self.GEO_LOCATOR, "Москвa, Тверская")
        self.click(self.CORRECT_ADDRESS_LOCATOR)

    def click_draft_button(self):
        self.click_the_button_action(self.DRAFT_BUTTON_LOCATOR)

    def click_release_button(self):
        self.click(self.RELEASE_LOT_BUTTON_LOCATOR)

    def steps_create_lot(self):
        self.input_product_name()
        self.input_search_category()
        self.click_price()
        self.input_price()
        self.input_date()
        self.input_products_description()
        self.scroll_down()
        self.upload_products_photo()

    def get_title_lot(self):
        return self.get_element_text(self.TITLE_POP_UP_LOCATOR)













