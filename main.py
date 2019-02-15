from pathlib import Path
import fileprocessing as fp
import datatransforming as dt

data_folder = Path('')
file = data_folder / 'StraightPipe_SingleDefect - Sheet1.csv'
# destination_file = data_folder / 'PipeDefects_DataTransformation.csv'
destination_file = data_folder / 'test.csv'

data = fp.read_file(file)

dt.DataTransformation.init_locations(data[-1])
a = dt.DataTransformation(data[0])
a.process_data()
data = a.final_data

fp.write_file(destination_file, data)
