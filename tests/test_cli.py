"""Test for eldoled cli."""
import eldoled.cli
import unittest


class TestCli(unittest.TestCase):
    """TestCli."""

    def setUp(self):
        """TestCli."""
        self.hello_message = "Hello world!"

    def test_prints_hello_world(self):
        """TestCli."""
        output = eldoled.cli.hello()
        self.assertEquals(output, self.hello_message)
