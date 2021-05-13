from hall_of_fame.read_file import read_file
from lab1.distance_counter import count_dist

if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = count_dist(coordinates)

    #MSLS:
    # nawalasz local search po 10 razy
    # i in range(100)
    # losowe rozwiązanie
    # puszczam to przez steepest

