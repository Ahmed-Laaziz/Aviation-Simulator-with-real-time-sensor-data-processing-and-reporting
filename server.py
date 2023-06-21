import tkinter as tk
from random import random
import random

from PIL import ImageTk
from tkinter import *
import pygame

from kafka_sensors import KafkaProducer

try:
    from PIL import Image
except ImportError:
    import Image
from tkinter import messagebox
import math
import socket
import threading
import pyttsx3
import pyaudio

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 5555))

def play_sound(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 150)

#from main import CircleButton

root = tk.Tk()

parent_frame = tk.Frame(root, bg="black")
parent_frame.pack()
canvas = tk.Canvas(parent_frame, width=1750, height=400)



sky_gif_image = Image.open("C:\\Users\\ADMIN\\Downloads\\skygif.gif")
#nd_bg_image = Image.open("C:\\Users\\ADMIN\\Downloads\\nd_bg.gif")
# Create a list of photo images from the frames of the GIF animation
sky_photo_frames = []

try:
    while True:
        # Resize each frame to a new width and height
        sky_new_width = 1550
        sky_new_height = 400
        sky_resized_image = sky_gif_image.resize((sky_new_width, sky_new_height))
        # Create a PhotoImage object from the resized image
        sky_photo_frames.append(ImageTk.PhotoImage(sky_resized_image))

        sky_gif_image.seek(len(sky_photo_frames))  # Move to the next frame
except EOFError:
    pass  # End of frames







# Load the image
#img = Image.open("C:\\Users\\ADMIN\\Downloads\\3-34566_go-to-image-sky-png-transparent-background.png")

# Resize the image
#resized_img = img.resize((2500, 500))

# Create a PhotoImage from the resized image
#bg_img = ImageTk.PhotoImage(resized_img)
# Load the background image and its dimensions
#bg_img = PhotoImage(file="C:\\Users\\ADMIN\\Downloads\\3-34566_go-to-image-sky-png-transparent-background.png")


#bg_width = bg_img.width()
#bg_height = bg_img.height()

# Create two image objects to hold the two copies of the background
#bg1 = canvas.create_image(0, 0, image=bg_img, anchor=NW)
#bg2 = canvas.create_image(bg_width, 0, image=bg_img, anchor=NW)
sky_image_item = canvas.create_image(0, 0, anchor=NW, image=sky_photo_frames[0])
canvas.lower(tk.ALL)

# Set the scrolling speed and direction
scroll_speed = 2  # pixels per frame
scroll_direction = -1  # leftwards

# Define a function to scroll the background




def rotate_right_plane2(event):
    global rotation
    if (event.char == "v") and rotation == 0 or rotation == 10:
        global image_plane, plane_photo, img2
        global pil_image, photovv, canvas_image
        image_plane = image_plane.rotate(-3, resample=Image.BICUBIC)#image = image.rotate
        plane_photo = ImageTk.PhotoImage(image_plane)
        canvas.itemconfigure(img2, image=plane_photo)
        pil_image = pil_image.rotate(-3, resample=Image.BICUBIC)  # image = image.rotate
        cropped = pil_image.crop((x_offset, y_offset, x_offset + canvas_width, y_offset + canvas_height))
        photovv = ImageTk.PhotoImage(cropped)
        canvas1.itemconfigure(canvas_image, image=photovv)
        rotation = (rotation - 10) % 360
        #print(rotation)
def rotate_right(event):
    global rotation
    if (event == "x") and rotation == 0 or rotation == 10:
        global plane2_image, photo2_image, img1
        # global pil_image, photovv, canvas_image
        plane2_image = plane2_image.rotate(-3, resample=Image.BICUBIC)
        photo2_image = ImageTk.PhotoImage(plane2_image)
        canvas.itemconfigure(img1, image=photo2_image)
        rotation = (rotation - 10) % 360

def rotate_left_plane2(event):
    global rotation
    if (event.char == "c") and rotation == 0 or rotation == 350:
        global image_plane, plane_photo, img2
        global pil_image, photovv, canvas_image
        image_plane = image_plane.rotate(3, resample=Image.BICUBIC)
        plane_photo = ImageTk.PhotoImage(image_plane)
        canvas.itemconfigure(img2, image=plane_photo)

        pil_image = pil_image.rotate(3, resample=Image.BICUBIC)  # image = image.rotate
        cropped = pil_image.crop((x_offset, y_offset, x_offset + canvas_width, y_offset + canvas_height))
        photovv = ImageTk.PhotoImage(cropped)
        canvas1.itemconfigure(canvas_image, image=photovv)
        rotation = (rotation + 10) % 360
       # print(rotation)
def rotate_left(event):
    global rotation
    if (event == "y") and rotation == 0 or rotation == 350:
        global plane2_image, photo2_image, img1
        #global pil_image, photovv, canvas_image
        plane2_image = plane2_image.rotate(3, resample=Image.BICUBIC)
        photo2_image = ImageTk.PhotoImage(plane2_image)
        canvas.itemconfigure(img1, image=photo2_image)
        rotation = (rotation + 10) % 360

plane2_image = Image.open("C:\\Users\\ADMIN\\Downloads\\resized_tanker2.png")
photo2_image = ImageTk.PhotoImage(plane2_image)
img1 = canvas.create_image(50, 250, anchor="nw", image=photo2_image)


#another plane
image_plane = Image.open("C:\\Users\\ADMIN\\Downloads\\normal_plane.png")
plane_photo = ImageTk.PhotoImage(image_plane)
#resized_image1 = image.subsample(6, 6)
img2 = canvas.create_image(20, 20, anchor="nw", image=plane_photo)

rotation = 0
canvas.bind_all("<KeyPress-v>", rotate_right_plane2)
canvas.bind_all("<KeyPress-c>", rotate_left_plane2)
canvas.focus_set()

# Create a StringVar to hold the value of the button
button_value = tk.StringVar(value="Speed : 0")
button_value1 = tk.StringVar(value="Altitude : 100")

# plane 2
button_value_plane2 = tk.StringVar(value="Speed : 0")
button_value1_plane2 = tk.StringVar(value="Altitude : 100")
# Create a frame widget to hold the buttons and image
#frame = tk.Frame(root, bg="black")
#frame.pack(side="left", pady=10)


mode_tanker = "manual"
mode_plane = "manual"
def tanker_flight_mode(event):
    global mode_tanker
    if event == 'A':
        mode_tanker = "automatic"
        #play_sound("mode auto pilote activé")
    elif event == 'M':
        mode_tanker = "manual"
        #play_sound("mode manuel activé")
