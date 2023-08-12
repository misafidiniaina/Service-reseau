import customtkinter as ctk
import pyautogui 
import keyboard

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
                """if int(value) >= 25 and len(value)==2:
                    pyautogui.press('tab')
                elif 0 <= int(value) <= 255 and len(value)==3:
                    pyautogui.press('tab')""" 
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
            octet = ctk.CTkEntry(frame,width=30,fg_color="#1a232e",border_color="#c4eaee")
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
        
        octet = ctk.CTkEntry(frame,width=30,fg_color="#1a232e",border_color="#c4eaee")
        octet.pack(side=ctk.LEFT,ipadx=3)
       
        validate_command = self.app.register(validate_entry_mask)
        octet.configure(validate='key', validatecommand=(validate_command, '%d', '%P')) 
        self.octets[4]=octet
        for i in range(5):
            self.octets[i].bind('<Return>',enter_pressed)
        frame.pack(side=ctk.LEFT,padx=10)
        
        return self.octets
    
    def _get_ip(self):
        ip = self.octets[0].get()+"."+self.octets[1].get()+"."+self.octets[2].get()+"."+self.octets[3].get()+"/"+self.octets[4].get()
        return ip
    def _set_ip(self):
        print("dlmskjfq")
    
    def _set_empty(self):
        for i in range(5):
            self.octets[i].delete(0,"end")
    def _set_focus(self):
        self.octets[0].focus_set()


class tableau:
    def __init__(self,master,bouton):
        self.master=master
        self.bouton=bouton
        self.list_frame = None
    def affiche(self,contents):
        #self.clean()
        def checked_listner():
            print(str(state.get()))
            """if any(state.get() == 1 in state):
                self.bouton.configure(state=ctk.DISABLED)
            else:
                self.bouton.configure(state=ctk.NORMAL)"""
            
                
        list_frame = ctk.CTkFrame(self.master)
        self.list_frame = list_frame
        headers=['','Règles','Protocole','Options','Source','Destination','Déscription']
        cellule=['none']*7
        header=[0,0,0,0,0,0,0]
        header_frame = ctk.CTkFrame(list_frame)
        for i in range(len(headers)):
            cellule[i] = ctk.CTkFrame(header_frame,border_width=1,border_color="black",corner_radius=0)
            header[i]=ctk.CTkFrame(cellule[i],border_width=1,border_color="black",corner_radius=0)
            text = ctk.CTkLabel(header[i],text=headers[i],corner_radius=0)
            text.pack(fill=ctk.X,padx=5,pady=5)
            header[i].pack(fill=ctk.X,expand=True)
            cellule[i].pack(fill=ctk.X,side=ctk.LEFT,expand=True)
        for data in range(len(contents)):
            for col in range(len(contents[data])):
                text = str(contents[data][col])
                if col==0:
                    state = ctk.StringVar()
                    check = ctk.CTkCheckBox(cellule[col],text="",checkbox_width=20,checkbox_height=20,height=28,width=1,command=checked_listner,variable=state,onvalue="on",offvalue="off")
                    check.pack(pady=3)
                else:
                    donnee = ctk.CTkLabel(cellule[col],text=text)
                    donnee.pack(pady=3)
        header_frame.pack(fill=ctk.X)
        list_frame.pack(fill=ctk.BOTH,expand=True,padx=5,pady=5)
        
    def clean(self):
        self.list_frame.destroy()

    
    

        