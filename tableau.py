import customtkinter as ctk
from regle import Regle
class tableau:
    list_checked = []
    def __init__(self,master,bouton):
        self.master=master
        self.bouton=bouton
        self.list_frame = None
        self.colums:ctk.CTkFrame = ['']*7
    
    def buildTabHeader(self):
        headers = ['','Règles','Protocole','Options','IP source','IP de déstination','Etat']
        self.master.configure(fg_color="transparent")
        self.list_frame = ctk.CTkFrame(self.master,fg_color="transparent")
        self.list_frame.pack(fill=ctk.BOTH,expand=True)
        for i in range(len(headers)):
            self.colums[i] = ctk.CTkFrame(self.list_frame,border_color="#10151d",border_width=1,corner_radius=0,fg_color="transparent")
            title = ctk.CTkFrame(self.colums[i],border_color="#10151d",border_width=1,corner_radius=0,fg_color="#4f9c66")
            titre = ctk.CTkLabel(title,text=headers[i])
            titre.pack(pady=2)
            title.pack(fill=ctk.X,expand=True)
            self.colums[i].pack(side=ctk.LEFT,fill=ctk.BOTH,expand=True)

    def buildItems(self,contents:Regle):
        def check_action():
            item = state.get()[:-4]
            if "on" in state.get():
                self.list_checked.append(item)
            else:
                self.list_checked.remove(item)
            if len(tableau.list_checked) == 0:
                self.bouton.configure(state=ctk.DISABLED,cursor="circle")
            else:
                self.bouton.configure(state=ctk.NORMAL,cursor="hand2")

        Frame_checkBox = ctk.CTkFrame(self.colums[0],corner_radius=0,fg_color="#1a232e")
        state = ctk.StringVar()
        check_value = f"{contents.num}_{contents.chain}"
        Checkbox = ctk.CTkCheckBox(Frame_checkBox,text='',border_width=3,width=5,height=5,variable=state,command=check_action,onvalue=check_value+"__on",offvalue=check_value+"_off")
        Checkbox.pack(pady=2)
        Frame_checkBox.pack(fill=ctk.BOTH,expand=True,pady=5,padx=3)

        Frame_target = ctk.CTkFrame(self.colums[1],border_color="#10151d",border_width=1,corner_radius=0,fg_color="#1a232e")
        target_label = ctk.CTkLabel(Frame_target,text=contents.target)
        target_label.pack(fill=ctk.BOTH,expand=True)
        Frame_target.pack(fill=ctk.BOTH,expand=True,pady=5,padx=3)

        Frame_target = ctk.CTkFrame(self.colums[2],border_color="#10151d",border_width=1,corner_radius=0,fg_color="#1a232e")
        target_label = ctk.CTkLabel(Frame_target,text=contents.protocol)
        target_label.pack(fill=ctk.BOTH,expand=True)
        Frame_target.pack(fill=ctk.BOTH,expand=True,pady=5,padx=3)

        Frame_target = ctk.CTkFrame(self.colums[3],border_color="#10151d",border_width=1,corner_radius=0,fg_color="#1a232e")
        target_label = ctk.CTkLabel(Frame_target,text=contents.option)
        target_label.pack(fill=ctk.BOTH,expand=True)
        Frame_target.pack(fill=ctk.BOTH,expand=True,pady=5,padx=3)

        Frame_target = ctk.CTkFrame(self.colums[4],border_color="#10151d",border_width=1,corner_radius=0,fg_color="#1a232e")
        target_label = ctk.CTkLabel(Frame_target,text=contents.source)
        target_label.pack(fill=ctk.BOTH,expand=True)
        Frame_target.pack(fill=ctk.BOTH,expand=True,pady=5,padx=3)

        Frame_target = ctk.CTkFrame(self.colums[5],border_color="#10151d",border_width=1,corner_radius=0,fg_color="#1a232e")
        target_label = ctk.CTkLabel(Frame_target,text=contents.destination)
        target_label.pack(fill=ctk.BOTH,expand=True)
        Frame_target.pack(fill=ctk.BOTH,expand=True,pady=5,padx=3)

        Frame_target = ctk.CTkFrame(self.colums[6],border_color="#10151d",border_width=1,corner_radius=0,fg_color="#1a232e")
        target_label = ctk.CTkLabel(Frame_target,text=contents.etat)
        target_label.pack(fill=ctk.BOTH,expand=True)
        Frame_target.pack(fill=ctk.BOTH,expand=True,pady=5,padx=3)

    def clean(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.list_checked.clear()

    def get_list_frame(self):
        return self.list_frame

    def affiche_tab(self):
        self.list_frame.pack(fill=ctk.BOTH,expand=True)