def awakened_or_not(awakened_flag, new_banner):
    if not awakened_flag:
        return {
            "frag_amount": [4, 5, 6],
            "essentine_to_frag": 210 if new_banner else 270,
            "card_value": 30,
            "rankup_list": [25, 50, 75, 100, 150, 200, 250, 300]
        }

    return {
        "frag_amount": [7, 8, 9],
        "essentine_to_frag": 100,
        "card_value": 70,
        "rankup_list": [60, 120, 180, 250, 400, 550, 700, 850]
    }
