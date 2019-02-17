from pathlib import Path
import fileprocessing as fp
import datatransforming as dt


data_folder = Path('')
file = data_folder / 'StraightPipe_SingleDefect - Sheet1.csv'

data = fp.read_file(file)
dt.DataTransformation.init_locations(data[-1])
data1 = data[:-1]  # remove location data
sensors = {data1[i][0]: dt.DataTransformation(data1[i]) for i in range(len(data1))}

for s_name, s in sensors.items():
    s.process_data()
    s_data = s.final_data
    destination_file = data_folder / (s_name + '_PipeDefects_DataTransformation.csv')
    fp.write_file(destination_file, s_data)
