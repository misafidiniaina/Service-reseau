import subprocess

import terminal


class Forward:
    __protocole = ''
    __sport = ''
    __dport = ''
    __intIn = ''
    __intOut = ''
    __source = ''
    __destination = ''
    __error: str = ''
    __success: str = ''

    def __init__(self, protocole, sport, dport, intIn, intOut, source, dest):
        self.__dport = dport
        self.__protocole = protocole
        self.__sport = sport
        self.__intOut = intOut
        self.__intIn = intIn
        self.__source = source
        self.__destination = dest

    def save(self, jump, place='A'):
        #  checker tous les attributs et s'ils ne sont pas "None", on les ajoute dans la commande à executer
        attr = {
            "-p": self.__protocole,
            "--sport": self.__sport,
            "--dport": self.__dport,
            "--destination": self.__destination,
            "-i": self.__intIn,
            "-o": self.__intOut,
            "--source": self.__source
        }
        argument = ""
        # louper à travers les attributs
        for key, value in attr.items():
            if value not in ("", "Toutes"):
                argument += f"{key} {value} "

        # Sauvegarder la commande
        commande = f"sudo iptables -{place} FORWARD {argument} -j {jump}"

        # execution de la commande
        resultat = subprocess.run(commande, capture_output=True, text=True, shell=True)

        if resultat.returncode == 0:
            self.__success = "Operation effectuée avec succès."
            return self.__success
        else:
            self.__error = resultat.stderr
            return self.__error
