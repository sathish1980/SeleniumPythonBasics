import pytest

@pytest.mark.usefixtures("setup")
class TestSecondTestcase():
    @pytest.mark.SIT
    def testnumberonetescase(self):
        print("This is first test case")

    @pytest.mark.skip
    def testnumbertwotescase(self):
        print("This is second test case")

    @pytest.mark.Sanity
    def testnumberthreetescase(self,paramonfixwithmultidata):

        print("This is third test case: " +paramonfixwithmultidata[1])
        print("This is third test case with second param: " + paramonfixwithmultidata[2])

    @pytest.mark.Sanity
    def testnumbertwothirdtescase(self,dataload):
        print("This is forth test case: "+ dataload[0])
        print("This is forth test case: " + dataload[1])
        print("This is forth test case: " + dataload[2])

    @pytest.fixture
    def ficture_value2(self):
        print("This is Fixture value2")
        yield
        print("After fixtures2")