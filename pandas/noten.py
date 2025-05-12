__author__ = "Felix Friesenbichler"
__license__ = "GPLv2"
__email__ = "1127@htl.rennweg.at"

import argparse
import pandas as pd


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="noten.py by Felix Friesenbichler / HTL Rennweg")

    parser.add_argument("outfile", help="Ausgabedatei (z.B. result.csv)")
    parser.add_argument("-n", help="csv-Datei mit den Noten")
    parser.add_argument("-s", help="xml-Datei mit den Schülerdaten")
    parser.add_argument("-m", default="Nummer", help="Felix Friesenbichlerum Verknüpfen (default = Nummer)")
    parser.add_argument("-f", help="Zu filternder Gegenstand (z.B. SEW)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Gibt die Daten auf der Kommandozeile aus")
    parser.add_argument("-q", "--quiet", action="store_true", help="Keine Textausgabe")

    return parser.parse_args()

if __name__ == "__main__":
    parse_args()
