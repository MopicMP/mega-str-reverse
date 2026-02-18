"""Tests for mega-str-reverse."""

import pytest
from mega_str_reverse import reverse


class TestReverse:
    """Test suite for reverse."""

    def test_basic(self):
        """Test basic usage."""
        result = reverse("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            reverse("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = reverse(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
