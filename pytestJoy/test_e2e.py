import pytest

from pytestJoy.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestJoy(BaseClass):

    # @pytest.mark.skip

    #@pytest.mark.smoke
    def test_Booking(self):
        #print("Hello")
        log = self.getLogger()
        log.info("hello")

    def test_Contact(self):
        msg = "hello1"
        assert msg == "hello", "test failed"

    @pytest.mark.smoke
    def test_fixtureDemo(self):
        print("i will execute steps in fixture")