# from tkinter import * 
# from PIL import Image, ImageTk 
# from tkinter.filedialog import askopenfilename
# import cv2
# from tkinter import messagebox
# root = Tk()
# sw = root.winfo_screenwidth()
# sh = root.winfo_screenheight()
# root.geometry(f'{sw}x{sh}')
# root.title('Photo Meow')
# filll= 'black'
# num = 200
# def paintingg():
#     global bg_label2,bg_image2
    
#     if 'bg_canvas' in globals():
#         bg_canvas.destroy() 
    
    

#     bg_canvas = Canvas(root, width=iww, height=ihh)
#     bg_canvas.place(anchor='center', relx=0.5, rely=0.5)
#     bg_canvas.create_image(0, 0, image=bg_image2, anchor='nw')

#     prev_x, prev_y = None, None  # برای ذخیره‌ی نقطه‌ی قبلی

#     def draw(event):
#         global prev_x, prev_y
#         prev_x, prev_y = event.x, event.y

#         if prev_x and prev_y:
#             bg_canvas.create_line(prev_x, prev_y, event.x, event.y, fill=filll, width=num, capstyle=ROUND, smooth=True)

#     def reset_coords(event):
#         global prev_x, prev_y
#         prev_x, prev_y = None, None

#     # اتصال ایونت‌ها
#     bg_canvas.bind('<B1-Motion>', draw)
#     bg_canvas.bind('<ButtonRelease-1>', reset_coords)
# #30 .47 . 20 . 45
# # def painting_setting(event):
# #     global color_palette , filll,x_start,btn_width,btn_height,gap,set_color
# #     color_palette = ['#D50000','#9C0D0D','#C41475','#3E2C82','#1D53A0','#038D91','#118E2E','#87C310','#F2EB1A']
# #     x_start = 40
# #     btn_width = 23
# #     gap = 0  # اگه فاصله خواستی، مقدارشو زیاد کن
# # خخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخخ
# #     btn_height = 45
    
# # def painting_setting(event):
# #     global filll
# #     color_palette = ['#D50000','#9C0D0D','#C41475','#3E2C82','#1D53A0','#038D91','#118E2E','#87C310','#F2EB1A']
    
# #     xx1 = 40
# #     xx2 = 63
# #     for i in range(len(color_palette)):
# #     #     if xx2== 0:
# #     #         pass
# #         if xx1 <= event.x <= xx2 and 20 <= event.y <= 65:
# #             filll = color_palette[i]
# #     #     else:
# #     #         pass
# #         xx1 = xx2
# #         xx2+=23

# def painting_setting(event):
#     # لیبل زمینه برای دکمه‌ها
    

#     # رنگ‌ها همونایی که گفتی:
#     color_palette = ['#D50000','#9C0D0D','#C41475','#3E2C82','#1D53A0','#038D91','#118E2E','#87C310','#F2EB1A']

#     def set_color(index):
#         global filll
#         filll = color_palette[index]

#     # موقعیت اولیه:
#     xx1 = 40
#     btn_width = 23
#     btn_height = 45
#     y_pos = 20

#     # ساخت دکمه‌ها با حلقه مثل painting_setting:
#     for i in range(len(color_palette)):
#         btn = Button(tbp_label, bg=color_palette[i], command=lambda i=i: set_color(i),
#                     relief=FLAT, bd=0)
#         btn.place(x=xx1, y=y_pos, width=btn_width, height=btn_height)
#         xx1 += btn_width  # برای دکمه بعدی
    
# Image_open_lbl = 'photos\\a3.jpg'
# bg_image2 = Image.open(str(Image_open_lbl))
# bg_image3 = Image.open('photos\\wall3.jpg')
# tbp = Image.open('photos\\painting.jpg')
# tbp = tbp.resize((550 ,140))
# tbp = ImageTk.PhotoImage(tbp)
# tbp_label = Label(root, image=tbp)
# tbp_label.place(x=20,y=20)
# Button(text='',bg = 'red').place(x=67,y=65)
# tbp_label.bind("<Button-1>", painting_setting)
# iw = bg_image2.width/10
# ih = bg_image2.height/10

# bg_image2 = bg_image2.resize((int(iw) , int(ih)))
# iww, ihh = bg_image2.size
# bg_image2 = ImageTk.PhotoImage(bg_image2)
# bg_label2 = Label(root, image=bg_image2)
# bg_label2.place(anchor='center',relx=0.5, rely=0.5)

# paintingg()






# root.mainloop()

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
options = ['#D50000']
dropdown = ttk.Combobox(root,values=options)
dropdown.pack()
def show():
    sel = dropdown.get()
    print(sel)
show()
root.mainloop()