import pytest


@pytest.mark.usefixtures("setup")
class Test_final():

   # @pytest.mark.usefixtures("setup")
    def test_thirdtescase(self):
        print("Third test case")


    def test_forthtescase(self,setup2):
        print("Forth test case")


    def test_fifthescase(self):
        print("Fifth test case")

    def test_sixthhescase(self,dataload):
        print("six test case")
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])

    def test_seventhhescase(self, paramonfix):
        print("seventh test case")
        print(paramonfix)

    def test_eighthescase(self, paramonfixwithmultidata):
        print("seventh test case")
        print(paramonfixwithmultidata[0])
        print(paramonfixwithmultidata[1])
        print(paramonfixwithmultidata[2])


