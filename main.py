import time

from awakened_or_not import awakened_or_not
from graph_stuff import generate_graph
from probability_stuff import probability_stuff
from simulate_old_banner import simulate_old_banner
from simulate_new_banner import simulate_new_banner
from simulate_new_new_banner import simulate_new_new_banner


# ask for inputs
awakened_input = input("Is the valk awakened? (yes/no) ")
banner_type = input("Banner type? (0/1/2) ")
qtty_simulation = int(input("How many times to simulate? "))

awakened_sanitized = False
if awakened_input in ["yes", "ye", "y"]:
    awakened_sanitized = True

banner_type_sanitized = int(banner_type)

# calculate stuff
start = time.time()

awakened = awakened_or_not(awakened_sanitized, banner_type_sanitized)
probability_stuff = probability_stuff()
total_dic = {
    "simulations": 0,
    "total_rolls_sum": [0, 0, 0, 0, 0, 0, 0, 0, 0],
    "total_rolls": [{}, {}, {}, {}, {}, {}, {}, {}, {}],
    "total_cards": 0,
    "total_frags_through_frag_drop": 0,
    "total_frags_through_essentine": 0
}

for x in range(qtty_simulation):
    if banner_type_sanitized == 0:
        current_sim = simulate_old_banner(awakened, probability_stuff)
    elif banner_type_sanitized == 1:
        current_sim = simulate_new_banner(awakened, probability_stuff)
    else:
        current_sim = simulate_new_new_banner(awakened, probability_stuff)

    total_dic["simulations"] += 1
    for y in range(9):
        total_dic["total_rolls_sum"][y] += current_sim["rank_list"][y]

        if f'{current_sim["rank_list"][y]}' in total_dic["total_rolls"][y]:
            total_dic["total_rolls"][y][f'{current_sim["rank_list"][y]}'] += 1
        else:
            total_dic["total_rolls"][y][f'{current_sim["rank_list"][y]}'] = 1

    total_dic["total_cards"] += current_sim["cards"]
    total_dic["total_frags_through_frag_drop"] += current_sim["frags_through_frag_drop"]
    total_dic["total_frags_through_essentine"] += current_sim["frags_through_essentine"]

end = time.time()


# print results
print(f'\nSimulated {total_dic["simulations"]} times for getting a 3s '
      f'{"awakened" if awakened_sanitized else "non-awakened"} valk on the '
      f'{"new banner system (5.9+)" if banner_type_sanitized == 1 else "old banner system (5.8-)" if banner_type_sanitized == 0 else "new new banner system (7.3+)"}')

for x, y in [(" s0", 0), (" s1", 1), (" s2", 2), (" s3", 3),
             (" 2s", 4), ("2s1", 5), ("2s2", 6), ("2s3", 7), (" 3s", 8)]:
    generate_graph(total_dic["total_rolls"][y], x, total_dic["simulations"], awakened_sanitized,
                   banner_type_sanitized)
    print(f'Average pulls for {x} valk: {total_dic["total_rolls_sum"][y] / total_dic["simulations"]}')

print(f'\nAverage cards for  3s valk: {total_dic["total_cards"] / total_dic["simulations"]}')
print(f'Average amount of frags gotten through frag drops: '
      f'{total_dic["total_frags_through_frag_drop"] / total_dic["simulations"]}')
print(f'Average amount of frags gotten through essentine: '
      f'{total_dic["total_frags_through_essentine"] / total_dic["simulations"]}')

print(f'\nTime taken to simulate: {end - start:.2f} seconds')
