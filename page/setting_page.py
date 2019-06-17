from selenium.webdriver.common.by import By
import allure
from base.base_action import BaseAction


class SettingPage(BaseAction):

    search_button = By.ID, "com.android.settings:id/search"
    @allure.step('点击搜索框')
    def click_search(self):
        self.click(self.search_button)