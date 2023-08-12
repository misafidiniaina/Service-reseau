import customtkinter as ctk
import champ_personnaliser as chmPers
import time
from forward import *
from input import *
from output import *
from regle import *
from terminal import *

fenetre = ctk.CTk()
fenetre.geometry("800x500")
fenetre.minsize(height=550,width=600)
global Rule_list
"""def remplie_tab(liste_regle:list):
    for rule in liste_regle:
        if rule.chain == "input":
            contents_Input.append([rule.num,rule.target,rule.protocol,rule.option,rule.source,rule.destination, rule.etat])
        elif rule.chain == "output":
            contents_Output.append([rule.num,rule.target,rule.protocol,rule.option,rule.source,rule.destination, rule.etat])
        else:
            contents_forward.append([rule.num,rule.target,rule.protocol,rule.option,rule.source,rule.destination, rule.etat])
"""
def move_next_page():
    global cont
    buton2.configure(corner_radius=0,fg_color="#1a232e",border_color="white",border_width=0,text_color="white")
    buton1.configure(corner_radius=0,fg_color="transparent",border_color="#1a232e",border_width=0,text_color="black")
    if not cont > len(pages) - 2:
        for p in pages:
            p.pack_forget()
        cont +=1
        page = pages[cont]
        page.pack(fill=ctk.BOTH,expand=True,pady=10)
    rule_list = update_file()
    #remplie_tab(rule_list)
    
    for rule in rule_list:
        if rule.chain == "input":
            contents_Input.append([rule.num,rule.target,rule.protocol,rule.option,rule.source,rule.destination, rule.etat])
        elif rule.chain == "output":
            contents_Output.append([rule.num,rule.target,rule.protocol,rule.option,rule.source,rule.destination, rule.etat])
        else:
            contents_forward.append([rule.num,rule.target,rule.protocol,rule.option,rule.source,rule.destination, rule.etat])
    #tableau_Input.clean()
    tableau_Input.affiche(contents_Input)
    tableau_Output.affiche(contents_Output)
    tableau_forward.affiche(contents_forward)
    contents_Input.clear()
    contents_Output.clear()
    contents_forward.clear()
    #fenetre.update()

  
def move_back_page():
    buton1.configure(corner_radius=0,fg_color="#1a232e",border_color="white",border_width=0,text_color="white")
    buton2.configure(corner_radius=0,fg_color="transparent",border_color="#1a232e",border_width=0,text_color="black")

    global cont
    if not cont == 0:
        for p in pages:
            p.pack_forget()
        cont -=1
        page = pages[cont]
        page.pack(fill=ctk.BOTH,expand=True,pady=10)
    tableau_Input.clean()
    tableau_Output.clean()
    tableau_forward.clean()

def validate_entry(action, value_if_allowed):
    if action == '0':  # Suppression de texte
        return True
    if value_if_allowed.isdigit() and 0 <= int(value_if_allowed) <= 255 and len(value_if_allowed) <= 3 and value_if_allowed != '00':
        return True
    else:
        return False

#navigation
nav = ctk.CTkFrame(fenetre,fg_color="#c4eaee",corner_radius=0)
buton1=ctk.CTkButton(nav,text=" Nouvelle règle ",command=move_back_page,corner_radius=0,fg_color="#1a232e",border_color="white",border_width=0,text_color="white")
buton1.pack(side=ctk.LEFT,padx=2,ipady=5,ipadx=5)

buton2=ctk.CTkButton(nav,text=" Liste des règles ", corner_radius=0,fg_color="transparent", command=move_next_page, border_color="#1a232e",border_width=0,text_color="black")
buton2.pack(side=ctk.LEFT,padx=2,ipady=5,ipadx=5)

nav.pack(side=ctk.TOP,fill=ctk.X,pady=1)


#contenu du logiciel
main_frame=ctk.CTkFrame(fenetre,fg_color="#1a232e")

