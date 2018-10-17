import unittest
from commons import tags
import os


class EnvironmentSetup(unittest.TestCase):
    # setup contains the browser setup attributes

    def setUp(self):
        print(tags.STARTING)
