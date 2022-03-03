import pytest

@pytest.mark.usefixtures("age")
class Test_first():

    @pytest.mark.SIT
    def test_testcase(self):
        print("First test case")

    @pytest.mark.SIT
    def test_testcase2(self):
        print("Second test case")

    @pytest.mark.SIT
    def test_testcase3(self):
        print("Third test case")

    @pytest.mark.xfail
    def test_testcase1(self):
        print("fourth test case")


    @pytest.mark.Sanity
    def test_testcase6(self,age):
        print("fourth test case" + str(age))