def plane_flight_mode(event):
    global mode_plane
    if event.keysym == 'K':
        mode_plane = "automatic"
        play_sound("mode auto pilote activé")
    elif event.keysym == 'L':
        mode_plane = "manual"
        play_sound("mode manuel activé")

############################################################## EWD #####################################################

def move_lines():
    global angle1, angle2
    random_value = random.randint(0, 1)
    if random_value == 0:
        #angle1 += 2
        angle2 += 1
    elif random_value == 1:
        angle1 -= 1
        angle2 -= 1
    else:
        return
    angle1 = max(min(angle1, 180), 0)
    angle2 = max(min(angle2, 180), 0)
    x1, y1 = get_coordinates(angle1)
    x2, y2 = get_coordinates(angle2, x_offset=200)

    if angle1 < 90 and angle2 <90:
        canvas_nd_accelerometer.itemconfig(line1, fill='green')
        canvas_nd_accelerometer.itemconfig(line2, fill='green')
        canvas_nd_accelerometer.itemconfig(text1, text='{}'.format(angle1),fill='green')
        canvas_nd_accelerometer.itemconfig(text2, text='{}'.format(angle2),fill='green')
        canvas_nd_accelerometer.itemconfig(css,fill='green')
        canvas_nd_accelerometer.itemconfig(css2, fill='green')
        canvas_nd_accelerometer.itemconfig(warning_text, text='N1 exceeds {} %'.format(angle1), fill="black")
    elif angle1 >= 90 and angle1 <140 and angle2 >= 90 and angle2 < 140:
        canvas_nd_accelerometer.itemconfig(line1, fill='yellow')
        canvas_nd_accelerometer.itemconfig(line2, fill='yellow')
        canvas_nd_accelerometer.itemconfig(text1, text='{}'.format(angle1),fill='yellow')
        canvas_nd_accelerometer.itemconfig(text2, text='{}'.format(angle2),fill='yellow')
        canvas_nd_accelerometer.itemconfig(css, fill='yellow')
        canvas_nd_accelerometer.itemconfig(css2, fill='yellow')
        canvas_nd_accelerometer.itemconfig(warning_text, text='N1 exceeds {} %'.format(angle1), fill="yellow")
    else:
        canvas_nd_accelerometer.itemconfig(line1, fill='red')
        canvas_nd_accelerometer.itemconfig(line2, fill='red')
        canvas_nd_accelerometer.itemconfig(text1, text='{}'.format(angle1),fill='red')
        canvas_nd_accelerometer.itemconfig(text2, text='{}'.format(angle2),fill='red')
        canvas_nd_accelerometer.itemconfig(css, fill='red')
        canvas_nd_accelerometer.itemconfig(css2, fill='red')
        canvas_nd_accelerometer.itemconfig(warning_text, text='N1 exceeds {} %'.format(angle1), fill="red")
        #play_alarm_sound()
    canvas_nd_accelerometer.coords(line1, 100, 100, x1, y1)
    canvas_nd_accelerometer.coords(line2, 300, 100, x2, y2)

    canvas_nd_accelerometer.itemconfig(text1, text='{}'.format(angle1))
    canvas_nd_accelerometer.itemconfig(text2, text='{}'.format(angle2))


def moves_lines2():
    global angle3
    random_value = random.randint(0, 1)
    if random_value == 0: #event.keysym
        angle3 += 2
    elif random_value == 1: #event.keysym
        angle3 -= 1
    else:
        return
    angle3 = max(min(angle3, 180), 0)
    x3, y3 = get_coordinates(angle3, x_offset=0, y_offset=200)

    if angle3 < 90:
        canvas_nd_accelerometer.itemconfig(line3, fill='green')
        canvas_nd_accelerometer.itemconfig(text3, text='{}'.format(angle3), fill='green')
        canvas_nd_accelerometer.itemconfig(css3,fill='green')
        canvas_nd_accelerometer.itemconfig(warning_text1, text='EGT exceeds {} %'.format(angle3), fill="black")


    elif angle3 >= 90 and angle3 < 120:
        canvas_nd_accelerometer.itemconfig(line3, fill='yellow')
        canvas_nd_accelerometer.itemconfig(text3, text='{}'.format(angle3), fill='yellow')
        canvas_nd_accelerometer.itemconfig(css3, fill='yellow')
        canvas_nd_accelerometer.itemconfig(warning_text1, text='EGT exceeds {} %'.format(angle3),fill="yellow")
    else:
        canvas_nd_accelerometer.itemconfig(line3, fill='red')
        canvas_nd_accelerometer.itemconfig(text3, text='{}'.format(angle3), fill='red')
        canvas_nd_accelerometer.itemconfig(css3, fill='red')
        canvas_nd_accelerometer.itemconfig(warning_text1,text='EGT exceeds {} %'.format(angle3), fill="red")


    canvas_nd_accelerometer.coords(line3, 100, 300, x3, y3)
    canvas_nd_accelerometer.itemconfig(text3, text='{}'.format(angle3))

def moves_lines3():
    global angle4
    random_value = random.randint(0, 1)
    if random_value == 0:
        angle4 += 2
    elif random_value == 1:
        angle4 -= 2
    else:
        return
    angle4 = max(min(angle4, 180), 0)
    x4, y4 = get_coordinates(angle4, x_offset=200, y_offset=200)

    if angle4 < 90:
        canvas_nd_accelerometer.itemconfig(line4, fill='green')
        canvas_nd_accelerometer.itemconfig(text4, text='{}'.format(angle4), fill='green')
        canvas_nd_accelerometer.itemconfig(css4, fill='green')

    elif angle4 >= 90 and angle4 < 120:
        canvas_nd_accelerometer.itemconfig(line4, fill='yellow')
        canvas_nd_accelerometer.itemconfig(text4, text='{}'.format(angle4), fill='yellow')
        canvas_nd_accelerometer.itemconfig(css4, fill='yellow')
    else:
        canvas_nd_accelerometer.itemconfig(line4, fill='red')
        canvas_nd_accelerometer.itemconfig(text4, text='{}'.format(angle4), fill='red')
        canvas_nd_accelerometer.itemconfig(css4, fill='red')


    canvas_nd_accelerometer.coords(line4, 300, 300, x4, y4)

    canvas_nd_accelerometer.itemconfig(text4, text='{}'.format(angle4))

def get_coordinates(angle, x_offset=0, y_offset=0):
    x = 100 - 80 * math.cos(angle * math.pi / 180)
    y = 100 - 80 * math.sin(angle * math.pi / 180)
    return x + x_offset, y + y_offset


