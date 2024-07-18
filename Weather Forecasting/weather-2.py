from tkinter import *
import tkinter as tk
from webbrowser import open_new
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather Pridiction")
root.geometry("900x500+300+200")
root.resizable(False,False)

try:  
  def getWeather():
   city = textfield.get()
   geolocator = Nominatim(user_agent="geopiExercises")
   location = geolocator.geocode(city)
   obj = TimezoneFinder()
   result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
   home = pytz.timezone(result)
   local_time = datetime.now(home)
   current_time = local_time.strftime("%I:%M %p") 
   clock.config(text=current_time)
   name.config(text="CURRENT WEATHER")


   #Weather 
   api = "https://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=b1db77a39afa8f485d87310ff059dbeb"
   json_date = requests.get(api).json()
   condition = json_date['weather'][0]['main']
   description = json_date['weather'][0]['description']
   temp = int(json_date['main']['temp']-273.15)
   pressure = json_date['main']['pressure']
   humidity = json_date['main']['humidity']
   wind = json_date['wind']['speed']

   t.config(text=(temp,"°"))
   c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

   w.config(text=(wind,"km/h"))
   h.config(text=(humidity,"%"))
   d.config(text=description)
   p.config(text=(pressure,"Hg"))

except Exception as e:
  messagebox.showerror("Weather Pridiction","Invalid Entry!!")
  

  #serach box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()



Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


#Time
name = Label(root,font=("arial",15, "bold"))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1 = Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef" )
label1.place(x=120,y=400)

label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef" )
label2.place(x=250,y=400)

label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef" )
label3.place(x=430,y=400)

label4 = Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef" )
label4.place(x=650,y=400)

t = Label(font=("arial",70,"bold"),fg="red")
t.place(x=400,y=150)

c = Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)

p = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

# Lbl = ttk.Label( text = "Button Not Click ")  
# Lbl.pack()# Click event  
def click(): action.configure(open_new("http://127.0.0.1:5500/html/main.html"))  
# Lbl.configure(foreground = 'red')  
# Lbl.configure(text = 'Button Clicked')# Adding Button  
action = ttk.Button( text = "Learn More...", command = click)  
action.place(x=650,y=350)
# action.pack()  

root.mainloop()

