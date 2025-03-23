__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license = "GPLv2"

import argparse
import sys
from pathlib import Path

sys.path.insert(0, "../kasiski")
from kasiski import Caesar, Kasiski


def crack_file(infile: str, cipher: str, verbose: bool):
    """
    Attempts to crack an encrypted file and determine the most likely key.
    """
    input_path = Path(infile)

    if not input_path.is_file():
        print(f"{infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)

    with open(infile, "r", encoding="utf-8") as f:
        text = f.read()

    if cipher in ["caesar", "c"]:
        caesar = Caesar()
        probable_keys = caesar.crack(text, 1)
        key = probable_keys[0] if probable_keys else "Unknown"

    elif cipher in ["vigenere", "v"]:
        kasiski = Kasiski(text)
        probable_lengths = Kasiski.dist_n_list(text, 3)

        if probable_lengths:
            key_length = probable_lengths[0]
            key = kasiski.crack_key(key_length)
        else:
            key = "Unknown"
    else:
        print("Invalid cipher. Use 'caesar' or 'vigenere'", file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f"Cracking {cipher.capitalize()}-encrypted file {infile}: Key = {key}")
    else:
        print(key)

    def parse_args():
        """
        Parse command-line arguments using arpgarse.
        """
        parser = argparse.ArgumentParser(description="Crack caesar or Vigenère encrypted files.")
        parser.add_argument("infile", type=str, help="Input file to crack")
        parser.add_argument("-c", "--cipher", choices=["caesar", "-c", "vigenere", "v"], required=True, help="Cipher type")
        parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed cracking process")
        parser.add_argument("-q", "--quiet", action="store_true", help="Only output the cracked key")

        args = parser.parse_args()
        return args

if __name__ == "__main__":
    args = parse_args()
    crack_file(args.infile, args.cipher, args.verbose)
