import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualize(res, coordinates, cycle=True):
    res_coord_x = [coordinates[r][0] for r in res]
    res_coord_y = [coordinates[r][1] for r in res]
    xcoord = [x for x, y in coordinates]
    ycoord = [y for x, y in coordinates]
    if cycle:
        res_coord_x.append(coordinates[res[0]][0])
        res_coord_y.append(coordinates[res[0]][1])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim(min(xcoord)-100, max(xcoord)+100)
    plt.ylim(min(ycoord)-100, max(ycoord)+100)
    plt.plot(res_coord_x, res_coord_y, '-', color='blue')
    plt.plot(xcoord, ycoord, 'o', color='black', markersize=4)
    plt.show()

def visualize2(res1, res2, coordinates, cycle=True):
    res_coord_x10 = [coordinates[r][0] for r in res1[0]]
    res_coord_x11 = [coordinates[r][0] for r in res1[1]]
    res_coord_y10 = [coordinates[r][1] for r in res1[0]]
    res_coord_y11 = [coordinates[r][1] for r in res1[1]]
    res_coord_x20 = [coordinates[r][0] for r in res2[0]]
    res_coord_x21 = [coordinates[r][0] for r in res2[1]]
    res_coord_y20 = [coordinates[r][1] for r in res2[0]]
    res_coord_y21 = [coordinates[r][1] for r in res2[1]]
    xcoord = [x for x, y in coordinates]
    ycoord = [y for x, y in coordinates]
    if cycle:
        res_coord_x10.append(coordinates[res1[0][0]][0])
        res_coord_x11.append(coordinates[res1[1][0]][0])
        res_coord_y10.append(coordinates[res1[0][0]][1])
        res_coord_y11.append(coordinates[res1[1][0]][1])
        res_coord_x20.append(coordinates[res2[0][0]][0])
        res_coord_x21.append(coordinates[res2[1][0]][0])
        res_coord_y20.append(coordinates[res2[0][0]][1])
        res_coord_y21.append(coordinates[res2[1][0]][1])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim(min(xcoord)-100, max(xcoord)+100)
    plt.ylim(min(ycoord)-100, max(ycoord)+100)
    plt.plot(res_coord_x10, res_coord_y10, '-', label='before', color='red')
    plt.plot(res_coord_x11, res_coord_y11, '-', label='before', color='orange')
    plt.plot(res_coord_x20, res_coord_y20, '-', label='after', color='green')
    plt.plot(res_coord_x21, res_coord_y21, '-', label='after', color='blue')
    plt.plot(xcoord, ycoord, 'o', color='black', markersize=4)
    plt.legend()
    plt.show()

def animate_old(results, coordinates, cycle=True):

    # setting up aspects and limits
    xcoord = [x for x, y in coordinates]
    ycoord = [y for x, y in coordinates]

    minlim = min(min(xcoord), min(ycoord))
    maxlim = max(max(xcoord), max(ycoord))

    fig = plt.figure()
    ax1 = plt.axes(
        xlim=(min(xcoord)-100, max(xcoord)+100),
        ylim=(min(ycoord)-100, max(ycoord)+100))
    ax1.set_aspect('equal')
    ax1.set_visible(False)

    # setting up plots
    line, = ax1.plot([], [])
    lines = []
    lobj = ax1.plot([],[], 'o', color='black', markersize=4)[0]
    lines.append(lobj)
    dobj = ax1.plot([],[], '-', color='blue')[0]
    lines.append(dobj)


    def init():
        for line in lines:
            line.set_data([],[])
        return lines

    x1,y1 = xcoord, ycoord
    x2,y2 = [],[]

    def animate(i):
        x2 = [coordinates[r][0] for r in results[i]]
        y2 = [coordinates[r][1] for r in results[i]]
        if cycle:
            x2.append(coordinates[results[i][0]][0])
            y2.append(coordinates[results[i][0]][1])

        xlist = [x1, x2]
        ylist = [y1, y2]

        for lnum,line in enumerate(lines):
            line.set_data(xlist[lnum], ylist[lnum])

        return lines

    anim = FuncAnimation(fig, animate, init_func=init,
                                   frames=range(len(coordinates)), blit=True)

    plt.show()


def animate(history, coordinates, cycle=[True]):
    if type(history[0][0]) is not list:
        history = [[h] for h in history]
    if type(cycle) is not list:
        cycle = [cycle]
    plots_num = len(history[0])

    # setting up aspects and limits
    xcoord = [x for x, y in coordinates]
    ycoord = [y for x, y in coordinates]

    minlim = min(min(xcoord), min(ycoord))
    maxlim = max(max(xcoord), max(ycoord))

    fig = plt.figure()
    ax1 = plt.axes(
        xlim=(min(xcoord)-100, max(xcoord)+100),
        ylim=(min(ycoord)-100, max(ycoord)+100))
    ax1.set_aspect('equal')
    ax1.set_visible(False)

    # setting up plots
    line, = ax1.plot([], [])
    lines = []
    lobj = ax1.plot([],[], 'o', color='black', markersize=4)[0]
    lines.append(lobj)

    # dobj = ax1.plot([],[], '-', color='blue')[0]
    for pi in range(plots_num):
        lines.append(ax1.plot([],[], '-')[0])


    def init():
        for line in lines:
            line.set_data([],[])
        return lines

    x1,y1 = xcoord, ycoord
    x2,y2 = [],[]

    def animate(i):
        xlist = [x1]
        ylist = [y1]
        for pi in range(plots_num):
            x2 = [coordinates[r][0] for r in history[i][pi]]
            y2 = [coordinates[r][1] for r in history[i][pi]]
            if cycle[pi]:
                x2.append(coordinates[history[i][pi][0]][0])
                y2.append(coordinates[history[i][pi][0]][1])
            xlist.append(x2)
            ylist.append(y2)


        for lnum,line in enumerate(lines):
            line.set_data(xlist[lnum], ylist[lnum])

        return lines

    frames = list(range(len(history)))
    frames.extend([len(history)-1]*5)
    anim = FuncAnimation(fig, animate, init_func=init,
                                   frames=frames, blit=True)

    plt.show()