#premier page
page1=ctk.CTkFrame(main_frame,fg_color="transparent")



titre = ctk.CTkFrame(page1,corner_radius=0,fg_color="transparent")
titre_label = ctk.CTkLabel(titre,text="Par-feu personnalisé",font=("arial",20),text_color="#2ca089")
titre_label.pack(pady=0)
titre.pack(fill=ctk.X)


input_frame = ctk.CTkFrame(page1,fg_color="transparent")

Chain_tab = ctk.CTkTabview(input_frame,segmented_button_fg_color='#1a232f',fg_color='#16181D',width=50)
Input_tab = Chain_tab.add("  Entrant  ")
Output_tab = Chain_tab.add("  Sortant  ")
Forward_tab = Chain_tab.add("  Passant  ")
Chain_tab.set("  Entrant  ")
Chain_tab.pack(fill=ctk.BOTH,expand=True,side=ctk.BOTTOM)


#composant de la chaine INPUT
Input_chain_composant = ctk.CTkFrame(Input_tab,fg_color="transparent")

champ2=ctk.CTkFrame(Input_chain_composant,fg_color="transparent",)
label2=ctk.CTkLabel(champ2,text="Adresse IP source:               ")
label2.pack(side=ctk.LEFT)
ip_source_input = chmPers.ttt(champ2,fenetre)
ip_source_input.ip_input()
champ2.pack(fill=ctk.X,pady=10,padx=30)

champ4 = ctk.CTkFrame(Input_chain_composant,fg_color='transparent')
label4=ctk.CTkLabel(champ4,text="Interface :                                   ")
label4.pack(side=ctk.LEFT)
liste_interface = get_link_interface()
interface_Input_chain = ctk.CTkComboBox(champ4,values=liste_interface,width=100)
interface_Input_chain.configure(state='readonly')
interface_Input_chain.pack(side=ctk.LEFT)
champ4.pack(fill=ctk.BOTH,pady=10,padx=30)

champ3 = ctk.CTkFrame(Input_chain_composant,fg_color="transparent")
label5 = ctk.CTkLabel(champ3,text="Protocole:                                   ")
label5.pack(side=ctk.LEFT)
protocole_input_chain=ctk.CTkComboBox(champ3,values=["TCP","UDP","TCP/UDP"],width=100)
protocole_input_chain.configure(state='readonly')
protocole_input_chain.pack(side=ctk.LEFT)
label3 = ctk.CTkLabel(champ3,text="       Port:      ")
label3.pack(side=ctk.LEFT)
sport = ctk.CTkEntry(champ3,width=50)
sport.pack(side=ctk.LEFT)
champ3.pack(fill=ctk.X,pady=10,padx=30)

champ6 = ctk.CTkFrame(Input_chain_composant,fg_color="transparent")
label6 = ctk.CTkLabel(champ6,text="Action à faire:                            ")
label6.pack(side=ctk.LEFT)
action_input_chain= ctk.StringVar()
action_option_1 = ctk.CTkRadioButton(champ6,text="Accepter" , variable=action_input_chain, value="ACCEPT")
action_option_1.pack(side=ctk.LEFT)
action_option_2 = ctk.CTkRadioButton(champ6,text="Réfuser" , variable=action_input_chain, value="DROP")
action_option_2.pack(side=ctk.LEFT)
action_option_3 = ctk.CTkRadioButton(champ6,text="Rejeter", variable=action_input_chain, value="REJECT")
action_option_3.pack(side=ctk.LEFT)
champ6.pack(fill=ctk.X,pady=10,padx=30)

