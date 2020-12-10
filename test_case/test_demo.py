import pytest
from 简易计算器 import calculator as ca
import yaml

class Testcalc:

    def setup_class(self):
        self.cal = ca()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, expect", [
        (1, 2, 3), (-1, -2, -3)
    ], ids=["add1", "add2"])
    def test_add(self, a, b, expect):
        assert self.cal.add(a, b) == expect

    @pytest.mark.parametrize(("a", "b", "expect"), yaml.safe_load(open("./data.yaml", encoding="utf-8"))['test0']
                             , ids=["sub1", "sub2"])
    def test_sub(self, a, b, expect):
        assert self.cal.sub(a, b) == expect

    @pytest.mark.parametrize(("a", "b", "expect"), yaml.safe_load(open("./data.yaml",encoding="utf-8"))['test1']
                             , ids=["mul1", "mul2"])
    def test_mul(self, a, b, expect):
        assert self.cal.mul(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("./data.yaml",encoding="utf-8"))['test2']
                             , ids=["div1", "div2"])
    def test_div(self, a, b, expect):
        assert self.cal.div(a, b) == expect

