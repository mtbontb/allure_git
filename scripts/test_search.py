from base.base_driver import init_driver
from page.page import Page

import pytest


class TestSearch:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("keyword", ["xiaoming", "123", "hello"])
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_search(self, keyword):
        self.page.setting.click_search()
        self.page.search.input_search(keyword)
        self.page.search.click_back()

    def test_hh(self):
        print ('hhh')
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_hh1(self):
        print ('hhh1')
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_hh2(self):
        print ('hhh2')
        assert 1
