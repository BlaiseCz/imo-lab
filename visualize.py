import matplotlib.pyplot as plt

def visualize(res, coordinates):
    res_coord_x = [coordinates[r][0] for r in res]
    res_coord_x.append(coordinates[res[0]][0])
    res_coord_y = [coordinates[r][1] for r in res]
    res_coord_y.append(coordinates[res[0]][1])
    plt.axis('off')
    plt.plot(res_coord_x, res_coord_y, '-o', markersize=4)
    plt.show()
