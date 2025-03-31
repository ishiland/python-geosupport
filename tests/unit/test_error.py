from geosupport.error import GeosupportError

from ..testcase import TestCase


class TestError(TestCase):

    def test_error(self):
        e = GeosupportError("")
