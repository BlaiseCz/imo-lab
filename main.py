from pprint import pprint
from readFile import read_file

if __name__ == '__main__':
    overview, coordinates = read_file('data/kroA100.tsp')
    pprint(overview)
    pprint(coordinates)
