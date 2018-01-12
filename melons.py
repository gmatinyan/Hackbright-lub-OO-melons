"""Classes for melon orders."""

CHRISTMAS = "Christmas melon"

class AbstractMelonOrder(object):
    """Abstract class for domestic or international melons."""

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

        if country_code:
            self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == CHRISTMAS:
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record whether or not an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize an international melon order with a country code."""
        super(InternationalMelonOrder, self).__init__(species, qty,
                                                      country_code)

    def get_total(self):
        """All orders under 10 have a flat fee of $3."""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the U.S. Government."""

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        """Checks if melon has been inspected and marks it."""
        pass
        # if passed:
        #     self.passed_inspection = True
