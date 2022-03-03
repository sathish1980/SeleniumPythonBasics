import pytest


@pytest.mark.usefixtures("setup")
class Testfirst:

    @pytest.mark.usefixtures("dataload")
    def test_firsttescase(self,dataload):
        print("first test case")
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])

   # @pytest.mark.usefixtures("setup2")
    def test_secondtescase(self):
        print("second test case")

    def test_thirdtescase(self):
        print("Third test case")

    #@pytest.mark.usefixtures("paramonfix")
    def test_forthtescase(self,paramonfix):
        print("fourth test case")
        print(paramonfix)

    def test_fifthtescase(self,paramonfixwithmultidata):
        print("fifth test case")
        print(paramonfixwithmultidata[0])