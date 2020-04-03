from web.PageObj.demo1.page.main import MainPage


class TestAddMem:
    def setup(self):
        self.add_mem_page = MainPage().login_by_cookie().goto_add_mem()

    def test_add_mem(self):
        #self.add_mem_page.clean_environment()
        self.add_mem_page.add_mem()
        mem = self.add_mem_page.get_new_mem()
        assert mem.text == 'test'