canvas_nd_accelerometer = tk.Canvas(parent_frame, width=398, height=390, bg='black', borderwidth=0, highlightthickness=0)
canvas_nd_accelerometer.pack(side=tk.LEFT)
canvas.pack()
angle1 = 120
angle2 = 16 #pressure
angle3 = 70 #Temperature (°F)
angle4 = 65 #Oil Pressure (Psi)






#CSS
css = canvas_nd_accelerometer.create_oval(95, 95, 105, 105, width=2, fill="green")
css4 = canvas_nd_accelerometer.create_oval(295, 295, 305, 305, width=2, fill="green")

css3 = canvas_nd_accelerometer.create_oval(95, 295, 105, 305, width=2, fill="green")
css2 = canvas_nd_accelerometer.create_oval(295, 95, 305, 105, width=2, fill="green")





canvas_nd_accelerometer.create_arc(20, 20, 180, 180, start=0, extent=180, style='arc',outline="white",width=2)
canvas_nd_accelerometer.create_arc(220, 20, 380, 180, start=0, extent=180, style='arc',outline="white",width=2)
canvas_nd_accelerometer.create_arc(20, 220, 180, 380, start=0, extent=180, style='arc',outline="white",width=2)
canvas_nd_accelerometer.create_arc(20, 220, 180, 380, start=0, extent=60, style='arc',outline="red",width=2)
canvas_nd_accelerometer.create_arc(220, 220, 380, 380, start=0, extent=180, style='arc',outline="white",width=2)
canvas_nd_accelerometer.create_arc(220, 220, 380, 380, start=0, extent=60, style='arc',outline="red",width=2)

#N1
canvas_nd_accelerometer.create_text(190, 50, text='⛽',fill="white", anchor='nw',font=('Arial', 12))
canvas_nd_accelerometer.create_text(192, 75, text='%',fill="sky blue", anchor='nw',font=('Arial', 12))

#EGT
canvas_nd_accelerometer.create_text(185, 250, text='EGT',fill="white", anchor='nw',font=('Arial', 12))
canvas_nd_accelerometer.create_text(190, 270, text='°F',fill="sky blue", anchor='nw',font=('Arial', 12))

#0-180 TOP-LEFT
canvas_nd_accelerometer.create_text(165, 100, text='180',fill="gray", anchor='nw',font=('Arial', 12))
canvas_nd_accelerometer.create_text(10, 100, text='0',fill="gray", anchor='nw',font=('Arial', 12))

#0-180 TOP-Right
canvas_nd_accelerometer.create_text(370, 100, text='180',fill="gray", anchor='nw',font=('Arial', 12))
canvas_nd_accelerometer.create_text(210, 100, text='0',fill="gray", anchor='nw',font=('Arial', 12))

#0-180 Bottom-left
canvas_nd_accelerometer.create_text(10, 300, text='0',fill="gray", anchor='nw',font=('Arial', 12))
canvas_nd_accelerometer.create_text(175, 300, text='180',fill="gray", anchor='nw',font=('Arial', 12))

#0-180 Bottom-right
canvas_nd_accelerometer.create_text(210, 300, text='0',fill="gray", anchor='nw',font=('Arial', 12))
canvas_nd_accelerometer.create_text(370, 300, text='180',fill="gray", anchor='nw',font=('Arial', 12))

line1 = canvas_nd_accelerometer.create_line(100, 100, *get_coordinates(angle1), width=2, fill='green')
line2 = canvas_nd_accelerometer.create_line(300, 100, *get_coordinates(angle2, x_offset=200), width=2, fill='green')
line3 = canvas_nd_accelerometer.create_line(100, 300, 20,300, width=2, fill='green')
line4 = canvas_nd_accelerometer.create_line(300, 300, 220,300, width=2, fill='green')
rectangle1 =canvas_nd_accelerometer.create_rectangle(50, 105, 150, 130, outline="white", fill="black")
rectangle2 =canvas_nd_accelerometer.create_rectangle(250,105,350,130,outline="white",fill="black")
rectangle3 =canvas_nd_accelerometer.create_rectangle(50,305,150,335,outline="white",fill="black")
rectangle4 =canvas_nd_accelerometer.create_rectangle(250,305,350,335,outline="white",fill="black")
text1=canvas_nd_accelerometer.create_text(90, 102, text='{}'.format(angle1),fill="green", anchor='nw',font=('Arial', 20))
text2=canvas_nd_accelerometer.create_text(290, 102, text='{}'.format(angle2),fill="green", anchor='nw',font=('Arial', 20))
text3=canvas_nd_accelerometer.create_text(90, 302, text='{}'.format(angle3),fill="green", anchor='nw',font=('Arial', 20))
text4=canvas_nd_accelerometer.create_text(290, 302, text='{}'.format(angle4),fill="green", anchor='nw',font=('Arial', 20))



warning_text=canvas_nd_accelerometer.create_text(30, 350, text='N1 exceeds {} %'.format(angle1),fill="black", anchor='nw',font=('Arial', 15))
warning_text1=canvas_nd_accelerometer.create_text(30, 370, text='EGT exceeds {} %'.format(angle1),fill="black", anchor='nw',font=('Arial', 15))



#canvas_nd_accelerometer.focus_set()
#canvas_nd_accelerometer.bind_all('<Up>', moves_lines3)
#root.bind('<Left>', move_lines)
#canvas_nd_accelerometer.bind('<I>', moves_lines2)
#canvas_nd_accelerometer.bind('<D>', moves_lines2)
#root.bind('<Up>', moves_lines3)
#root.bind('<Down>', moves_lines3)


#################################################### END EWD ##########################################################





#================================= Audio =====================================#


p = pyaudio.PyAudio()

chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 5454
s.bind((host, port))

s.listen(1)


print(f"Listening on ...")


#window = tk.Tk()
#window.title("Audio Recorder")


audio_data = []

record_pressed = False
seconds = 5

def start_recording():
    global audio_data


    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)


    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        audio_data.append(data)


    stream.stop_stream()
    stream.close()
def send_audio():

    s_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_send = 'localhost'
    port_send = 5454
    s_send.connect((host_send, port_send))

    for data in audio_data:
        s_send.sendall(data)


    s_send.close()


def receive_audio():

    conn, addr = s.accept()
    print(f"Connection from {addr[0]}:{addr[1]}")

    stream_recv = p.open(format=sample_format,
                         channels=channels,
                         rate=fs,
                         frames_per_buffer=chunk,
                         output=True)


    while conn:
        data = conn.recv(chunk)
        if not data:
            break
        stream_recv.write(data)


    stream_recv.stop_stream()
    stream_recv.close()
    conn.close()


