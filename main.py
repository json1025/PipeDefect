from pathlib import Path
import fileprocessing as fp
import datatransforming as dp

data_folder = Path('C:/Users/Jason/Desktop/School/Methacton/Science Fair/12th Grade/PipeDefect')
file = data_folder / 'StraightPipe_SingleDefect - Sheet1.csv'
destination_file = data_folder / 'PipeDefects_DataTransformation.csv'

data = fp.read_file(file)
dp.DataTransformation.initialize_location_indices(data[-1])
fp.write_file(destination_file, data)
