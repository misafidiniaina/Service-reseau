import subprocess

import terminal


class Forward:
    __protocole = None
    __sport = None
    __dport = None
    __intIn = None
    __intOut = None
    __source = None
    __destination = None
    __error: str = None
    __success: str = None

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
            if value is not None:
                argument += f"{key} {value} "

        # Sauvegarder la commande
        commande = f"iptables -{place} FORWARD {argument} -j {jump}"

        # execution de la commande
        resultat = terminal.command_line(commande)

        if resultat.stdout:
            self.__success = "Operation effectuée avec succès."
            return self.__success
        else:
            self.__error = resultat.stderr
            return self.__error
