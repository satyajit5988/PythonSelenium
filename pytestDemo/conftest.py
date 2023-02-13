import pytest


@pytest.fixture(scope="class")
def setup():
    print("I should be executed first")
    yield
    print("I would be executed last")


@pytest.fixture()
def dataLoad():
    print("Passing Data to TestCase")
    return ["Satyajit", "More"]


@pytest.fixture(params=[("Chrome", "Rahul"), ("Firefox", "Rahul"), "IE"])
def crossBrowser(request):
    return request.param