#canvas_audio = tk.Canvas(parent_frame, width=350, height=450)
#canvas_audio.pack(side=tk.LEFT)

canvas.pack()
button_record = tk.Button(parent_frame, text="📣", command=start_recording, font=("Arial",16), background="gray")
button_record.pack(anchor=tk.CENTER, side="left",  padx=0, ipadx=30)


button_send = tk.Button(parent_frame, text="➤", command=send_audio, font=("Arial",16), background="gray")
button_send.pack(anchor=tk.CENTER, side="left",  padx=0, ipadx=30)


button_receive = tk.Button(parent_frame, text="👂", command=lambda: threading.Thread(target=receive_audio).start(),font=("Arial",16), background="gray")
button_receive.pack(anchor=tk.CENTER, side="left",  padx=0, ipadx=30)




# create a frame widget with a gray background color
frame = Frame(root, bg="black", width=400)
frame.pack(fill=BOTH, expand=YES)





###################################################### START PFD ######################################################


# Create an Image widget to display the image
pil_image = Image.open("C:\\Users\\ADMIN\\Downloads\\pfd4.jpg")
pil_image = pil_image.resize((450, 420))

########## events ##############
def move_image(event, planeNumber):
    global y_offset_right
    global y_offset1
    x, y = canvas_button.coords(canvas_image223)
    x1, y1 = canvas_button_speed.coords(canvas_image229)
    global mode_tanker
    if mode_tanker == "manual":
        if planeNumber == 1:
            if event == "Up":
                global y_offset
                y_offset -= 1
                #y_offset_right = 90
                if(abs(y_offset-y_offset1)<2):
                    tcas_button_value.set("■ ↑ : " + str(y_offset1-y_offset))
                else:
                    tcas_button_value.set("● ↑ : " + str(y_offset1 - y_offset))
            elif event == "Down":
                y_offset += 1
                #y_offset_right = 90
                if (abs(y_offset - y_offset1) < 2):
                    tcas_button_value.set("■ ↓ : " + str(y_offset1 - y_offset))
                else:
                    tcas_button_value.set("● ↓ : " + str(y_offset1 - y_offset))
            elif event == "Right":
                y_offset_right -=1
        elif planeNumber == 2:
            #print("palne number : " , planeNumber)
            if event.char == "w":
                y -= 5  # pfd
                y1 += 1
                y_offset -= 1
                if (abs(y_offset - y_offset1) < 5):
                    tcas_button_value.set("■ - : " + str(y_offset1 - y_offset))
                else:
                    tcas_button_value.set("● - : " + str(y_offset1 - y_offset))
            elif event.char == "s":
                y += 5
                y1 += 1
                y_offset += 1
                if (abs(y_offset - y_offset1) < 5):
                    tcas_button_value.set("■ - : " + str(y_offset1 - y_offset))
                else:
                    tcas_button_value.set("● - : " + str(y_offset1 - y_offset))
            elif event.char == "d":
                y1 -= 1
                y_offset_right -=1
            canvas_button.coords(canvas_image223, x, y)
            canvas_button_speed.coords(canvas_image229, x1, y1)

            cropped = pil_image.crop((x_offset, y_offset, x_offset + canvas_width, y_offset + canvas_height))
            photo = ImageTk.PhotoImage(cropped)
            canvas1.itemconfig(canvas_image, image=photo)
            canvas1.image = photo  # keep a reference to prevent garbage collection

        #second plane
        cropped1 = pil_image.crop((x_offset1, y_offset1, x_offset1 + canvas_width1, y_offset1 + canvas_height1))
        photo = ImageTk.PhotoImage(cropped1)
        #PFD2 changes
        #canvas2.itemconfig(canvas_image, image=photo)
        #canvas2.image = photo  # keep a reference to prevent garbage collection

        #altitude bar
        ##cropped22 = grade_bar_image.crop((x_offset-120, y_offset+200, x_offset-120 + canvas_width, y_offset+200 + canvas_height))
        ##photo = ImageTk.PhotoImage(cropped22)
        ##canvas_button.itemconfig(canvas_image22, image=photo)
        ##canvas_button.image = photo  # keep a reference to prevent garbage collection


        # speed bar
        ##cropped33 = grade_bar_image.crop((x_offset_right - 90, y_offset_right + 200, x_offset_right - 90 + canvas_width, y_offset_right + 200 + canvas_height))
        ##photo = ImageTk.PhotoImage(cropped33)
        ##canvas_button_speed.itemconfig(canvas_image_33, image=photo)
        ##canvas_button_speed.image = photo  # keep a reference to prevent garbage collection
################# PFD DYNAMIC IMAGES ############################

# set the size of the viewable region
canvas_width = 200
canvas_height = 200

# set the initial offset to (0, 0)
x_offset = 120
y_offset = 63

#second plane
# set the size of the viewable region
canvas_width1 = 200
canvas_height1 = 200

# set the initial offset to (0, 0)
x_offset1 = 120
y_offset1 = 40

# set the initial offset to (0, 0)
x_offset_right = 90
y_offset_right = 40
# create the canvas

###################################### PFD1 ALTITUDE #########################################
canvas_button = tk.Canvas(frame, width=70, height=250, bg='black', borderwidth=0, highlightthickness=0)
grade_bar_image = Image.open("C:\\Users\\ADMIN\\Downloads\\indice.jpg")
grade_bar_image = grade_bar_image.resize((70, 250))
#cropped22 = grade_bar_image.crop((x_offset-120, y_offset+200, x_offset-120 + canvas_width, y_offset+200 + canvas_height))
photo22 = ImageTk.PhotoImage(grade_bar_image)
canvas_image22 = canvas_button.create_image(0, 0, anchor=NW, image=photo22)
# create a button on the canvas
# Create the Altitude button and add it to the frame
pfd_indicator = Image.open("C:\\Users\\ADMIN\\Downloads\\pfdIndicator.png")
pfd_indicator = pfd_indicator.resize((150, 110))
pfd_indicator = pfd_indicator.rotate(180)
#cropped22 = grade_bar_image.crop((x_offset-120, y_offset+200, x_offset-120 + canvas_width, y_offset+200 + canvas_height))
photo23 = ImageTk.PhotoImage(pfd_indicator)
canvas_image223 = canvas_button.create_image(-40, 50, anchor=NW, image=photo23)
canvas_button.pack(side=tk.LEFT)

