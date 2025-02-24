
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

from pathlib import Path

print("-----------------------------------")
absolute_path = Path(input("Enter the absolute path of a file: "))
print("-----------------------------------")

print(f"Der Dateiname ohne Verzeichnis: {absolute_path.name}")
print(f"Der Dateiname ohne die Dateierweiterung: {absolute_path.stem}")
print(f"Die Dateierweiterung: {absolute_path.suffix}")
print(f"Der Dateiname ohne Verzeichnis: {absolute_path.anchor}")
print(f"Das Dateiverzeichnis, das die Datei enthält bzw. das übergeordnete Verzeichnis: {absolute_path.parent}")


if absolute_path.parent == absolute_path.parent.parent:
    print("Parent directory does not exist")
else:
    print(absolute_path.parent.parent)
