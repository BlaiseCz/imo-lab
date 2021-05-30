from hall_of_fame.distance import create_distance_matrix
from hall_of_fame.read_file import read_file
from hall_of_fame.visualize import animate

if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '200.tsp')
    distance_matrix = create_distance_matrix(coordinates)

    cycles = [[][]]
    animate(cycles, coordinates)