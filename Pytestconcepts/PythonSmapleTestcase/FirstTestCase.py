import pytest

@pytest.mark.usefixtures("ficture_value")
class TestFirstTestcase():
    @pytest.mark.SIT
    def testnumberonetescase(self):
        print("This is first test case")

    @pytest.mark.UAT
    def testnumbertwotescase(self):
        print("This is second test case")

    @pytest.mark.Sanity
    def testnumberthreetescase(self):
        print("This is third test case")

    @pytest.mark.Sanity
    def testnumbertwothirdtescase(self,ficture_value2):
        print("This is forth test case")

    @pytest.fixture
    def ficture_value(self):
        print("first test case before setup")
        yield
        print("first test case after setup ")

    @pytest.fixture
    def ficture_value2(self):
        print("This is Fixture value2")
        yield
        print("After fixtures2")