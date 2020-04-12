from selenium.webdriver.common.by import By

from page import BasePage


class AddMember(BasePage):
    # 在添加成员页面填写信息并保存
    def add_member(self):
        # 填写成员信息
        self.driver.find_element_by_id("username").send_keys("uname1")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("acctid2")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("12345678910")
        # 点击【保存】按钮
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

    def get_first_member(self):
        # 获得成员列表中第一个人的姓名
        return self.driver.find_element(By.CSS_SELECTOR, "#member_list tr:nth-child(1) td:nth-child(2)").get_attribute(
            "title")
