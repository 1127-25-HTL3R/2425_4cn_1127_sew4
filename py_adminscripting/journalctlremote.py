
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

#
# Beantwortung der Fragen:
#
# -) Welche Dateien werden erzeugt - wie lautet deren absoluter Pfad?
# -> ~/.ssh/key
# -> ~/.ssh/key.pub
# ---
# -) Welche zusätzlichen Informationen werden angezeigt?
# -> Schlüsselspeicherort, Fingerprint und eine graphische Repräsentation des
#    Schlüssels
# ---
# -) Welche Daten werden kopiert?
# -> ~/.ssh/key.pub wird an ~/.ssh/authorized_keys @ remote angehängt.
# ---
# -) Warum darf der private-key die eigene Maschine nie verlassen?
# -> Weil sonst die Identität vorgetäuscht werden könnte.
# ---
# -) Wird nach erneuter Verbindung nach einem Passwort gefragt?
# -> Nein.
# ---
# -) Warum gilt die Authentifizuerung mittels Schlüsselpaar als sicherer, als ein Login mittels herkömmlicher Passwörter?
# -> Ein Schlüsselpaar wird schwerer gebrochen.

import paramiko
import getpass

def fetch_journal_logs(remote_host: str, username: str, key_file: str, minutes: int) -> None:
    command = f'journalctl --since "-{minutes} minutes"'

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(remote_host, username=username, key_filename=key_file)

        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())

        client.close()
    except Exception as e:
        print(f"Fehler bei der Verbindung: {e}")

if __name__ == "__main__":
    remote_host = "192.168.1.100"  # Hier die Server-IP hardcoden
    username = "junioradmin"
    key_file = getpass.getpass("Pfad zum privaten SSH-Schlüssel: ")

    try:
        minutes = int(input("Geben Sie die Anzahl der Minuten ein: "))
        fetch_journal_logs(remote_host, username, key_file, minutes)
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
