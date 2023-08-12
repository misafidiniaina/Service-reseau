import subprocess


class Input:
    __protocole = None
    __port = None
    __source = None
    __intf = None
    __jump = None
    __error: str = None
    __success: str = None

    def __init__(self, protocole, port, source, intf):
        super().__init__()
        self.__protocole = protocole
        self.__port = port
        self.__source = source
        self.__intf = intf

    def save(self, jump, place='A') -> str:
        #  checker tous les attributs et s'ils ne sont pas "None", on les ajoute dans la commande à executer
        attr = {
            "-p": self.__protocole,
            "--sport": self.__port,
            "-s": self.__source,
            "-i": self.__intf
        }
        argument = ""
        # louper à travers les attributs
        for key, value in attr.items():
            if value is not None:
                argument += f"{key} {value} "

        # Sauvegarder la commande
        commande = f"iptables -{place} INPUT {argument} -j {jump}"

        # execution de la commande
        resultat = subprocess.run(commande, capture_output=True, text=True, shell=True)

        if resultat.stdout:
            self.__success = "Operation effectuée avec succès."
            return self.__success
        else:
            self.__error = resultat.stderr
            return self.__error