Input_chain_composant.pack(pady=10) 
input_frame.pack(fill=ctk.BOTH,expand=True,padx=20,pady=5)
bouton_Input_chain_frame = ctk.CTkFrame(Input_tab,fg_color="transparent")
bouton = ctk.CTkFrame(bouton_Input_chain_frame,fg_color="transparent")              #**************
def get_data_input():                                                               #**************
    port = sport.get()                                                              #**************
    protocol = protocole_input_chain.get()                                          #**************        
    action_ = action_input_chain.get()                                              #**************
    ip_source_ = ip_source_input._get_ip()                                          
    interface = interface_Input_chain.get()
    input = Input(protocol,port,ip_source_,interface)
    print(input.save(action_))

    

bouton_ok_INPUT = ctk.CTkButton(bouton,
    text="Ok",                      
    width=50,
    height=35,
    fg_color="#2ca089",
    command=get_data_input
)
bouton_ok_INPUT.pack(side=ctk.RIGHT,padx=5)
def annuler_input():
    sport.delete(0,"end")
    ip_source_input._set_empty()
    ip_source_input._set_focus()

bouton_annuler_INPUT = ctk.CTkButton(bouton,
    text="Annuler",
    width=80,
    fg_color="transparent",
    text_color="#2ca089",
    border_width=2,
    border_color="#2ca089",
    hover_color="#16202c",
    height=35,
    command=annuler_input
)
bouton_annuler_INPUT.pack(side=ctk.RIGHT,padx=5)

bouton.pack(side=ctk.RIGHT,padx=20,pady=10)
bouton_Input_chain_frame.pack(side=ctk.BOTTOM,fill=ctk.X,pady=5,padx=5,ipady=10,)

#composant de la chaine OUTPUT
Output_chain_composant = ctk.CTkFrame(Output_tab,fg_color="transparent")

champ2=ctk.CTkFrame(Output_chain_composant,fg_color="transparent",)
label2=ctk.CTkLabel(champ2,text="Adresse IP de déstination: ")
label2.pack(side=ctk.LEFT)
ip_destination_output = chmPers.ttt(champ2,fenetre)
ip_destination_output.ip_input()
champ2.pack(fill=ctk.X,pady=10,padx=30)

champ4 = ctk.CTkFrame(Output_chain_composant,fg_color='transparent')
label4=ctk.CTkLabel(champ4,text="Interface :                                   ")
label4.pack(side=ctk.LEFT)
interface_Output_chain = ctk.CTkComboBox(champ4,values=liste_interface,width=100)
interface_Output_chain.configure(state='readonly')
interface_Output_chain.pack(side=ctk.LEFT)
champ4.pack(fill=ctk.BOTH,pady=10,padx=30)

champ3 = ctk.CTkFrame(Output_chain_composant,fg_color="transparent")
label5 = ctk.CTkLabel(champ3,text="Protocole:                                   ")
label5.pack(side=ctk.LEFT)
protocole=ctk.CTkComboBox(champ3,values=["TCP","UDP","TCP/UDP"],width=100)
protocole.configure(state='readonly')
protocole.pack(side=ctk.LEFT)
label3 = ctk.CTkLabel(champ3,text="       Port:      ")
label3.pack(side=ctk.LEFT)
dport = ctk.CTkEntry(champ3,width=50)
dport.pack(side=ctk.LEFT)
champ3.pack(fill=ctk.X,pady=10,padx=30)

champ6 = ctk.CTkFrame(Output_chain_composant,fg_color="transparent")
label6 = ctk.CTkLabel(champ6,text="Action à faire:                            ")
label6.pack(side=ctk.LEFT)
action_output_chain= ctk.StringVar()
action_option_1 = ctk.CTkRadioButton(champ6,text="Accepter" , variable=action_output_chain, value="ACCEPT")
action_option_1.pack(side=ctk.LEFT)
action_option_2 = ctk.CTkRadioButton(champ6,text="Réfuser" , variable=action_output_chain, value="DROP")
action_option_2.pack(side=ctk.LEFT)
action_option_3 = ctk.CTkRadioButton(champ6,text="Rejeter", variable=action_output_chain, value="REJECT")
action_option_3.pack(side=ctk.LEFT)
champ6.pack(fill=ctk.X,pady=10,padx=30)

