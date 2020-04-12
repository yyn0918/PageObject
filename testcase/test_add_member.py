from time import sleep

from page import Index


class TestAddMember:
    def setup(self):
        self.index = Index()

    def test_add_member(self):
        # goto_add_member实例化了AddMember
        add_member = self.index.goto_add_member()
        # 添加成员
        add_member.add_member()
        sleep(2)
        # 验证是否添加成功
        assert add_member.get_first_member() == "uname1"
