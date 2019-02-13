# proc_data_row_length = 100
# shift = 10


class DataTransformation:
    location_indices = []

    def __init__(self, data_row, location_row, proc_data_row_length, shift):
        self.data_row = data_row
        self.proc_data_row_length = proc_data_row_length
        self.shift = shift
        self.proc_data = []
        self.find_location_indices(location_row)

    def find_location_indices(self, location_row):
        self.location_indices.append(location_row[0])
        for i in range(len(location_row)-1):
            if location_row[i] != location_row[i+1]:
                self.location_indices.append(i+1)
        return self.location_indices

    def process_data(self):
        first_index = 1
        last_index = first_index + self.proc_data_row_length - 1

        while last_index < len(self.data_row):
            self.add_row(first_index, self.proc_data_row_length)
            # self.add_location_to_row(self.location_row)
            first_index += self.shift
            last_index += self.shift
        if last_index >= len(self.data_row):
            self.proc_data.append([])
            last_index -= self.shift

            # for i in range(len(data_row)-last_index):

    def add_row(self, first_index, length):
        self.proc_data.append([])
        for i in range(length):
            self.proc_data[-1].append(self.data_row[i + first_index])
        self.add_location()

    def add_location(self):
        self.proc_data[-1].append()
