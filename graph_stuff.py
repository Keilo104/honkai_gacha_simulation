from matplotlib import pyplot as plt
import matplotlib.ticker as mtick


def generate_graph(total_rolls_dict, rank, total_simulations, awakened_sanitized, banner_type_sanitized):
    graph_list = []

    for x, y in total_rolls_dict.items():
        graph_list += [[int(x), y]]

    graph_list.sort(key=lambda item: item[0])

    names = []
    values = []
    for x in graph_list:
        names += [x[0]]
        values += [x[1]]

    cum_values = [graph_list[0][1]]
    for x in range(1, len(graph_list)):
        graph_list[x][1] += graph_list[x-1][1]
        cum_values += [graph_list[x][1]]

    for x in range(len(cum_values)):
        cum_values[x] /= total_simulations

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle(f'Average pulls for {rank} {"awakened" if awakened_sanitized else "non-awakened"}'
                 f' on {"new banner system (5.9+)" if banner_type_sanitized else "old banner system (5.8-)"}')

    ax1.plot(names, values)
    ax1.set_ylabel("normal idk")

    ax2.plot(names, cum_values)
    ax2.set_ylabel("Cumulative")
    ax2.set_xlabel("Number of Pulls")

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.show()
