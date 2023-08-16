import customtkinter as ctk
import pyautogui 
from CTkMessagebox import CTkMessagebox
from regle import *

class ttt:
    def __init__(self,master,app):
        self.master = master
        self.app = app
        self.octets = [0]*6


    def ip_input(self):
        def validate_entry(action, value):
            
            if action == '0':  # Suppression de texte
                return True
            if action == 'Return':
                return True
            
            if value.isdigit() and 0 <= int(value) <= 255 and len(value) <= 3 and value != '00':
                return True
            
            else:
                return False
        
        def validate_entry_mask(action, value):
            if action == '0':  # Suppression de texte
                return True
            if value.isdigit() and 0 <= int(value) <= 32 and len(value) <= 2 and value != '00':
                return True
            else:
                return False

        frame = ctk.CTkFrame(self.master,fg_color="transparent")   
        for i in range (4):
            octet = ctk.CTkEntry(frame,width=30,fg_color="#16181D",border_color="#c4eaee")
            octet.pack(side=ctk.LEFT,ipadx=3)
            validate_command = self.app.register(validate_entry)
            octet.configure(validate='key', validatecommand=(validate_command, '%d', '%P')) 
            self.octets[i]=octet
            if i==3:
                label = ctk.CTkLabel(frame,text=" / ",font=('bold',22))
            else:
                label = ctk.CTkLabel(frame,text=" . ")
            label.pack(side=ctk.LEFT)
        def enter_pressed(event):
            pyautogui.press('tab')
        
        octet = ctk.CTkEntry(frame,width=30,fg_color="#16181D",border_color="#c4eaee")
        octet.pack(side=ctk.LEFT,ipadx=3)
       
        validate_command = self.app.register(validate_entry_mask)
        octet.configure(validate='key', validatecommand=(validate_command, '%d', '%P')) 
        self.octets[4]=octet
        for i in range(4):
            self.octets[i].bind('<Return>',enter_pressed)
        frame.pack(side=ctk.LEFT,padx=10)
        
        return self.octets
    
    def _get_ip(self):
        if self.octets[0].get() == '' or self.octets[1].get() == '' or self.octets[2].get() == '' or self.octets[3].get()== '' :
            ip = ''
        else:
            if self.octets[4].get() == '':
                ip = self.octets[0].get()+"."+self.octets[1].get()+"."+self.octets[2].get()+"."+self.octets[3].get()
            else:
                ip = self.octets[0].get()+"."+self.octets[1].get()+"."+self.octets[2].get()+"."+self.octets[3].get()+"/"+self.octets[4].get()
        return ip
    def _set_ip(self):
        print("dlmskjfq")
    
    def _set_empty(self):
        for i in range(5):
            self.octets[i].delete(0,"end")
    def _set_focus(self):
        self.octets[0].focus_set()



        
    
class Messagebox():
    def __init__(self,message) -> None:
        self.__message = message

    def show_succes_mess(self):
        CTkMessagebox(message=self.__message,icon="check",option_1="OK",title="succès",bg_color="#26282D",fg_color="#2a333f",border_width=30, border_color="#26282D",width=360,cancel_button="circle",button_color="#0c8069",button_hover_color="#2ca089",justify="center")
    
    def show_error_mess(self):
        self.addMessage("Une erreur s'est produite :( ")
        CTkMessagebox(message=self.__message,icon="cancel",option_1="OK",title="erreur",bg_color="#26282D",fg_color="#2a333f",border_width=30, border_color="#26282D",width=360,cancel_button="circle",button_color="#0c8069",button_hover_color="#2ca089",justify="center")

    def set_message(self,mess):
        self.__message = mess

    def addMessage(self,mess_to_add):
        mess = mess_to_add+"\n\n"+self.__message
        self.set_message(mess)

    def affiche_mbox(self):
        if self.__message == "Operation effectuée avec succès.":
            self.show_succes_mess()
        else:
            self.show_error_mess()


        