##################################### PFD1 image #################################################
canvas1 = Canvas(frame, width=canvas_width, height=canvas_height, background="black", borderwidth=0, highlightthickness=0)
cropped = pil_image.crop((x_offset, y_offset, x_offset + canvas_width, y_offset + canvas_height))
photovv = ImageTk.PhotoImage(cropped)
canvas_image = canvas1.create_image(0, 0, anchor=NW, image=photovv)
# Load the foreground image using PIL
pfd1_fg_image = Image.open("C:\\Users\\ADMIN\\Downloads\\pfd_adi_mask.png")
pfd1_fg_photo = ImageTk.PhotoImage(pfd1_fg_image)
# Add the foreground image to the canvas, above the background image
canvas1.create_image(-43, 0, anchor=NW, image=pfd1_fg_photo)

pfd1_fg_image2 = Image.open("C:\\Users\\ADMIN\\Downloads\\cadre.png")
pfd1_fg_image2 = pfd1_fg_image2.resize((230, 245))
pfd1_fg_photo2 = ImageTk.PhotoImage(pfd1_fg_image2)
# Add the foreground image to the canvas, above the background image
canvas1.create_image(-13, -15, anchor=NW, image=pfd1_fg_photo2)
canvas1.pack(side="left", padx=10, pady=0)


####################################### PFD1 SPEED ###############################################
####################################### PFD1 SPEED ###############################################
canvas_button_speed = tk.Canvas(frame, width=70, height=250, bg='black', borderwidth=0, highlightthickness=0)
grade_bar_image = Image.open("C:\\Users\\ADMIN\\Downloads\\indice.jpg")
grade_bar_image = grade_bar_image.resize((70, 250))
#cropped33 = grade_bar_image.crop((x_offset_right-90, y_offset_right+200, x_offset_right-90 + canvas_width, y_offset_right+200 + canvas_height))
photo33 = ImageTk.PhotoImage(grade_bar_image)
canvas_image_33 = canvas_button_speed.create_image(0, 0, anchor=NW, image=photo33)
# Create the Speed button and add it to the frame
pfd_indicator1 = Image.open("C:\\Users\\ADMIN\\Downloads\\pfdIndicator.png")
pfd_indicator1 = pfd_indicator1.resize((150, 110))
pfd_indicator1 = pfd_indicator1.rotate(180)
#cropped22 = grade_bar_image.crop((x_offset-120, y_offset+200, x_offset-120 + canvas_width, y_offset+200 + canvas_height))
photo239 = ImageTk.PhotoImage(pfd_indicator1)
canvas_image229 = canvas_button_speed.create_image(-40, 50, anchor=NW, image=photo239)

#button_window_11 = canvas_button_speed.create_window(0, 0, anchor=tk.NW, window=button)
canvas_button_speed.pack(side="left", padx=0, pady=0)


############################################ END PFD1 #####################################################

############################################ START TCAS ###################################################

other_plane_position = y_offset1-y_offset
tcas_button_value = tk.StringVar(value="↑" + str(other_plane_position))

#TCAS
canvas1_1 = Canvas(frame, width=250, height=200, bg="black", borderwidth=0, highlightthickness=0)
tcas_button = tk.Button(canvas1_1, textvariable=tcas_button_value, bg='black', fg="red", font=("Arial", 10), width=6, height=2)

btn_id = canvas1_1.create_window(150, 150, anchor="nw", window=tcas_button)
image = Image.open("C:\\Users\\ADMIN\\Downloads\\tcas.png")
image.resize((650, 250))
photo1_1 = ImageTk.PhotoImage(image)
canvas_image1_1 = canvas1_1.create_image(0, 0, anchor=NW, image=photo1_1)
#plane icon
plane_position = tk.Button(canvas1_1, text="✈", bg="black", fg="yellow", font=("Arial", 12), width=3, height=1)
plane_position.config(bd=0, highlightthickness=0)
canvas1_1.create_window(90, 170, anchor="nw", window=plane_position)
canvas1_1.pack(side="left", padx=0, pady=0)

# configure a function to change the text color of the button automatically
def change_text_color(btn, color):
    current_color = btn["fg"]
    if current_color == color:
        btn["fg"] = "white"
    elif current_color == "orange":
        btn["fg"] = "white"
        color = "orange"
    elif current_color == "lightblue":
        btn["fg"] = "white"
        color = "lightblue"
    else:
        btn["fg"] = color
    root.after(1000, lambda: change_text_color(btn, color))
    # call the function again after 500ms
change_text_color(plane_position, "yellow")
#change_text_color(button_send, "blue")
change_text_color(button_receive, "black")
#change_text_color(button_record, "black")
#change_text_color(tcas_button, "red")

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def change_tcas_position(userEvent):
    x1, y1 = canvas.coords(img1)
    x2, y2 = canvas.coords(img2)
    d = distance(x1, y1, x2, y2)
    if userEvent == "up" or userEvent == "down":
        if y1 > 270:
            canvas1_1.coords(btn_id, 150, 150)

        elif 170 < y1 < 270:
            canvas1_1.coords(btn_id, 100, 100)

        elif y1 <= 170:
            canvas1_1.coords(btn_id, 50, 50)

    if d >= 290:
        tcas_button.config(fg="lightblue", textvariable=tcas_button_value)
    elif 190 <= d < 290:
        tcas_button.config(fg="orange", textvariable=tcas_button_value)
    elif 90 <= d < 190:
        tcas_button.config(fg="red", textvariable=tcas_button_value)

tcas_button.config(command=change_tcas_position)
tcas_button.config(bd=0, highlightthickness=0)


#====================================  START ND ==========================================#
canvas_button_speed_plane2_nd = tk.Canvas(frame, width=80, height=350, bg="black", borderwidth=0, highlightthickness=0)
grade_bar_image_nd = Image.open("C:\\Users\\ADMIN\\Downloads\\nd1_grads.jpeg")
grade_bar_image_nd = grade_bar_image_nd.resize((80, 240))
graduated_bar_nd = ImageTk.PhotoImage(grade_bar_image_nd)
canvas_image_33_plane2 = canvas_button_speed_plane2_nd.create_image(0, 12, anchor=NW, image=graduated_bar_nd)
# create the button shape
#button_nd = canvas_button_speed_plane2_nd.create_arc(15, 175, 125, 225, fill='gray', tags=('nd_speed_button',))
# create the button shape
canvas_button_speed_plane2_nd.pack(side=LEFT)

nd_point_size = 2
nd_trail_length = 50
nd_trail_width = 1

