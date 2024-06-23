import pytest


@pytest.fixture()
def setup():
    print("i will be executed first")
    yield
    print("i will be executed last")

