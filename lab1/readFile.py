def read_file(path):
    with open(path) as file:
        overview = {}
        coordinates = []
        for line in file:
            if not line[0].isnumeric():
                parts = line.split(':')
                if len(parts) != 2:
                    continue
                overview[parts[0].strip()] = parts[1].strip()
            else:
                parts = line.split()
                coordinates.append((int(parts[1]), int(parts[2])))

        return overview, coordinates

