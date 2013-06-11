from gi.repository import Gtk
from gi.repository import GdkPixbuf
from gi.repository import GLib
from random import randint
from socket import gethostname

gui_contactlist = Gtk.ListStore(str,int)

Contactlist = {}
Selected = -1

#Gui items
Selbox = None
Sel_lbl = None
Nick_box = None
Builder = None


def wcd_close(w,e):
    w.hide()
    return True

def gui_showdetails(Treeview,path,view_column):
    global Builder
    Detailwindow = Builder.get_object("window_contact_details")
    Nick_lbl = Builder.get_object("wcd_nick")
    
    Selection = Treeview.get_selection()
    (Gls,tree_iter) = Selection.get_selected()
    gv = Gls.get_value(tree_iter,1)
    print(Gls.get_value(tree_iter,1))
    print(Contactlist[gv].nick)

    #Populate window
    Nick_lbl.set_text(Contactlist[gv].nick)
    Detailwindow.show_all()

def nfid():
    if len(Contactlist) == 0: return 0
    for i in range(max(Contactlist) + 2):
        if(i in Contactlist):
                continue
        else:
                return i

def ui_remove(list_it):
    gui_contactlist.remove(list_it)
    return False

def ui_unselect():
    Sel_lbl.set_text("No recipient selected")
    Sb = Selbox.get_selection()
    Sb.unselect_all()
    return False

class Message_in:
    def __init__(self,mc,contents,transport):
        self.time_received = 0
        self.time_sent = 0
        self.timeout = 0
        self.mc = mc
        self.transport = transport
        self.security = 0
        self.contents = contents
        self.multipart = ()
        self.seqid = 0
        
class Contact:
    def __init__(self):
        self.nick = ""
        self.list_it = None
        self.Transports = {}
        self.autodel = True     
        self.nfid = nfid()

        Contactlist[self.nfid] = self

        #Security attributes
                        #in_file,in_offset,out_file,out_offset
        self.otp_info = ["",0,"",0]
        self.enc_key = ""

        #self.Messages_incoming = {}
        #self.Messages_outgoing = {}

        self.Messages_pending = {}
        
    def ui_nick(self):
        if(self.list_it): gui_contactlist[self.list_it] = [self.nick, self.nfid]
        else: self.list_it = gui_contactlist.append([self.nick,self.nfid])
        return False

    #def ui_removeself(self):
     #   gui_contactlist.remove(self.list_it)
     #   return False
    
    def __del__(self):
        global Selected
        print("Delself")
        GLib.idle_add(ui_remove,self.list_it)
        
        if(self.nfid == Selected):
            Selected = -1
            GLib.idle_add(ui_unselect)
            
    def add_transport(self,transport,key):
        self.Transports[transport] = key
        
    #def del_transport(self,transport):
    #   del self.Transports[transport]
    #  if(self.autodel and (not self.Transports)): del(self)

    def set_nick(self,nickname):
        self.nick = nickname
        GLib.idle_add(self.ui_nick)

class Self_contact:
    def __init__(self,nickname):
        self.nick = nickname
        #Nick_box.set_text(nickname)
        

Myself = Self_contact(gethostname())
