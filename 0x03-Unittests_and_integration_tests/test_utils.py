#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from typing import Mapping, Sequence, Any, Dict
import utils
import unittest
from unittest.mock import patch
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
 
class TestGetJson(unittest.TestCase):
    """ Test get_json method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}, {"payload": True}),
        ("http://holberton.io", {"payload": False}, {"payload": False}),
        ])
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool] , expected: Dict[str, bool]) -> None:
        """ Test Mocked HTTP call """
        with patch('utils.requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            result = utils.get_json(test_url)
            self.assertEqual(result, expected)
            mocked_get.assert_called_once()

