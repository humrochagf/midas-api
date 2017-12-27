from django.conf import settings
from django.core.exceptions import ValidationError
from django.test import TestCase
from moneyed import Money

from .models import Entry
from .validators import validate_not_zero


class EntryTestCase(TestCase):

    def test_is_income(self):
        entry = Entry(value=Money(10, settings.MIDAS_DEFAULT_CURRENCY))

        self.assertTrue(entry.is_income)
        self.assertFalse(entry.is_outcome)

    def test_is_outcome(self):
        entry = Entry(value=Money(-10, settings.MIDAS_DEFAULT_CURRENCY))

        self.assertTrue(entry.is_outcome)
        self.assertFalse(entry.is_income)

    def test_not_income_and_not_outcome(self):
        entry = Entry(value=Money(0, settings.MIDAS_DEFAULT_CURRENCY))

        self.assertFalse(entry.is_outcome)
        self.assertFalse(entry.is_income)


class ValidatorsTestCase(TestCase):

    def test_validate_not_zero(self):
        self.assertRaises(ValidationError, validate_not_zero, 0)
        self.assertRaises(ValidationError, validate_not_zero,
                          Money(0, settings.MIDAS_DEFAULT_CURRENCY))
        self.assertIsNone(validate_not_zero(1))
        self.assertIsNone(validate_not_zero(
            Money(1, settings.MIDAS_DEFAULT_CURRENCY)))
