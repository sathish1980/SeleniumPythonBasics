import pytest


@pytest.fixture(scope="class")
def setup():
    print("This is fixtures1 - before test case")
    yield
    print("This is Yield1 - after test")

@pytest.fixture()
def setup2():
    print("This is fixtures2 - before test case")
    yield
    print("This is Yield2 - after test")
@pytest.fixture()
def dataload():
    return ["sathish", "kumar", "1990"]

@pytest.fixture(params =["chrome","firefox","IE"])
def paramonfix(request):
    return request.param

@pytest.fixture(params =[("chrome","sathish","password"),("firefox","username1","password1"),("IE","ie-username1","ie-password"),("Edge","Edge-username1","Edge-password")])
def paramonfixwithmultidata(request):
    return request.param

@pytest.fixture
def age():
    print("Before each test case")
    yield
    print("After each testcase")


