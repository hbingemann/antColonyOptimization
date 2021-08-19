
class CitiesFromTSPFile:

    def __init__(self, tsp_file_name):
        with open(tsp_file_name, "r") as tsp_file:
            content = tsp_file.readlines()
            line_of_city_start = content.index("NODE_COORD_SECTION\n") + 1
            line_of_city_end = content.index("EOF\n")
            city_lines = content[line_of_city_start:line_of_city_end]
            self._cities = []
            for line in city_lines:
                city_info = line.strip().split(" ")
                city_number, city_x, city_y = city_info
                self._cities.append((float(city_x), float(city_y)))

    def get_city_count(self):
        return len(self._cities)

    def __iter__(self):
        for city in self._cities:
            yield city

    def get_first(self):
        return self._cities[0]

    def get(self, index):
        return self._cities[index]

    def get_index(self, item):
        return self._cities.index(item)

    def get_city_list(self):
        return self._cities.copy()


