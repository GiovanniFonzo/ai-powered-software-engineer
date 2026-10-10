def calculate_total_with_tax(amount: int | float, country_code: str, get_tax_rate) -> int | float:
    """Return the total amount including tax for a country."""
    tax_rate = get_tax_rate(country_code)

    return amount + (amount * tax_rate)
