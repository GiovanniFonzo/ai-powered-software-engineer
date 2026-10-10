from src.tax_service import calculate_total_with_tax


def test_calculate_total_with_tax_uses_mocked_tax_rate():
    def fake_get_tax_rate(country_code):
        return 0.23

    result = calculate_total_with_tax(100, "IE", fake_get_tax_rate)

    assert result == 123.0


