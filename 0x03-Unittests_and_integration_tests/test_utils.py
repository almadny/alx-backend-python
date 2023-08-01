#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from typing import Mapping, Sequence, Any
import utils
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Defines test cases for utils """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self,
            nested_map: Mapping[str, Any],
            path: Sequence[str],
            expected: Any) -> None:
        """ Test the access nested map method """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping[str, Any],
            path: Sequence[str],
            expected: Any) -> None:
        with self.assertRaises(expected):
            utils.access_nested_map(nested_map, path)
