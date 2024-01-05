# Create an abstract class Money which takes currency and value as input and initializes it. A class must have these methods:

# get_value method which returns the value of the money.
# get_currency method which returns the currency of the money.
# convert_to_currency abstract method, which takes target currency and conversion rate as input and converts the value of the money to the target currency.
# Now create two subclasses of Money: Cash and Card. The Cash class should take the denomination of the cash as input in the constructor,
# and should implement the convert_to_currency method. The Card class should take the credit limit of the card as input in the constructor,
# and should implement the convert_to_currency method using the conversion rate to convert the value of the card to the target currency.

from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, currency: str, value: int) -> None:
        self.currency = currency
        self.value = value

    def get_value(self) -> int:
        return self.value

    def get_currency(self) -> str:
        return self.currency

    @abstractmethod
    def convert_to_currency(self) -> float:
        pass


class Cash(Money):
    def __init__(self, currency: str, value: int, denominator: float) -> None:
        super().__init__(currency, value)
        self.denominator = denominator

    def convert_to_currency(self) -> float:
        return self.currency / self.denominator


class Card(Money):
    def __init__(self, currency: str, value: int, credit_limit: float) -> None:
        super().__init__(currency, value)
        self.credit_limit = credit_limit
    
    def convert_to_currency(self) -> float:
        return self.currency / self.credit_limit
