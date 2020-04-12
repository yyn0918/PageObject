from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 初始化，参数中的driver需要指定类型webdriver
    def __init__(self, driver: WebDriver = None):
        # 让python编译器知道有一个实例变量driver
        self.driver = None
        # 如果driver没有值表示第一次实例化子类
        if driver is None:
            # 复用已有浏览器
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
            self.driver.maximize_window()
            # 隐式等待，解决元素加载过慢的问题
            self.driver.implicitly_wait(3)
        # 如果driver有值，说明不是第一次实例化
        else:
            self.driver = driver
