def awakened_or_not(awakened_flag, banner_type):
    if not awakened_flag:
        return {
            "frag_amount": [4, 5, 6],
            "essentine_to_frag": 210 if banner_type == 0 else 270,
            "card_value": 30 if banner_type != 2 else 50,
            "rankup_list": [25, 50, 75, 100, 150, 200, 250, 300]
        }

    return {
        "frag_amount": [7, 8, 9],
        "essentine_to_frag": 100,
        "card_value": 70 if banner_type != 2 else 150,
        "rankup_list": [60, 120, 180, 250, 400, 550, 700, 850]
    }