nd_point_x = (nd_point_size // 2)
nd_point_y = (200 // 2)


def move_point():
    global nd_point_x, nd_point_y
    nd_canvas.focus_set()  # Set the focus on the canvas widget
    #nd_trail_points = [nd_point_x, nd_point_y, nd_point_x - nd_trail_length, nd_point_y]
    #canvas.create_line(trail_points, width=trail_width)
    nd_canvas.create_oval(nd_point_x - nd_point_size, nd_point_y - nd_point_size, nd_point_x + nd_point_size, nd_point_y + nd_point_size, fill='blue', outline="")
    nd_point_x += 1
    nd_canvas_x, nd_canvas_y = 200 // 2 - nd_point_x, 0
    nd_canvas.scan_dragto(nd_canvas_x, nd_canvas_y, gain=1)
    nd_canvas.after(150, move_point)

def move_up(event):
    global nd_point_y
    nd_point_y = max(nd_point_y - 1, nd_point_size // 2)

def move_down(event):
    global nd_point_y
    nd_point_y = min(nd_point_y + 1, 200 - nd_point_size // 2)
# create parent frame for the two horizontal canvas
nd_canvas = tk.Canvas(frame, width=350, height=350, borderwidth=0, highlightthickness=0)

# Load an image
nd_image = Image.open("C:\\Users\\ADMIN\\Downloads\\nd_image.png")
nd_image = nd_image.resize((2500, 285))
nd_tk_image = ImageTk.PhotoImage(nd_image)

# Add the image to the canvas
nd_item = nd_canvas.create_image(0, 120, image=nd_tk_image)

# define the scrolling function
def scroll_nd_background():
   nd_canvas.move(nd_item, -0.1, 0)
   nd_canvas.after(100000, scroll_nd_background)

# start the scrolling
#scroll_nd_background()
nd_canvas.pack(side=tk.LEFT)
nd_canvas.bind('<w>', move_up)
nd_canvas.bind('<s>', move_down)
move_point()


#====================================  END ND ==========================================#


#====================================== START RADAR =======================================#
# Load the animated GIF image using PIL
radar_image = Image.open("C:\\Users\\ADMIN\\Desktop\\RTS_code\\data\\radar1.gif")
#nd_bg_image = Image.open("C:\\Users\\ADMIN\\Downloads\\nd_bg.gif")
# Create a list of photo images from the frames of the GIF animation
radar_photo_frames = []

try:
    while True:
        # Resize each frame to a new width and height
        radar_new_width = 300
        radar_new_height = 250
        radar_resized_image = radar_image.resize((radar_new_width, radar_new_height))
        # Create a PhotoImage object from the resized image
        radar_photo_frames.append(ImageTk.PhotoImage(radar_resized_image))

        radar_image.seek(len(radar_photo_frames))  # Move to the next frame
except EOFError:
    pass  # End of frames


# Create a canvas and add the first photo image to it
radar_canvas = Canvas(frame, width=radar_photo_frames[0].width(), height=radar_photo_frames[0].height(), bg="black", borderwidth=0, highlightthickness=0)
radar_canvas.pack()
radar_image_item = radar_canvas.create_image(0, 0, anchor=NW, image=radar_photo_frames[0])

# Define the button parameters
button_text_radar = ["↑ AAL375", button_value.get(), button_value1.get()]
button_text_radar1 = ["↑ FFD668", button_value_plane2.get(), button_value1_plane2.get()]
button_x, button_y = 100, 100
button_x1, button_y1 = 150, 150
button_padding = 5

# Create the button
button_radar = radar_canvas.create_text(button_x, button_y, text="\n".join(button_text_radar),
                            anchor="center", justify="center", width=100, fill="white")
button_radar1 = radar_canvas.create_text(button_x1, button_y1, text="\n".join(button_text_radar1),
                            anchor="center", justify="center", width=100, fill="lightBlue")




# Define a function to animate the GIF frames

# Define a function to animate the GIF frames
def animate_sky(frame_index):

    canvas.itemconfig(sky_image_item, image=sky_photo_frames[frame_index])
    root.after(100, animate_sky, (frame_index + 1) % len(sky_photo_frames))

def animate_radar(frame_index):
    radar_canvas.itemconfig(radar_image_item, image=radar_photo_frames[frame_index])
    root.after(50, animate_radar, (frame_index + 1) % len(radar_photo_frames))

# Start the animation
animate_sky(0)
animate_radar(0)











#====================================  START PFD2 ==========================================#
# create the canvas
#canvas_button_plane2 = tk.Canvas(root, width=70, height=150, bg='white')
#grade_bar_image = Image.open("C:\\Users\\ADMIN\\Downloads\\speed_altitude.png")
#grade_bar_image = grade_bar_image.resize((550, 500))
#cropped22_plane2  = grade_bar_image.crop((x_offset-120, y_offset+200, x_offset-120 + canvas_width, y_offset+200 + canvas_height))
##photo22_plane2  = ImageTk.PhotoImage(cropped22_plane2)
#canvas_image22_plane2  = canvas_button_plane2.create_image(0, 0, anchor=NW, image=photo22_plane2)
# create a button on the canvas
# Create the Altitude button and add it to the frame
#button11 = tk.Button(canvas_button_plane2, textvariable=button_value1_plane2, bg="gray", fg="lightGreen",
#                    activebackground="darkred", activeforeground="white",
#                    highlightbackground="black", highlightcolor="black",
#                    highlightthickness=2, width=10, height=1)
#button_window_1 = canvas_button_plane2.create_window(20, 10, anchor=tk.NW, window=button11)
#canvas_button_plane2.pack(side='left', padx=0, pady=0)
#canvas2 = Canvas(root, width=canvas_width1, height=canvas_height1)
#cropped1 = pil_image.crop((x_offset1, y_offset1, x_offset1 + canvas_width1, y_offset1 + canvas_height1))
#photo = ImageTk.PhotoImage(cropped1)
#canvas_image1 = canvas2.create_image(0, 0, anchor=NW, image=photo)
#canvas2.pack()

# speed Button
# create the canvas
#canvas_button_speed_plane2 = tk.Canvas(root, width=70, height=150, bg='white')
#grade_bar_image = Image.open("C:\\Users\\ADMIN\\Downloads\\speed_altitude.png")
#grade_bar_image = grade_bar_image.resize((550, 500))
#cropped33_plane2 = grade_bar_image.crop((x_offset_right-120, y_offset_right+200, x_offset_right-120 + canvas_width, y_offset_right+200 + canvas_height))
#photo33_plane2 = ImageTk.PhotoImage(cropped33_plane2)
#canvas_image_33_plane2 = canvas_button_speed_plane2.create_image(0, 0, anchor=NW, image=photo33)
# Create the Speed button and add it to the frame
#button = tk.Button(canvas_button_speed_plane2, textvariable=button_value_plane2, bg="gray", fg="black",
#                   activebackground="darkred", activeforeground="white",
#                   highlightbackground="black", highlightcolor="black",
#                   highlightthickness=2, width=10, height=1)
#button_window_11_plane2 = canvas_button_speed_plane2.create_window(0, 0, anchor=tk.NW, window=button)
#canvas_button_speed_plane2.pack()

#canvas_button.pack(side=tk.LEFT)
#canvas1.pack(side=tk.LEFT)
#canvas_button_speed.pack(side=tk.LEFT)
#canvas1_1.pack(side=tk.LEFT)
#canvas_button_plane2.pack(side=tk.LEFT)
#canvas2.pack(side=tk.LEFT)
#canvas_button_speed_plane2.pack(side=tk.LEFT)

#====================================  END PFD2 ==========================================#


#==================================== SPEED + ALTITUDE ===================================#
# Define a function to increase the value of the button
def increase_button_value(event, planeNumber):
    if (planeNumber == 1):
        current_value = int(button_value.get().split("Speed : ")[1])
        new_value = current_value + 1
        button_value.set("Speed : " + str(new_value))
    elif (planeNumber == 2):
        current_value = int(button_value_plane2.get().split("Speed : ")[1])
        new_value = current_value + 1
        button_value_plane2.set("Speed : " + str(new_value))

def increase_altitude(event, planeNumber):
    if (planeNumber == 1):
        current_altitude = int(button_value1.get().split("Altitude : ")[1])
        new_value1 = current_altitude + 2
        button_value1.set("Altitude : " + str(new_value1))
        button_value.set("Speed : " + str(0))
    elif planeNumber == 2:
        current_altitude = int(button_value1_plane2.get().split("Altitude : ")[1])
        new_value1 = current_altitude + 2
        button_value1_plane2.set("Altitude : " + str(new_value1))
        button_value_plane2.set("Speed : " + str(0))

def decrease_altitude(event, planeNumber):
    if (planeNumber == 1):
        current_altitude = int(button_value1.get().split("Altitude : ")[1])
        new_value1 = current_altitude - 2
        button_value1.set("Altitude : " + str(new_value1))
        button_value.set("Speed : " + str(0))
    elif planeNumber == 2:
        current_altitude = int(button_value1_plane2.get().split("Altitude : ")[1])
        new_value1 = current_altitude - 2
        button_value1_plane2.set("Altitude : " + str(new_value1))
        button_value_plane2.set("Speed : " + str(0))


#==================================== Sounds =================================#
def play_sound_atc():
   pygame.init()
   pygame.mixer.music.load("C:\\Users\\ADMIN\\Downloads\\atc.mp3")
   pygame.mixer.music.play()

def play_alarm_sound():
    pygame.init()
    pygame.mixer.music.load("C:\\Users\\ADMIN\\Downloads\\alarm.mp3")
    pygame.mixer.music.play()

def play_take_off_sound():
   pygame.init()
   pygame.mixer.music.load("C:\\Users\\ADMIN\\Downloads\\airplane-take-off-01.mp3")
   pygame.mixer.music.play()
#play_alarm_sound()
#play_take_off_sound()

#play_sound_atc()
#================================ EVENTS ==================================#
def move_rect(event):
    if mode_tanker == "manual":
        ####RADAR#######
        global button_x, button_y

        if event == "Right" and button_x <= 214:
            button_x += 1
        elif event == "Up" and 50 <= button_y:
            button_y -= 1
        elif event == "Down" and button_y <= 187:
            button_y += 1
        radar_canvas.coords(button_radar, button_x, button_y)
        # button_text_radar.append(button_text_radar.pop(0))
        button_text_radar[1] = button_value.get()
        button_text_radar[2] = button_value1.get()
        radar_canvas.itemconfigure(button_radar, text="\n".join(button_text_radar))


        move_image(event, 1)
        #move_plane(event)
        #move_button(event)
        ###########show_alert(event)
        if event == 'Up':
            canvas.move(img1, 0, -10)
            increase_altitude(event, 1)
            #play_take_off_sound()
            x1, y1 = canvas.coords(img1)
            #print(f"Image coordinates: ({x1}, {y1})")
            change_tcas_position("up")
            #rotate_image(event, "left")
        elif event == 'Down' :
            canvas.move(img1, 0, 10)
            decrease_altitude(event, 1)
            x1, y1 = canvas.coords(img1)
            #print(f"Image coordinates: ({x1}, {y1})")
            change_tcas_position("down")
        elif event == 'Right':
            canvas.move(img1, 10, 0)
            increase_button_value(event, 1)
            x1, y1 = canvas.coords(img1)
            #print(f"Image coordinates: ({x1}, {y1})")
            change_tcas_position("right")
            # Get the coordinates of the image
            #play_sound()


def move_rect_second_plane(event):
    if mode_plane == "manual":
        global button_x1, button_y1

        move_image(event, 2)
        if event.char == 'w':
            canvas.move(img2, 0, -10)
            increase_altitude(event, 2)
            change_tcas_position('w')
            x2, y2 = canvas.coords(img2)
            print(f"Image coordinates: ({x2}, {y2})")
            #moves_lines3(event)
            #play_take_off_sound()
        elif event.char == 's':
            change_tcas_position('s')
            canvas.move(img2, 0, 10)
            decrease_altitude(event, 2)
            x2, y2 = canvas.coords(img2)
            print(f"Image coordinates: ({x2}, {y2})")
           # moves_lines3(event)
        elif event.char == 'd':
           # move_lines(event)
            canvas.move(img2, 10, 0)
            increase_button_value(event, 2)

        #elif event.char == "a":
           # move_lines(event)

        if event.char == "d" and button_x1 <= 214:
            button_x1 += 1
        elif event.char == "w" and 50 <= button_y1:
            button_y1 -= 1
        elif event.char == "s" and button_y1 <= 187:
            button_y1 += 1
        radar_canvas.coords(button_radar1, button_x1, button_y1)
        # button_text_radar.append(button_text_radar.pop(0))
        button_text_radar1[1] = button_value_plane2.get()
        button_text_radar1[2] = button_value1_plane2.get()
        radar_canvas.itemconfigure(button_radar1, text="\n".join(button_text_radar1))


def show_alert(event):
    global y_offset
    global y_offset1
    if y_offset == y_offset1:
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Alert", "Same layer")

canvas.bind_all('<Up>', move_rect)
canvas.bind_all('<Down>', move_rect)
canvas.bind_all('<Left>', move_rect)
canvas.bind_all('<Right>', move_rect)
canvas.bind_all('<w>', move_rect_second_plane)
canvas.bind_all('<s>', move_rect_second_plane)
canvas.bind_all('<a>', move_rect_second_plane)
canvas.bind_all('<d>', move_rect_second_plane)
canvas.bind_all('<I>', moves_lines2)
canvas.bind_all('<D>', moves_lines2)
canvas.bind_all('<a>', move_lines)
canvas.bind_all('<g>', moves_lines3)
canvas.bind_all('<v>', moves_lines3)
canvas.bind_all("<KeyPress-K>", plane_flight_mode)
canvas.bind_all("<KeyPress-L>", plane_flight_mode)

#canvas.bind('<Motion>', callback)
#canvas.bind('<Motion>', show_alert)



#=================================================== Fueling ===================================================#

fueling = None
def Fueling(event):

    global fueling
    global mode_tanker
    global mode_plane
    x1, y1 = canvas.coords(img1)
    x2, y2 = canvas.coords(img2)
    d = distance(x1, y1, x2, y2)
    if event == 'F' and fueling == None:
        print("distance = ", d)
        if 0 <= d < 190:

            mode_tanker = "automatic"
            mode_plane = "automatic"
            play_sound("La distance est parfaite, ravitaillement avion en cours")
            fueling = canvas.create_line(x1, y1 + 40, x2, y2 + 30, fill="black", width=2)
        else:
            play_sound("Rapprochez vous s'il vous plait, l'autre avion est encore loin")
    # animate_fueling(canvas, fueling, 50, 50, 200, 200)
    # wait_and_do_something()
    # canvas.coords(fueling,x1+20,y1+40,(x2+x1)/1.5,(y2+y1)/1.5)
    if event == 'E':
        if 0 <= d < 190:
            mode_tanker = "manual"
            mode_plane = "manual"
            canvas.delete(fueling)
            play_sound("Opération terminée avec succé, merci")
            fueling = None

def animate_fueling(canvas, fueling, x1, y1, x2, y2, i=0):
    x2,y2 = canvas.coords(img2)
    x1,y1 = canvas.coords(img1)
    canvas.coords(fueling, x1 + 30, y1 + 40, x1 - i, y1 + 40)

    # If the line hasn't reached the endpoint yet, schedule the next update
    if i < 40:
        canvas.after(50, animate_fueling, canvas, fueling, x1, y1, x2, y2, i + 1)
    else:
        angle = math.pi / 8
        steps = 20
        cx, cy = x1 + 30, y1 + 40  # center of rotation

        # Rotate the line from 0 to 45 degrees with animation
        for i in range(steps + 1):
            # Calculate the new coordinates of the second point of the line
            x2r = (x1+x2)/3
            y2r = (x1+x2)/3

            #x2r = cx + (x2 - cx / 5) * math.cos(angle * i / steps) - (y2 + cy) * math.sin(angle * i / steps)
            #5y2r = cy + (x2 - cx / 5) * math.sin(angle * i / steps) + (y2 - cy / 5) * math.cos(angle * i / steps)

            # Update the coordinates of the line
            canvas.coords(fueling, x1 + 30, y1 + 40, x2r, y2r)

            # Update the canvas and create a delay between each step of the animation
            canvas.update()
            canvas.after(50)

canvas.bind_all('<F>',Fueling)
canvas.bind_all('<E>',Fueling)


#====================== KAFKA section =======================#
def generate_data():
    plane_position_x, plane_position_y = canvas.coords(img2)
    move_lines()
    moves_lines2()
    moves_lines3()
    speed_sensor = (plane_position_x - 20) + 150
    current_altitude = int(button_value1_plane2.get().split("Altitude : ")[1])

    # Replace this with your own data generation logic
    #return " Y : " + str(current:altitude) + " Tempearture (°F)  " + str(angle3) + " Fuel (%) : " + str(angle1) + " Pressure (inHg)" + str(angle2) + " Speed (mph) : " + str(speed_sensor) + " Oil Pressure (PSI)" + str(angle4)
    return "FFD668" + "|" + str(current_altitude) + "|" + str(
        angle3) + "|" + str(angle1) + "|" + str(angle2) + "|" + str(
        speed_sensor) + "|" + str(angle4)

# Create the KafkaProducer instance
producer = KafkaProducer('localhost:9092')  # Replace with your Kafka broker address

# Start the Kafka producer in a separate thread
kafka_thread = threading.Thread(target=producer.start_sending_data, args=('sensorsTopic', generate_data))
kafka_thread.daemon = True
kafka_thread.start()












#================================ SOCKET =========================================#



def receive_messages():
    while True:
        message, address = sock.recvfrom(1024)
        print(message.decode())
        event = tk.Event()
        event.char = message.decode()

        if message.decode() == 'Up':
            move_rect(message.decode())
            #move_lines(message.decode())
            #moves_lines3(message.decode())

        elif message.decode() == "Down":
            move_rect(message.decode())
            #move_lines(message.decode())
            #moves_lines3(message.decode())
        elif message.decode() == 'Right':
            move_rect(message.decode())
            #move_lines(message.decode())
            #moves_lines3(message.decode())
        elif (message.decode() == "F" or message.decode() == "E"):
            Fueling(message.decode())
        elif message.decode() == 'x':
            rotate_right(message.decode())
        elif message.decode() == 'y':
            rotate_left(message.decode())
        elif message.decode() == 'A' or message.decode() == "M":
            tanker_flight_mode(message.decode())

receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

def print_key(event):
    if event.keysym.isprintable() or event.keysym.startswith('F') or event.keysym.startswith('E') or event.keysym.startswith('K') or event.keysym.startswith('L') or event.keysym.startswith('w') or event.keysym.startswith('s') or event.keysym.startswith('d') or event.keysym.startswith(
        'i') or event.keysym.startswith('k') or event.keysym.startswith('j') or event.keysym.startswith('l') or event.keysym.startswith('c') or event.keysym.startswith('v'):
        print(event.keysym.encode('utf-8'))
        sock.sendto(event.keysym.encode('utf-8'), ('localhost', 8888))



root.bind('<KeyPress>', print_key)
root.mainloop()
# Stop the Kafka producer when the GUI is closed
producer.stop_sending_data()