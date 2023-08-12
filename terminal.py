import subprocess
from regle import Regle
import re


def get_protocol(file_path: str = '/etc/services') -> dict:
    """
    cette fonction retourne les Services et ports disponibles dans un système d'exploitation Linux
    :param file_path: chemin vers le fichier contenant les services
    :return:
    """
    protocole_list_file_path = 'protocole_list_file.txt'

    # effacer tous les commentaires dans le fichier d'origine
    with open(file_path, 'r') as file, open(protocole_list_file_path, 'w') as protocole_list_file:
        for line in file:
            #  Trouver l'index du '#' dans la ligne
            index = line.find('#')

            # Si '#' est trouvé, Garder la partie avant le '#' et écrire dans le nouveau fichier
            if index != -1:
                new_line = line[:index] + '\n'
                protocole_list_file.write(new_line)
            else:
                protocole_list_file.write(line)

    protocole = dict(tcp={}, udp={})
    with open(protocole_list_file_path, 'r') as file:
        for line in file:
            if line == '\n':
                continue

            # boucler dans chaque ligne qui est désormais un liste
            # si on trouve une '' (vide), on le suprimme du liste
            list_line = line.strip().split('\t')
            for word in list_line:
                if word == '':
                    list_line.remove(word)
                    continue

            #  list_line ne contient plus maintenant que [0]: nom de port, [1]: numéro de port/protocole
            # separer le mot contenant '/' en deux mots
            if len(list_line) >= 2:
                num_et_prot = list_line[1].split('/')  # => ['21', 'tcp']
                nom_port = list_line[0]

            # raha vao iray iany ny ao de mila zaraina par ' ' fa tsy hitany nom de port sy numero de port ary protocole
            if len(list_line) == 1:
                list_line = list_line[0].split(' ')
                num_et_prot = list_line[1].split('/')  # => ['21', 'tcp']
                nom_port = list_line[0]

            # Identifier le protocol
            if num_et_prot[1] == 'udp':
                protocole['udp'][nom_port] = num_et_prot[0]
            if num_et_prot[1] == 'tcp':
                protocole['tcp'][nom_port] = num_et_prot[0]

    return protocole


def command_line(command: str, arg: str = None):
    # execution de la commande
    if arg is not None:
        resultat = subprocess.run(f"{command} {arg}", capture_output=True, text=True, shell=True)
    else:
        resultat = subprocess.run(command, capture_output=True, text=True, shell=True)

    return resultat.stdout


def get_rule(path_to_file: str) -> list:
    list_rule = []

   
    # ouvrir le fichier list_rule.txt
    with open(path_to_file, "r") as file:
        # on ne doit prendre que trois blocs de tableau dans le fichier, INPUT, OUTPUT, FORWARD
        i = 0  # 0: INPUT   1: FORWARD, 2: OUTPUT

        # un repère j sera necessaire pour se situer dans la boucle
        j = 0
        # boucler à travers les lignes du fichier
        for line in file:
            if line != '\n':
                # Utilise une expression régulière pour remplacer les espaces/tabulations consécutifs par un seul espace
                line = re.sub(r'\s+', ' ', line)
                # Retire les espaces/tabulations au début et à la fin de la chaîne
                line = line.strip()
                # convertir la ligne par une liste si elle commence par un entier
                if line[0].isdigit():
                    # diviser la ligne en liste et si la longueur de la liste est 6, on ajoute le caractere ' ' 
                    line_to_list = line.split(' ')
                    if len(line_to_list) == 6:
                        line_to_list.append(" ")
                    
                    num = int(line_to_list[0])
                    # eu début on est dans la partie input:0
                    if i == 0:  # cette condition est uniquement fausse si j n'est pas inferieur à num
                        #                     ce qui veut dire, on passe à la CHAIN suivant, qui est forward avec i == 1
                        if j < num:
                            regle = Regle("input", num, line_to_list[1], line_to_list[2], line_to_list[3],
                                          line_to_list[4], line_to_list[5], line_to_list[6])
                            j = num
                            # ajouter les listes dans la liste de reglement
                            list_rule.append(regle)
                            continue
                        else:
                            j = 0
                            i += 1

                    if i == 1:
                        if j < num:
                            regle = Regle("forward", num, line_to_list[1], line_to_list[2], line_to_list[3],
                                          line_to_list[4], line_to_list[5], line_to_list[6])
                            j = num
                            # ajouter les listes dans la liste de reglement
                            list_rule.append(regle)
                            continue
                        else:
                            i += 1
                            j = 0

                    if i == 2:
                        if j < num:
                            regle = Regle("output", num, line_to_list[1], line_to_list[2], line_to_list[3],
                                          line_to_list[4], line_to_list[5], line_to_list[6])
                            j = num
                            # ajouter les listes dans la liste de reglement
                            list_rule.append(regle)
                        else:
                            i += 1

                #  on ignore si la ligne ne commence pas par 'Chain' et un chiffre
                if not ('Chain' in line or type(line[0]) == int):
                    continue

    return list_rule


def get_link_interface() -> list:
    """
    cette fonction retourne les interfaces réseaux disponibles dans un système Linux
    :return: liste des interfaces
    """
    resultat = subprocess.run("ip -o link show up | awk -F': ' '{print $2}'", capture_output=True, text=True,
                              shell=True)
    interface = re.sub(r'\s+', ' ', resultat.stdout)
    list_intf = interface.split(" ")
    return list_intf

def update_file():
    """
     mise à jour de la règles 
    """
     # lancer la commande de listage des règles dans le système
    subprocess.run("sudo iptables -t filter -L --line-numbers > liste_rule.txt", text=True, capture_output=True, shell=True)
    return get_rule("liste_rule.txt")