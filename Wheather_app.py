import tkinter as tk
import requests as req

    
# ENTRY WIDGET TO ENTER THE CITY NAME

city_entry = ttkb.Entry(root, font="Cambria, 14")
city_entry.pack(pady=10)

# BUTTON WIDGET TO FOUND WEATHER INFO 

search_button = ttkb.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# LABEL WIDGET TO SHOW THE LOCATION NAME 

location_label = tk.Label(root, font="Cambria, 19")
location_label.pack(pady=18)

# LABEL WIDGET TO SHOW THE WEATHER ICON

icon_label = tk.Label(root)
icon_label.pack()

temperature_lbl = tk.Label(root, font="Cambria, 16")
temperature_lbl.pack()

description_label = tk.Label(root, font="Cambria, 16")
description_label.pack()

    

# Parse the response in JSON to get weather information

weather = req.json()
icon_id = weather["weather"][0]["icon"]
temperature = weather["main"]["temp"] - 273.15
description = weather["weather"][0]["description"]
city = weather["name"]
country = weather["sys"]["country"]


def get_icon(icon_url):
    """"
    Get the icon url and return all the weather data
    """""
    icon_url = f"https://openweathermap.org/img/wm/{icon_id}@2x.png"
    return (icon_url,temperature,description,city,country)
    



root.mainloop()
