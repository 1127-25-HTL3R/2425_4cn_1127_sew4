
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

from pathlib import Path
from collections import Counter

path = Path(input("Enter an absolute path: "))
ext = input("Enter a file extension: ")

print(Counter(pathd.suffix for pathd in Path.cwd().iterdir()))

for file in sorted(path.rglob(f"*.{ext}")):
    print(file.absolute().resolve())
