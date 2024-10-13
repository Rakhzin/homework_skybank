def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер банковской карты"""

    masks_card_number = f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"
    return masks_card_number


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счёта"""

    masks_account_number = f"**{str(account_number)[-4:]}"
    return masks_account_number


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
