import random
from math import floor


def simulate_old_banner(awk_values, probability):
    roll_count = 0
    card_count = 0
    rank_list = []

    got_valk_flag = False

    frag_count = 0
    essentine_count = 0
    pulls_since_last_card = 0
    bonus_essentine_countdown = 0

    frags_through_frag_drop = 0
    frags_through_essentine = 0

    rankup_count = 0
    next_rankup = awk_values["rankup_list"][rankup_count]

    while frag_count < awk_values["rankup_list"][7]:
        while frag_count >= next_rankup and got_valk_flag:
            rankup_count += 1
            next_rankup = awk_values["rankup_list"][rankup_count]
            rank_list += [roll_count]

        if pulls_since_last_card != 99:
            current_rate = max(1.5, 1.5 * (pulls_since_last_card - 73))

            roll = random.choices(probability["possible_outcomes_main"],
                                  cum_weights=[current_rate, (current_rate + 2.25), 100],
                                  k=1)[0]
        else:
            roll = "card"

        roll_count += 1

        if got_valk_flag:
            roll_essentine = random.choices(probability["possible_outcomes_side"],
                                            cum_weights=probability["weights_side"],
                                            k=1)[0]

            if bonus_essentine_countdown > 0:
                essentine_count += floor(roll_essentine * 1.5)
                bonus_essentine_countdown -= 1
            else:
                essentine_count += roll_essentine

            frag_count += floor(essentine_count / awk_values["essentine_to_frag"])
            frags_through_essentine += floor(essentine_count / awk_values["essentine_to_frag"])
            essentine_count %= awk_values["essentine_to_frag"]

        if roll == "frags":
            frag_roll = random.choice(awk_values["frag_amount"])

            frag_count += frag_roll
            frags_through_frag_drop += frag_roll
            pulls_since_last_card += 1

        elif roll == "card":
            if got_valk_flag:
                frag_count += awk_values["card_value"]
            else:
                rank_list += [roll_count]
                got_valk_flag = True

            card_count += 1
            bonus_essentine_countdown = 60
            pulls_since_last_card = 0

        else:
            pulls_since_last_card += 1

    rank_list += [roll_count]

    return {
        "rank_list": rank_list,
        "frags": frag_count,
        "cards": card_count,
        "frags_through_frag_drop": frags_through_frag_drop,
        "frags_through_essentine": frags_through_essentine
    }
