"""Tests for currency converter."""

from unittest import TestCase

from app import app


class CurrencyConvertedTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_form_shows(self):
        """Test that form appears."""

        with self.client as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertIn('<form', html)

    def test_form_failures(self):
        """Test conversion failures."""

        with self.client as client:
            resp = client.get(
                "/convert",
                query_string={"code_from": "MUPPET",
                              "code_to": "BLARGH",
                              "amt": "glumph"})
            html = resp.get_data(as_text=True)
            self.assertIn('Not a valid amount', html)
            self.assertIn('Not a valid code: MUPPET', html)
            self.assertIn('Not a valid code: BLARGH', html)

    def test_conversion(self):
        """Test conversion."""

        # difficult to test as rates vary---so let's convert USD to USD
        with self.client as client:
            resp = client.get(
                "/convert",
                query_string={"code_from": "USD",
                              "code_to": "USD",
                              "amt": "1.55"})
            html = resp.get_data(as_text=True)
            self.assertIn('$ 1.55', html)
