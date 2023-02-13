import pytest

from pytestDemo.getLogger import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_FixturesData(self, dataLoad):
        print("Aniket-----", type(dataLoad))
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])

