"""Classes for melon orders."""


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

        # requires user input when instantiating to be perfect
        if self.species == "Christmas melon":
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

        # else:
        #     super(InternationalMelonOrder, self).get_total()

# class DomesticMelonOrder(object):
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder(object):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code
