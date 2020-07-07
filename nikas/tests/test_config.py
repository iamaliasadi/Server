# -*- encoding: utf-8 -*-

import io
import unittest

from nikas import config


class TestConfig(unittest.TestCase):

    def test_parser(self):
        parser = config.NikasParser(allow_no_value=True)
        parser.read_file(io.StringIO(u"""
            [foo]
            bar = 1h
            baz = 12
            spam = a, b, cdef
            bla =
                spam
                ham
            asd = fgh"""))

        self.assertEqual(parser.getint("foo", "bar"), 3600)
        self.assertEqual(parser.getint("foo", "baz"), 12)
        self.assertEqual(parser.getlist("foo", "spam"), ['a', 'b', 'cdef'])
        self.assertEqual(list(parser.getiter("foo", "bla")), ['spam', 'ham'])
        self.assertEqual(list(parser.getiter("foo", "asd")), ['fgh'])
