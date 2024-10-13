def mask_account_card(name_cart_account: str) -> str:
    """Обрабатывает информацию о картах и счетах"""

    if name_cart_account[-16:].isdigit() and name_cart_account[-17] == " ":
        mask_card = (
            f"{name_cart_account[:-16]} "
            f"{name_cart_account[-16:-12]} "
            f"{name_cart_account[-12:-10]}** "
            f"**** "
            f"{name_cart_account[-4:]}"
        )
        return mask_card

    else:
        mask_card = f"{name_cart_account[:4]} **{name_cart_account[-4:]}"
        return mask_card


def get_date(data: str) -> str:
    """Вывдит дату в виде: ДД.ММ.ГГГГ"""

    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
