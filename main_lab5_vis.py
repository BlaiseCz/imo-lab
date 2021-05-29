from hall_of_fame.distance import create_distance_matrix
from hall_of_fame.read_file import read_file
from hall_of_fame.visualize import animate

if __name__ == '__main__':
    data_set = 'kroB'
    overview, coordinates = read_file('data/' + data_set + '100.tsp')
    distance_matrix = create_distance_matrix(coordinates)

    cycles =[[32, 5, 3, 82, 42, 51, 83, 6, 56, 93, 34, 60, 26, 70, 11, 89, 45, 24, 8, 33, 57, 53, 87, 22, 21, 54, 13, 63, 81, 41, 1, 15, 76, 23, 17, 95, 18, 43, 91, 35, 44, 40, 16, 77, 12, 62, 30, 47, 50, 14], [74, 29, 48, 85, 67, 9, 20, 0, 94, 97, 31, 58, 75, 28, 7, 98, 96, 90, 27, 2, 10, 92, 84, 72, 52, 69, 38, 39, 66, 4, 61, 68, 25, 99, 55, 80, 78, 64, 46, 49, 88, 86, 65, 73, 59, 71, 36, 37, 19, 79]]
    animate(cycles, coordinates)