Output_chain_composant.pack(pady=10) 
input_frame.pack(fill=ctk.BOTH,expand=True)
bouton_Output_chain_frame = ctk.CTkFrame(Output_tab,fg_color="transparent")
bouton = ctk.CTkFrame(bouton_Output_chain_frame,fg_color="transparent")
def yes():
    port_s = dport.get()
    protocol = protocole.get()
    action_ = action_output_chain.get()
    ip_dest = ip_destination_output._get_ip()
    interface = interface_Output_chain.get()
    print("port source : "+port_s)
    print("portocole : "+protocol)
    print("action à faire : "+action_)
    print("ip de destination:"+ip_dest)
    print("interface :"+interface)
    output = Output(protocol,port_s,ip_dest,interface)
    output.save(action_)

bouton_ok_OUTPUT = ctk.CTkButton(bouton,
    text="Ok",                      
    width=50,
    height=35,
    fg_color="#2ca089",
    command=yes
)
bouton_ok_OUTPUT.pack(side=ctk.RIGHT,padx=5)
def annuler_output():
    dport.delete(0,"end")
    ip_destination_output._set_empty()
    ip_destination_output._set_focus()

bouton_annuler_OUTPUT = ctk.CTkButton(bouton,
    text="Annuler",
    width=80,
    fg_color="transparent",
    text_color="#2ca089",
    border_width=2,
    border_color="#2ca089",
    hover_color="#16202c",
    height=35,
    command=annuler_output
)
bouton_annuler_OUTPUT.pack(side=ctk.RIGHT,padx=5)

bouton.pack(side=ctk.RIGHT,padx=20,pady=10)
bouton_Output_chain_frame.pack(side=ctk.BOTTOM,fill=ctk.X,pady=5,padx=5,ipady=10,)

#composont de la chaine forward
Forward_chain_composant = ctk.CTkFrame(Forward_tab,fg_color="transparent")

champ2=ctk.CTkFrame(Forward_chain_composant,fg_color="transparent",)
label2=ctk.CTkLabel(champ2,text="Adresse IP source:               ")
label2.pack(side=ctk.LEFT)
ip_source = chmPers.ttt(champ2,fenetre)
ip_source.ip_input()
champ2.pack(fill=ctk.X,pady=10,padx=30)

champ1=ctk.CTkFrame(Forward_chain_composant,fg_color="transparent")
label1=ctk.CTkLabel(champ1,text="Adresse IP de déstination: ")
label1.pack(side=ctk.LEFT)
ip_destination = chmPers.ttt(champ1,fenetre)
ip_destination.ip_input()
champ1.pack(fill=ctk.X,pady=10,padx=30)

champ4 = ctk.CTkFrame(Forward_chain_composant,fg_color='transparent')
label4=ctk.CTkLabel(champ4,text="Interface d'entrée                    ")
label4.pack(side=ctk.LEFT)
interface_entrer_chain = ctk.CTkComboBox(champ4,values=liste_interface,width=100)
interface_entrer_chain.configure(state='readonly')
interface_entrer_chain.pack(side=ctk.LEFT)
label4=ctk.CTkLabel(champ4,text="      Interface de sortie:      ")
label4.pack(side=ctk.LEFT)
interface_sortie_chain = ctk.CTkComboBox(champ4,values=liste_interface,width=100)
interface_sortie_chain.configure(state='readonly')
interface_sortie_chain.pack(side=ctk.LEFT)
champ4.pack(fill=ctk.BOTH,pady=10,padx=30)

champ3 = ctk.CTkFrame(Forward_chain_composant,fg_color="transparent")
label5 = ctk.CTkLabel(champ3,text="Protocole:                                   ")
label5.pack(side=ctk.LEFT)
protocole=ctk.CTkComboBox(champ3,values=["TCP","UDP","TCP/UDP"],width=100)
protocole.configure(state='readonly')
protocole.pack(side=ctk.LEFT)

