import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(history: list, coordinates: list, isCycle=[True, True]):
    """
    Funkcja do animacji/ wyświetlania rozwiązań.

    history: historia (lista wersji) albo jedna wersja.
    - każda wersja jest listą cykli
    - każdy cykl jest listą wierzchołków

    isCycle: lista Booleanów określająca czy coś jest cyklem czy ścieżką, albo
    jeden Boolean (jeżeli jest tylko jeden cykl/ścieżka).
    """
    if type(history[0]) is not list:
        # jeżeli history to cykl
        history = [[history]]
    elif type(history[0][0]) is not list:
        # jeżeli history to lista cykli
        if type(isCycle) is not list or len(isCycle) == 1:
            # jeżeli history to historia jednego cyklu
            history = [[h] for h in history]
        else:
            # jeżeli history to kilka cykli (nie historia!)
            history = [history]
    if type(isCycle) is not list:
        isCycle = [isCycle]
    assert len(history[0]) == len(isCycle), 'ilość cykli nie pasuje do długości parametru isCycle!'
    plots_num = len(history[0])

    # setting up aspects and limits
    xcoord = [x for x, y in coordinates]
    ycoord = [y for x, y in coordinates]

#     minlim = min(min(xcoord), min(ycoord))
#     maxlim = max(max(xcoord), max(ycoord))

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

    def animate(i):
        xlist = [x1]
        ylist = [y1]
        for pi in range(plots_num):
            x2 = [coordinates[r][0] for r in history[i][pi]]
            y2 = [coordinates[r][1] for r in history[i][pi]]
            if isCycle[pi]:
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

if __name__ == '__main__':
    from read_file import read_file
    from distance import create_distance_matrix
    _, coordinates = read_file('../data/kroA100.tsp')

    cycle1 = list(range(50))
    cycle2 = list(range(50, 100))

    animate([cycle1, cycle2], coordinates, isCycle=[True, True])

