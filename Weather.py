import requests
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x420")
root.maxsize(400, 420)
root.minsize(400, 420)
root.title("Weather App")
root.configure(bg='#060d3d')
img = ImageTk.PhotoImage(Image.open('Images/Other_Images/Icon.png'))
root.iconphoto(False, img)

title = Label(root, text="Weather App", font=("Comic Sans MS", 30, "bold"), fg='brown', bg="#0a0e2b", borderwidth=3,
              relief="groove").place(
    x=0, y=-2, relwidth=1, height=70)

city = StringVar()
entry = Entry(root, textvariable=city, width=25, font=("Comic Sans MS", 10, "bold"), highlightbackground="brown",
              highlightcolor="brown", highlightthickness=3)
entry.insert(0, "Enter Your City Name...")
entry.bind("<FocusIn>", lambda args: entry.delete('0', 'end'))
entry.place(x=55, y=95, height=35)

lable_1 = Label(root, text="Temperature : ", width=20, bg="#060d3d", font=("Comic Sans MS", 15, "bold"), fg='#1861d6')
lable_1.place(x=30, y=150)

lable_2 = Label(root, text="Pressure     : ", width=20, bg="#060d3d", font=("Comic Sans MS", 15, "bold"), fg='#1861d6')
lable_2.place(x=30, y=180)

lable_3 = Label(root, text="Humidity     : ", width=20, bg="#060d3d", font=("Comic Sans MS", 15, "bold"), fg='#1861d6')
lable_3.place(x=30, y=210)

lable_temp = Label(root, text="...", width=20, bg="#060d3d", font=("Comic Sans MS", 10, "bold"), fg='#1861d6')
lable_temp.place(x=220, y=158)

lable_pres = Label(root, text="...", width=20, bg="#060d3d", font=("Comic Sans MS", 10, "bold"), fg='#1861d6')
lable_pres.place(x=220, y=188)

lable_hum = Label(root, text="...", width=20, bg="#060d3d", font=("Comic Sans MS", 10, "bold"), fg='#1861d6')
lable_hum.place(x=220, y=218)

lable_desc = Label(root, text="...", width=20, bg="#060d3d", font=("Comic Sans MS", 15, "bold"), fg='#c0eaed')
lable_desc.place(x=152, y=280)

lable_mm = Label(root, text="... | ...", width=20, bg="#060d3d", font=("Comic Sans MS", 18, "bold"), fg='#c0eaed')
lable_mm.place(x=120, y=320)


def getTemp():
    city_name = entry.get()
    appKey = "your api key"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + appKey + "&units=metric"

    weatherData = requests.get(url).json()

    if weatherData["cod"] != '404':
        current_temperature = int(weatherData['main']['temp'])
        current_pressure = str(weatherData['main']['pressure']) + " Pa"
        humidity = str(weatherData['main']['humidity']) + "%"
        max_temp = int(weatherData['main']['temp_max'])
        min_temp = int(weatherData['main']['temp_min'])
        weather_description = weatherData['weather'][0]['description']
        icon = weatherData['weather'][0]['icon']

        current_temperature = str(current_temperature) + "°C"
        mm = str(min_temp) + "°C" + " | " + str(max_temp) + "°C"

        lable_pres.configure(text=current_pressure)
        lable_temp.configure(text=current_temperature)
        lable_hum.configure(text=humidity)
        lable_mm.configure(text=mm)
        lable_desc.configure(text=weather_description)
        i = ImageTk.PhotoImage(Image.open(f'Images/Weather_Images/{icon}.png'))
        panel.configure(image=i)
        panel.image = i
    else:
        lable_pres.configure(text="Unknown")
        lable_temp.configure(text="Unknown")
        lable_hum.configure(text="Unknown")
        lable_mm.configure(text="Unknown")
        lable_desc.configure(text="Unknown")
        i = ImageTk.PhotoImage(Image.open('Images/Other_Images/Unknown.png'))
        panel.configure(image=i)
        panel.image = i


Button(root, text="Search", width=10, bg='brown', fg='white', font=("Comic Sans MS", 10, "bold"), command=getTemp,
       borderwidth=2, relief="raised", activebackground="#e0f5c9", activeforeground="#100b17").place(x=265, y=95,
                                                                                                     height=35)

img = ImageTk.PhotoImage(Image.open('Images/Other_Images/Loading.png'))
panel = Label(root, image=img, borderwidth=3, relief="ridge", bg="#a7c0e8")
panel.place(x=60, y=270)

mainloop()
