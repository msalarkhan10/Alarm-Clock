from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from  threading import Thread
from datetime import datetime
import pytz
from pygame import mixer
from time import sleep
mixer.init()





bg_colour = "#ffffff"
coll = '#566FC6' #blue

window = Tk()
window.title("Alarm Clock")
window.configure(bg=bg_colour)
window.geometry('350x150')



frame_line = Frame(window, width=400, height=5, bg=coll)
frame_line.grid(row=0, column=0)
frame_body = Frame(window, width=400, height=290, bg=bg_colour)
frame_body.grid(row=1, column=0)


img = Image.open('icon.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)


app_image = Label(frame_body, height=100, width=100, image=img, bg=bg_colour)
app_image.place(x=10, y=10)

hour = Label(frame_body, text="Hour", height=1, font = ('Ivy 10 bold'), bg=bg_colour, fg=coll )
hour.place(x=127, y=40)

c_hour = Combobox(frame_body, width = 2, font=('arial 15'))
c_hour ['values'] = ("00", "01", "02", "03", "04", "05", "06", "07","08", "09", "10", "11", "12", "13", "14", "15",
"16", "17", "18", "19", "20", "21", "22", "23")
c_hour.current(0)
c_hour.place(x=130, y=58)


min = Label(frame_body, text="Min", height=1, font = ('Ivy 10 bold'), bg=bg_colour, fg=coll )
min.place(x=177, y=40)

c_min = Combobox(frame_body, width = 2, font=('arial 15'))
c_min ['values'] = ("00", "01", "02", "03", "04", "05", "06", "07","08", "09", "10", "11", "12", "13", "14", "15",
"16", "17", "18", "19", "20", "21", "22", "23" , "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
"36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
"48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=180, y=58)


sec = Label(frame_body, text="Sec", height=1, font = ('Ivy 10 bold'), bg=bg_colour, fg=coll )
sec.place(x=227, y=40)


c_sec = Combobox(frame_body, width = 2, font=('arial 15'))
c_sec ['values'] = ("00", "01", "02", "03", "04", "05", "06", "07","08", "09", "10", "11", "12", "13", "14", "15",
"16", "17", "18", "19", "20", "21", "22", "23" , "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
"36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
"48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")

c_sec.current(0)
c_sec.place(x=230, y=58)

selected = IntVar()


def activate_alarm():
    print("Alarm created")
    t = Thread(target=alarm)
    t.start()


rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Activate", bg=bg_colour, command=activate_alarm, variable=selected,)
rad1.place(x=125, y=95 )


def deactivate_alarm():
    print("Okey its getting closed now yippe :)")
    mixer.music.stop()



def alarm():
    while True:
        alarm_hour = c_hour.get()    
        alarm_minute = c_min.get()
        alarm_second = c_sec.get()
        now = datetime.now(pytz.timezone('Asia/Karachi'))
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        print(f'{hour}:{minute}:{second}')
        if alarm_hour == hour:
            if alarm_minute == minute:
                if alarm_second == second:
                    print("Time to take a break")
                    t = Thread(target=sound_alarm())
                    t.start()
                    return
        sleep(1)



def sound_alarm():
    mixer.music.load('alarm_sound.mp3')
    mixer.music.play(loops=5)
    sleep(2)
    print(mixer.music.get_busy())
    print("Alarm is now playing")
    selected.set(0)
    rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Deactivate", bg=bg_colour, command=deactivate_alarm, variable=selected,)
    rad1.place(x=200, y=95 )





window.mainloop()



