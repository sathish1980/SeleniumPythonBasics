import pytest



class scnd:
    @pytest.mark.skip
    @pytest.mark.usefixtures()
    def test_secondtestcase(self):
        print("second testcacse")
    @pytest.mark.xfail
    @pytest.mark.usefixtures()
    def test_firsttestcase(self):
        print("first testcacse")

    @pytest.mark.Sanity
    @pytest.mark.usefixtures()
    def test_thirdtestcase(self):
        print("Third testcacse")

