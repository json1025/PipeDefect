class DataTransformation:
    LOCATIONS = {}  # key: location   value: (starting index, ending index)
    FINAL_DATA_ROW_LENGTH = 100
    SHIFT = 10

    def __init__(self, data_row):
        self.data_row = data_row
        self.final_data = []

    @classmethod
    def init_locations(cls, loc_row):
        temp = []
        for i, location in enumerate(loc_row):
            if i == 0:  # skips the header
                continue
            if location != loc_row[i-1]:
                cls.LOCATIONS[float(location)] = None
                temp.append(i)
        temp.append(len(loc_row))
        i = 1
        for location in cls.LOCATIONS:
            cls.LOCATIONS[location] = (temp[i-1], temp[i])  # (starting index, ending index)
            i += 1

    def process_data(self):
        for location, indices in self.LOCATIONS.items():
            first_index = indices[0]
            last_index = first_index + self.FINAL_DATA_ROW_LENGTH - 1
            while last_index < indices[1]:
                self.add_row(first_index, self.FINAL_DATA_ROW_LENGTH, location)
                first_index += self.SHIFT
                last_index += self.SHIFT
            if first_index < last_index:
                self.add_row(first_index, indices[1]-first_index, location)

    def add_row(self, first_index, length, loc):
        self.final_data.append([])
        for i in range(length):
            self.final_data[-1].append(self.data_row[i + first_index])
        self.final_data[-1].append(loc)