champ3.pack(fill=ctk.X,pady=10,padx=30)

champ7 = ctk.CTkFrame(Forward_chain_composant,fg_color="transparent")
label3 = ctk.CTkLabel(champ7,text="Port d'entréé:                             ")
label3.pack(side=ctk.LEFT)
inport = ctk.CTkEntry(champ7,width=50)
inport.pack(side=ctk.LEFT)
label3 = ctk.CTkLabel(champ7,text="       Port de sortie:   ")
label3.pack(side=ctk.LEFT)
outport = ctk.CTkEntry(champ7,width=50)
outport.pack(side=ctk.LEFT)
champ7.pack(fill=ctk.X,pady=10,padx=30)

champ6 = ctk.CTkFrame(Forward_chain_composant,fg_color="transparent")
label6 = ctk.CTkLabel(champ6,text="Action à faire:                            ")
label6.pack(side=ctk.LEFT)
action= ctk.StringVar()
action_option_1 = ctk.CTkRadioButton(champ6,text="Accepter" , variable=action, value="ACCEPT")
action_option_1.pack(side=ctk.LEFT)
action_option_2 = ctk.CTkRadioButton(champ6,text="Réfuser" , variable=action, value="DROP")
action_option_2.pack(side=ctk.LEFT)
action_option_3 = ctk.CTkRadioButton(champ6,text="Rejeter", variable=action, value="REJECT")
action_option_3.pack(side=ctk.LEFT)
champ6.pack(fill=ctk.X,pady=10,padx=30)

bouton_Input_chain_frame = ctk.CTkFrame(Forward_tab,fg_color="transparent")
bouton = ctk.CTkFrame(bouton_Input_chain_frame,fg_color="transparent")
def yes():
    port_s = sport.get()
    port_d = dport.get()
    INint = interface_entrer_chain.get()
    Outint = interface_sortie_chain.get()
    protocol = protocole.get()
    action_ = action.get()
    ip_d = ip_destination._get_ip()
    ip_s = ip_source._get_ip()

    print("ip resource:"+ip_s)
    print("ip de destination:"+ip_d)
    print("port source : "+port_s)
    print("port destination:"+port_d)
    print("portocole : "+protocol)
    print("action à faire : "+action_)
    print("interface d'entree:"+INint)
    print("interface de sortie:"+Outint)
    

bouton_ok_FORWARD = ctk.CTkButton(bouton,
    text="Ok",                      
    width=50,
    height=35,
    fg_color="#2ca089",
    command=yes
)

bouton_ok_FORWARD.pack(side=ctk.RIGHT,padx=5)

def annuler_forward():
    sport.delete(0,"end")
    dport.delete(0,"end")
    ip_destination._set_empty()
    ip_source._set_empty()
    ip_source._set_focus()

bouton_annuler_FORWARD = ctk.CTkButton(bouton,
    text="Annuler",
    width=80,
    fg_color="transparent",
    text_color="#2ca089",
    border_width=2,
    border_color="#2ca089",
    hover_color="#16202c",
    height=35,
    command=annuler_forward
)
bouton_annuler_FORWARD.pack(side=ctk.RIGHT,padx=5)

bouton.pack(side=ctk.RIGHT,padx=20,pady=10)
bouton_Input_chain_frame.pack(side=ctk.BOTTOM,fill=ctk.X,pady=5,padx=5,ipady=10,)

Forward_chain_composant.pack(pady=10) 


page1.pack(fill=ctk.BOTH,expand=True,pady=10)

#deuxième page
page2=ctk.CTkFrame(main_frame,fg_color="transparent",corner_radius=0)
def toggle_widget(widget):
    if widget.winfo_ismapped():
        widget.pack_forget()  # Pour cacher le widget
    else:
        widget.pack(fill=ctk.BOTH)  # Pour afficher le widget
 
