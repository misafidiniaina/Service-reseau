import subprocess

import terminal


class Output:
    __protocole = ''
    __port = ''
    __destination = ''
    __intf = ''
    __jump = ''
    __error: str = ''
    __success: str = ''

    def __init__(self, protocole, port, destination, intf):
        super().__init__()
        self.__protocole = protocole
        self.__port = port
        self.__destination = destination
        self.__intf = intf

    def save(self, jump, place='A'):
        #  checker tous les attributs et s'ils ne sont pas "None", on les ajoute dans la commande à executer
        attr = {
            "-p": self.__protocole,
            "--sport": self.__port,
            "-s": self.__destination,
            "-o": self.__intf
        }
        argument = ""
        # louper à travers les attributs
        for key, value in attr.items():
            if value != '':
                argument += f"{key} {value} "

        # Sauvegarder la commande
        commande = f"sudo iptables -{place} OUTPUT {argument} -j {jump}"
        
        # execution de la commande
        resultat = subprocess.run(commande, capture_output=True, text=True, shell=True)

        if resultat.returncode == 0:
            self.__success = "Operation effectuée avec succès."
            return self.__success
        else:
            self.__error = resultat.stderr
            return self.__error

        

