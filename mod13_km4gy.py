# Khai Moffett (km4gy)
import unittest
import re
from datetime import datetime
 
 
# --- Validation functions (mirrors the input checks from Project 3) ---
 
def validate_symbol(symbol):
    """1-7 uppercase alpha characters."""
    return bool(re.match(r'^[A-Z]{1,7}$', symbol))
 
def validate_chart_type(chart_type):
    """Single numeric character: 1 or 2."""
    return chart_type in ['1', '2']
 
def validate_time_series(time_series):
    """Single numeric character: 1, 2, 3, or 4."""
    return time_series in ['1', '2', '3', '4']
 
def validate_date(date_str):
    """Date string in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
 
def validate_date_range(start_str, end_str):
    """End date must not be before start date. Both must be valid dates."""
    try:
        start = datetime.strptime(start_str, '%Y-%m-%d')
        end = datetime.strptime(end_str, '%Y-%m-%d')
        return end >= start
    except ValueError:
        return False
 
 
# --- Unit Tests ---
 
class TestSymbol(unittest.TestCase):
 
    def test_valid_single_char(self):
        self.assertTrue(validate_symbol('A'))
 
    def test_valid_typical_ticker(self):
        self.assertTrue(validate_symbol('AAPL'))
 
    def test_valid_seven_chars(self):
        self.assertTrue(validate_symbol('ABCDEFG'))
 
    def test_invalid_too_long(self):
        self.assertFalse(validate_symbol('TOOLONGS'))
 
    def test_invalid_lowercase(self):
        self.assertFalse(validate_symbol('aapl'))
 
    def test_invalid_mixed_case(self):
        self.assertFalse(validate_symbol('Aapl'))
 
    def test_invalid_contains_digit(self):
        self.assertFalse(validate_symbol('AAP1'))
 
    def test_invalid_empty(self):
        self.assertFalse(validate_symbol(''))
 
    def test_invalid_special_chars(self):
        self.assertFalse(validate_symbol('AA.PL'))
 
 
class TestChartType(unittest.TestCase):
 
    def test_valid_bar(self):
        self.assertTrue(validate_chart_type('1'))
 
    def test_valid_line(self):
        self.assertTrue(validate_chart_type('2'))
 
    def test_invalid_zero(self):
        self.assertFalse(validate_chart_type('0'))
 
    def test_invalid_three(self):
        self.assertFalse(validate_chart_type('3'))
 
    def test_invalid_letter(self):
        self.assertFalse(validate_chart_type('a'))
 
    def test_invalid_empty(self):
        self.assertFalse(validate_chart_type(''))
 
    def test_invalid_multiple_digits(self):
        self.assertFalse(validate_chart_type('12'))
 
 
class TestTimeSeries(unittest.TestCase):
 
    def test_valid_1(self):
        self.assertTrue(validate_time_series('1'))
 
    def test_valid_2(self):
        self.assertTrue(validate_time_series('2'))
 
    def test_valid_3(self):
        self.assertTrue(validate_time_series('3'))
 
    def test_valid_4(self):
        self.assertTrue(validate_time_series('4'))
 
    def test_invalid_zero(self):
        self.assertFalse(validate_time_series('0'))
 
    def test_invalid_five(self):
        self.assertFalse(validate_time_series('5'))
 
    def test_invalid_letter(self):
        self.assertFalse(validate_time_series('b'))
 
    def test_invalid_empty(self):
        self.assertFalse(validate_time_series(''))
 
 
class TestStartDate(unittest.TestCase):
 
    def test_valid_date(self):
        self.assertTrue(validate_date('2023-01-15'))
 
    def test_valid_leap_day(self):
        self.assertTrue(validate_date('2024-02-29'))
 
    def test_invalid_wrong_format_slashes(self):
        self.assertFalse(validate_date('01/15/2023'))
 
    def test_invalid_wrong_format_mmddyyyy(self):
        self.assertFalse(validate_date('01-15-2023'))
 
    def test_invalid_month_out_of_range(self):
        self.assertFalse(validate_date('2023-13-01'))
 
    def test_invalid_day_out_of_range(self):
        self.assertFalse(validate_date('2023-01-32'))
 
    def test_invalid_not_a_date(self):
        self.assertFalse(validate_date('not-a-date'))
 
    def test_invalid_empty(self):
        self.assertFalse(validate_date(''))
 
 
class TestEndDate(unittest.TestCase):
 
    def test_valid_date(self):
        self.assertTrue(validate_date('2024-12-31'))
 
    def test_valid_start_of_year(self):
        self.assertTrue(validate_date('2024-01-01'))
 
    def test_invalid_wrong_format_slashes(self):
        self.assertFalse(validate_date('12/31/2024'))
 
    def test_invalid_wrong_format_no_dashes(self):
        self.assertFalse(validate_date('20241231'))
 
    def test_invalid_zero_month(self):
        self.assertFalse(validate_date('2024-00-01'))
 
    def test_invalid_impossible_day(self):
        self.assertFalse(validate_date('2024-02-30'))
 
    def test_invalid_letters(self):
        self.assertFalse(validate_date('2024-ab-cd'))
 
    def test_invalid_empty(self):
        self.assertFalse(validate_date(''))
 
 
class TestDateRange(unittest.TestCase):
 
    def test_valid_range(self):
        self.assertTrue(validate_date_range('2023-01-01', '2023-12-31'))
 
    def test_same_day(self):
        """Start and end on the same day should be valid."""
        self.assertTrue(validate_date_range('2023-06-15', '2023-06-15'))
 
    def test_end_before_start(self):
        self.assertFalse(validate_date_range('2023-12-31', '2023-01-01'))
 
    def test_end_one_day_before_start(self):
        self.assertFalse(validate_date_range('2023-06-15', '2023-06-14'))
 
    def test_invalid_start_date(self):
        """Bad start date should return False."""
        self.assertFalse(validate_date_range('not-a-date', '2023-12-31'))
 
    def test_invalid_end_date(self):
        """Bad end date should return False."""
        self.assertFalse(validate_date_range('2023-01-01', 'not-a-date'))
 
    def test_multi_year_range(self):
        self.assertTrue(validate_date_range('2020-01-01', '2024-12-31'))
 
 
if __name__ == '__main__':
    unittest.main()
