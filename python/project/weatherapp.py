from tkinter import *
from tkinter import ttk
import requests


def fun():
    api_key="e47429e143998249994c6b058252d08b"
    request=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={var.get()}&appid={api_key}")
    ans=request.json()
    weathere_info.config(text=str(ans["main"]["temp"])+"°k"+"\n"+ans["weather"][0]["description"])
    print(ans)
    thankyou.config(text="Thank you for using our app \n GHOST")
    








win=Tk()
win.title("Weather App")
win.geometry("300x500")
win.configure(bg="light blue")
win.resizable(0,0)

var=StringVar()

indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", 
    "Kolkata", "Surat", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", 
    "Indore", "Thane", "Bhopal", "Visakhapatnam", "Vadodara", "Firozabad", 
    "Ludhiana", "Rajkot", "Agra", "Siliguri", "Nashik", "Faridabad", 
    "Patna", "Meerut", "Kalyan-Dombivli", "Vasai-Virar", "Varanasi", 
    "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", 
    "Allahabad", "Ranchi", "Howrah", "Coimbatore", "Jabalpur", "Gwalior", 
    "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota", "Guwahati", 
    "Chandigarh", "Solapur", "Hubballi-Dharwad", "Bareilly", "Moradabad", 
    "Mysore", "Gurugram", "Aligarh", "Jalandhar", "Tiruchirappalli", 
    "Bhubaneswar", "Salem", "Mira-Bhayandar", "Warangal", "Thiruvananthapuram", 
    "Guntur", "Bhiwandi", "Saharanpur", "Gorakhpur", "Bikaner", 
    "Amravati", "Noida", "Jamshedpur", "Bhilai", "Cuttack", "Firozabad", 
    "Kochi", "Bhavnagar", "Dehradun", "Durgapur", "Asansol", 
    "Nanded", "Ajmer", "Jamnagar", "Ujjain", "Sangli", "Loni", 
    "Jhansi", "Pondicherry", "Nellore", "Jammu", "Belgaum", "Raurkela", 
    "Mangalore", "Tirunelveli", "Malegaon", "Gaya", "Tiruppur", 
    "Davanagere", "Kozhikode", "Akola", "Kurnool", "Rajahmundry", 
    "Bokaro", "South Dumdum"
]

lis=ttk.Combobox(win,values=indian_cities,textvariable=var,font=(30))
lis.set("Select City")
lis.place(x=50,y=50,height=50,width=200)

but=Button(win,text="Submit",command=fun)
but.place(x=120,y=150)



weathere_info=Label(win,text="wait for weather info",font=(30),bg="light blue")
weathere_info.place(x=85,y=250)


thankyou=Label(win,text="",font=(30),bg="light blue")
thankyou.place(x=50,y=400)




win.mainloop()

