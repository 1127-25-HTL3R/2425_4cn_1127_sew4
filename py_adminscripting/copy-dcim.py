
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

from pathlib import Path
from shutil import copy as shcopy
import re

source_path = Path(input("Pleae enter the source directory: "))
destination_path = Path(input("Pleae enter the destination directory: "))


for file in sorted(source_path.glob("*.jpg")):
    name = file.name
    year = name[:4]
    month = name[4:6]
    day = name[6:8]

    if re.compile(r'^\d*_\d*').search(name):

        full_path = Path.joinpath(destination_path, year, month, day)

        if not full_path.exists():
            full_path.mkdir(parents=True)

    shcopy(file, full_path)
