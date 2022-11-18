from datetime import datetime
from os import listdir
from os.path import isfile, join
import shutil

oldPath = "/home/bernd/fluidflower/experiment/benchmarkdata/spatial_maps/csv-segmentations/c5/"
newPath = "/home/bernd/fluidflower/experiment/benchmarkdata/spatial_maps/run5/"

files = [f for f in listdir(oldPath) if isfile(join(oldPath, f))]
files.sort()

startTime = datetime.strptime(files[0][0:16], "%y%m%d_time%H%M%S")

for oldFileName in files:
    dtObject = datetime.strptime(oldFileName[0:16], "%y%m%d_time%H%M%S")

    delta = (dtObject - startTime)
    seconds = int(delta.total_seconds())

    newFileName = f"segmentation_{seconds:06d}s.csv"

    shutil.copyfile(oldPath + oldFileName, newPath + newFileName)
