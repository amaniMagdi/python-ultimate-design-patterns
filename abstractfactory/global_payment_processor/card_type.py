from enum import Enum


class CardType(Enum):
    """
    Enum for card types.
    """
    VISA = 1
    MASTER_CARD = 2
    AMERICAN_EXPRESS = 3
    DINERS = 4
    CARTE_BANCAIRE = 5