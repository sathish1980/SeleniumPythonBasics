import pytest


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
    def testnumbertwothirdtescase(self):
        print("This is forth test case")