def input_clicked(): #fonction qui agit si on veut voir la liste de INPUT
    toggle_widget(I_list)

def output_clicked(): #fonction qui agit sin on veut voir la liste de OUTPUT
    toggle_widget(O_list)

def forward_clicked(): #fonction qui agit si on veut voir la liste de FORWARD
    toggle_widget(F_list)
contents_Input = []
contents_Output = []
contents_forward = [] 
Rule_list = get_rule("liste_rule.txt")                                                                    #exmple


    
bouton_liste_frame = ctk.CTkFrame(page2,fg_color="transparent")
delete_btn = ctk.CTkButton(bouton_liste_frame,text="Supprimer",state=ctk.DISABLED,text_color_disabled="gray")
Liste_regle_frame = ctk.CTkScrollableFrame(page2,fg_color="transparent") #frame principale pour les liste accordion
input_LFrame = ctk.CTkFrame(Liste_regle_frame,fg_color="transparent")#frame pour la liste des input
I_title_frame = ctk.CTkFrame(input_LFrame,fg_color="transparent")#frame contenant le titre INPUT
I_title_frame.pack(fill=ctk.X,pady=5,padx=5)
title_input = ctk.CTkButton(I_title_frame,command=input_clicked,corner_radius=0,text=" Entrant (INPUT) ")#titre clicable pour la liste INPUT
title_input.pack(side=ctk.LEFT)
I_puce = ctk.CTkLabel(I_title_frame)
#I_puce.pack()
#****
I_list = ctk.CTkFrame(input_LFrame)#contenu de la liste INPUT 

tableau_Input = chmPers.tableau(I_list,delete_btn) #utilisation de la classe tableau pour afficher les données INPUT
#***
input_LFrame.pack(fill=ctk.BOTH,padx=10,pady=10)

output_LFrame = ctk.CTkFrame(Liste_regle_frame,fg_color="transparent")#frame pour la liste des output
O_title_frame = ctk.CTkFrame(output_LFrame,fg_color="transparent")#frame contenant le titre OUTPUT
O_title_frame.pack(fill=ctk.X,pady=5,padx=5)
title_output = ctk.CTkButton(O_title_frame,command=output_clicked,corner_radius=0,text=" Sortant (OUTPUT) ")#titre clicable pour la liste OUTPUT
title_output.pack(side=ctk.LEFT)
#***
O_list = ctk.CTkFrame(output_LFrame)#utilisation de la classe tableau pour afficher les données pour OUTPUT
tableau_Output = chmPers.tableau(O_list,delete_btn)
#tableau_Output.affiche()
#***
output_LFrame.pack(fill=ctk.BOTH,padx=10,pady=10)

forward_LFrame = ctk.CTkFrame(Liste_regle_frame,fg_color="transparent")#frame pour la liste des forward
F_title_frame = ctk.CTkFrame(forward_LFrame,fg_color='transparent')#frame contenant le titre FORWARD
F_title_frame.pack(fill=ctk.X,pady=5,padx=5)
title_forward = ctk.CTkButton(F_title_frame,command=forward_clicked,corner_radius=0,text=" Passant (FORWARD) ")#titre clicable pour la liste FORWARD
title_forward.pack(side=ctk.LEFT)
#***
F_list = ctk.CTkFrame(forward_LFrame) #utilisation de la classe tableau pour afficher les données pour FORWARD
tableau_forward = chmPers.tableau(F_list,delete_btn)
#tableau_forward.affiche()
forward_LFrame.pack(fill=ctk.BOTH,padx=10,pady=10)


Liste_regle_frame.pack(fill=ctk.BOTH,expand=True,pady=10)



delete_btn.pack(ipady=5,ipadx=3)
bouton_liste_frame.pack(fill=ctk.BOTH,side=ctk.BOTTOM)



main_frame.pack(fill=ctk.BOTH,expand=True)

pages= [page1,page2]
cont=0

    




fenetre.mainloop()