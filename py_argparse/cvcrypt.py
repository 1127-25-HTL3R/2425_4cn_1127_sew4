__author__ = "Felix Friesenbichler"
__emaiL__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

import argparse
import sys
from pathlib import Path

sys.path.insert(0, "../kasiski")
from kasiski import Caesar, Vigenere


def process_file(infile: str, outfile: str, cipher: str, key: str, decrypt: bool, verbose: bool):
    """
    Reads input file, processes it with the selected cipher, and writes output file.

    :param infile:
    :param outfile:
    :param cipher:
    :param key:
    :param bool:
    :param verbose:
    """

    input_path = Path(infile)

    if not input_path.is_file():
        print(f"{infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)

    with open(infile, "r", encoding="utf-8") as f:
        text = f.read()

    if cipher in ["caesar", "c"]:
        cipher_instance = Caesar()
    elif cipher in ["vigenere", "v"]:
        cipher_instance = Vigenere()
    else:
        print("Invalid cipher. Use 'caesar' or 'vigenere'.", file=sys.stderr)
        sys.exit(1)

    result = cipher_instance.decrypt(text, key) if decrypt else cipher_instance.encrypt(text, key)

    if verbose:
        action = "Decrypting" if decrypt else "Encrypting"
        print(f"{action} {cipher.capitalize()} with key = {key} from file {infile} into file {outfile}")

    with open(outfile, "w", encoding="utf-8") as f:
        f.write(result)


def parse_args():
    """
    Parse command-line arguments using argparse.
    """
    parser = argparse.ArgumentParser(description="Caesar & Vigenere encrypter / decrypter by 1127 / HTL Rennweg")
    parser.add_argument("infile", type=str, help="Zu verschlüsselnde Datei")
    parser.add_argument("outfile", type=str, help="Zieldatei")
    parser.add_argument("-c", "--cipher", choices=["caesar", "c", "vigenere", "v"], required=True, help="Zu verwendende Chiffre")
    parser.add_argument("-k", "--key", type=str, required=True, help="Encryption-Key")
    parser.add_argument("-e", "--encrypt", action="store_true")
    parser.add_argument("-d", "--decrypt", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()

    if args.encrypt == args.decrypt:
        print("Either --encrypt or --decrypt must be specified.", file=sys.stderr)
        sys.exit(1)

    return args

if __name__ == "__main__":
    args = parse_args()
    process_file(args.infile, args.outfile, args.cipher, args.key, args.decrypt, args.verbose)
