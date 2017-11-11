from Tkinter import *
import tkMessageBox
import Tkinter as tk

from FitoDownload import *
from FitoGeolocation import *
from FitoWebData import *
from Mr3SendData import *
from FitoWeather import *
from FitoConfig import *

#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk
import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class FitoMpiGui(Frame):
    
    # config vars
    cloud_api = "";
    appname = "";
    deviceId = "";
    ip = "0.0.0.0";
    port = 3000;
    timer = 0;

    # device info
    description = ""
    address = ""
    lat = 0.0
    lng = 0.0

    
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master
        
        self.init_config();
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

        

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget    
        self.master.title(self.appname)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        mainmenu = Menu(self.master)
        self.master.config(menu=mainmenu)

        # create the file object)
        fitotron = Menu(mainmenu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        fitotron.add_command(label="Get Context", command=self.getContext)
        fitotron.add_command(label="Start SendData", command=self.sendData)

        fitotron.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        mainmenu.add_cascade(label="File", menu=fitotron)

        # create the file object)
        setup = Menu(mainmenu)

        # adds a command to the menu option, calling it exit, and the
        mainmenu.add_cascade(label="Setup", menu=setup)

        setup.add_command(label="Parameters", command=self.create_parameters_window)




        #self.getGeolocation();
        #self.getWeather();        
 
    def init_config(self):
        myFitoConfig = FitoConfig();
        myData = myFitoConfig.getConfigData();
        #tkMessageBox.showinfo("FitoSmart - Config", myData)
        self.cloud_api = myData['cloud_api'];
        self.appname = myData['appname'];
        self.deviceid = myData['deviceid'];
        self.ip = myData['ip'];
        self.port = myData['port'];
        self.timer = myData['timer'];
        #print self.appname

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False


    def showImg(self):
        load = Image.open("fitotron.jpg")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=50)
        #img.grid(row=1, column=1)
        

    def sendData(self):
        self.showImg();
        myMr3 = Mr3SendData();
        myMsg = myMr3.sendData(self.lat, self.lng);
        tkMessageBox.showinfo("Mr3 - sendData", myMsg)

   
    def getDeviceData(self):
        myDeviceData = FitoWebData();
        
        myDevData = myDeviceData.getDeviceData(self.cloud_api);
        data =  myDevData

        myDownloadData = FitoDownload();
        myDowData = myDownloadData.getImageData(data);


 
    def getContext(self):
        self.   getDeviceData();
        lblContext = Label(self)#, text=myMsg)
        lblContext.pack()


    def create_parameters_window(self):
    

        #self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % "Parameters setup")

        def show():
          device_config = Object()       
          device_config.cloud_api = txt_cloud_api.get()
          device_config.appname = txt_appname.get()
          device_config.deviceid = txt_deviceid.get()
          device_config.ip = txt_ip.get()
          device_config.port = txt_port.get()
          device_config.timer = txt_timer.get()
          
          url = "device.config"
  
  #print url
          with open(url, "w") as f:
            f.write(device_config.toJSON())
          tkMessageBox.showinfo("FitoSmart - sendData", device_config.toJSON())
        l = tk.Label(t, text="cloud_api").grid(row=0)
        l = tk.Label(t, text="appname").grid(row=1)
        l = tk.Label(t, text="deviceid").grid(row=2)
        l = tk.Label(t, text="ip").grid(row=3)
        l = tk.Label(t, text="port").grid(row=4)
        l = tk.Label(t, text="timer").grid(row=5)

        txt_cloud_api = tk.Entry(t)
        txt_appname = tk.Entry(t)
        txt_deviceid = tk.Entry(t)
        txt_ip = tk.Entry(t)
        txt_port = tk.Entry(t)
        txt_timer = tk.Entry(t)

        txt_cloud_api.grid(row=0, column=1)
        txt_appname.grid(row=1, column=1)
        txt_deviceid.grid(row=2, column=1)
        txt_ip.grid(row=3, column=1)
        txt_port.grid(row=4, column=1)
        txt_timer.grid(row=5, column=1)

        txt_cloud_api.insert(END, self.cloud_api)
        txt_appname.insert(END, self.appname)
        txt_deviceid.insert(END, self.deviceid)
        txt_ip.insert(END, self.ip)
        txt_port.insert(END, self.port)
        txt_timer.insert(END, self.timer)
        
        l = tk.Button(t, text='Quit', command=t.quit).grid(row=6, column=0, sticky="w", pady=4)
        l = tk.Button(t, text='Show', command=show).grid(row=6, column=1, sticky="w", pady=4)


    def client_exit(self):
        exit()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = FitoMpiGui(root)


#mainloop 
root.mainloop()  
