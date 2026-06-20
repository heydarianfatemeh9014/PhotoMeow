from tkinter import * 
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import colorsys
from tkinter.filedialog import askopenfilename
import cv2
from tkinter import messagebox
root = Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(f'{sw}x{sh}')
root.title('Photo Meow')
filll= 'black'


color_menu = None

num = 200
def paintingg():
    global bg_label2,bg_image2
    
    if 'bg_canvas' in globals():
        bg_canvas.destroy() 
    
    

    bg_canvas = Canvas(root, width=iww, height=ihh)
    bg_canvas.place(anchor='center', relx=0.5, rely=0.5)
    bg_canvas.create_image(0, 0, image=bg_image2, anchor='nw')

    prev_x, prev_y = None, None  # برای ذخیره‌ی نقطه‌ی قبلی

    def draw(event):
        global prev_x, prev_y
        prev_x, prev_y = event.x, event.y

        if prev_x and prev_y:
            bg_canvas.create_line(prev_x, prev_y, event.x, event.y, fill=filll, width=num, capstyle=ROUND, smooth=True)

    def reset_coords(event):
        global prev_x, prev_y
        prev_x, prev_y = None, None

    # اتصال ایونت‌ها
    bg_canvas.bind('<B1-Motion>', draw)
    bg_canvas.bind('<ButtonRelease-1>', reset_coords)



# def painting_setting(event):
#     global filll
#     color_palette = ['blue','red']
    
#     xx1 = 1
#     xx2 = 6
#     for i in range(len(color_palette)):
#     #     if xx2== 0:
#     #         pass
#         if xx1 <= event.x <= xx2 and 17 <= event.y <= 62:
#             filll = color_palette[i]
#     #     else:
#     #         pass
#         xx1 = xx2
#         xx2+=5
filll = 'black'
color_palette = []

for i in range(500):
    h = i / 500          # Hue
    s = 0.65             # Saturation (نرم، نه جیغ)
    v = 0.95             # Brightness
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    color_palette.append(
        '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
    )


color_menu = None

def open_color_menu(x, y):
    global color_menu, filll

    if color_menu:
        color_menu.destroy()
        color_menu = None
        return

    color_menu = Frame(
        root,
        bg='#2b2b2b',
        bd=0,
        highlightthickness=0
    )
    color_menu.place(x=x, y=y)

    size = 40
    cols = 3

    for i, c in enumerate(color_palette):
        btn = Canvas(
            color_menu,
            width=size,
            height=size,
            bg=c,
            highlightthickness=0
        )
        btn.grid(row=i//cols, column=i%cols, padx=6, pady=6)

        def select_color(color=c):
            global filll, color_menu
            filll = color
            color_menu.destroy()
            color_menu = None

        btn.bind("<Button-1>", lambda e, col=c: select_color(col))

def painting_setting(event):
    open_color_menu(event.x_root - 40, event.y_root + 20)


    # اگر قبلاً ساخته شده، پاکش کن
    try:
        pass
    except:
        pass

    

    

    



    


def show_color_palette():
    global palette_frame, filll

    try:
        palette_frame.destroy()
    except:
        pass

    palette_frame = Frame(
        root,
        bg='#1f1f1f',
        width=600,
        height=500
    )
    palette_frame.place(x=20, y=20)

    size = 20
    cols = 25

    for i, c in enumerate(color_palette):
        btn = Canvas(
            palette_frame,
            width=size,
            height=size,
            bg=c,
            highlightthickness=0
        )
        btn.place(
            x=(i % cols) * size,
            y=(i // cols) * size
        )

        def select_color(color=c):
            global filll
            filll = color

        btn.bind("<Button-1>", lambda e, col=c: select_color(col))

def tools(event):
        global tbp_label,tbp
        if 0 <= event.x <= 200 and 0 <= event.y <= 70:
            try:
                tbp_label.destroy()
            except:
                pass
            
            show_color_palette()
            paintingg()
        elif 0 <= event.x <= 200 and 70 <= event.y <= 140:
            try:
                tbp_label.destroy()
                palette_frame.destroy()
            except:
                pass
            
            

            tbp = Image.open('photos\\eraser.jpg')
            tbp = tbp.resize((550 ,140))
            tbp = ImageTk.PhotoImage(tbp)
            tbp_label = Label(root, image=tbp)
            tbp_label.place(x=20,y=20)
        
        elif 0 <= event.x <= 200 and 140 <= event.y <= 210:
            try:
                tbp_label.destroy()
            except:
                pass
            
            

            tbp = Image.open('photos\\zoom.jpg')
            tbp = tbp.resize((550 ,140))
            tbp = ImageTk.PhotoImage(tbp)
            tbp_label = Label(root, image=tbp)
            tbp_label.place(x=20,y=20)
        
        elif 0 <= event.x <= 200 and 210 <= event.y <= 280:
            try:
                tbp_label.destroy()
            except:
                pass
            
        elif 0 <= event.x <= 200 and 280 <= event.y <= 350:
            try:
                tbp_label.destroy()
            except:
                pass
            
            

            tbp = Image.open('photos\\text.jpg')
            tbp = tbp.resize((550 ,140))
            tbp = ImageTk.PhotoImage(tbp)
            tbp_label = Label(root, image=tbp)
            tbp_label.place(x=20,y=20)
        elif 0 <= event.x <= 200 and 350 <= event.y <= 420:
            try:
                tbp_label.destroy()
            except:
                pass
        elif 0 <= event.x <= 200 and 420 <= event.y <= 480:
            try:
                tbp_label.destroy()
            except:
                pass
            
            

            tbp = Image.open('photos\\select.jpg')
            tbp = tbp.resize((550 ,140))
            tbp = ImageTk.PhotoImage(tbp)
            tbp_label = Label(root, image=tbp)
            tbp_label.place(x=20,y=20)

bg_image = Image.open("photos\\wall1.jpg")
bg_image = bg_image.resize((sw , sh))
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
btn_des = None
def open_f():
    global Image_open_lbl,bg_label2,bg_image2,open_lbl,new_lbl,tb,bg_image3,bg_label3,iww,ihh
    
    Image_open_lbl = askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    bg_image2 = Image.open(str(Image_open_lbl))
    if bg_image2.width >= sw or bg_image2.height >= sh:
        messagebox.showerror(message='Image is too big!')
    else:
        global tb_label
        bg_label.destroy()
        
        iw = bg_image2.width/2
        ih = bg_image2.height/2
        # bg_image2 = bg_image2.resize((int(iw) , int(ih)))
        iww, ihh = bg_image2.size

        bg_image2 = ImageTk.PhotoImage(bg_image2)
        open_lbl.destroy()
        new_lbl.destroy()
        tb = Image.open('photos\\tool_bx.jpg')
        bg_image3 = Image.open('photos\\wall3.jpg')

        bg_image3 = bg_image3.resize((int(sw) , int(sh)))
        bg_image3 = ImageTk.PhotoImage(bg_image3)
        bg_label3 = Label(root, image=bg_image3)
        bg_label3.pack()

        tb = tb.resize((50 ,500))
        tb = ImageTk.PhotoImage(tb)
        tb_label = Label(root, image=tb)
        tb_label.place(x=1525,y=0)





        bg_label2 = Label(root, image=bg_image2)
        bg_label2.place(anchor='center',relx=0.5, rely=0.5)
        tb_label.bind("<Button-1>", tools)

def open_nf():
    
    global Image_open_lbl,bg_label2,bg_image2,open_lbl,new_lbl,bg_image3,tb,iww,ihh
    Image_open_lbl = 'photos\\a3.jpg'
    bg_label.destroy()
    bg_image2 = Image.open(str(Image_open_lbl))
    bg_image3 = Image.open('photos\\wall3.jpg')
    tb = Image.open('photos\\tool_bx.jpg')
    iw = bg_image2.width/10
    ih = bg_image2.height/10
    bg_image2 = bg_image2.resize((int(iw) , int(ih)))
    iww, ihh = bg_image2.size
    bg_image2 = ImageTk.PhotoImage(bg_image2)
    bg_image3 = bg_image3.resize((int(sw) , int(sh)))
    bg_image3 = ImageTk.PhotoImage(bg_image3)

    tb = tb.resize((50 ,500))
    tb = ImageTk.PhotoImage(tb)

    open_lbl.destroy()
    new_lbl.destroy()
    bg_label3 = Label(root, image=bg_image3)
    bg_label3.pack()
    
    tb_label = Label(root, image=tb)
    tb_label.place(x=1525,y=0)


    bg_label2 = Label(root, image=bg_image2)
    bg_label2.place(anchor='center',relx=0.5, rely=0.5)
    tb_label.bind("<Button-1>", tools)


def open_nf2():
    
    global Image_open_lbl,bg_label2,bg_image2,open_lbl,new_lbl,bg_image3,tb,iww,ihh
    Image_open_lbl = 'photos\\a4.jpg'
    bg_label.destroy()
    bg_image2 = Image.open(str(Image_open_lbl))
    bg_image3 = Image.open('photos\\wall3.jpg')
    tb = Image.open('photos\\tool_bx.jpg')
    iw = bg_image2.width/10
    ih = bg_image2.height/10
    bg_image2 = bg_image2.resize((int(iw) , int(ih)))
    iww, ihh = bg_image2.size
    bg_image2 = ImageTk.PhotoImage(bg_image2)

    bg_image3 = bg_image3.resize((int(sw) , int(sh)))
    bg_image3 = ImageTk.PhotoImage(bg_image3)

    tb = tb.resize((50 ,500))
    tb = ImageTk.PhotoImage(tb)

    open_lbl.destroy()
    new_lbl.destroy()
    
    bg_label3 = Label(root, image=bg_image3)
    bg_label3.pack()

    tb_label = Label(root, image=tb)
    tb_label.place(x=1525,y=0)


    bg_label2 = Label(root, image=bg_image2)
    bg_label2.place(anchor='center',relx=0.5, rely=0.5)
    tb_label.bind("<Button-1>", tools)




def open_nf3():
    
    global Image_open_lbl,bg_label2,bg_image2,open_lbl,new_lbl,bg_image3,tb,hidden_btn,tbp,tbp_label,iww,ihh
    Image_open_lbl = 'photos\\a5.jpg'
    hidden_btn = Button(root, text=" ")
    hidden_btn.place(x=1525, y=0, width=275, height=140)
    bg_label.destroy()
    bg_image2 = Image.open(str(Image_open_lbl))
    bg_image3 = Image.open('photos\\wall3.jpg')
    tb = Image.open('photos\\tool_bx.jpg')
    iw = bg_image2.width/10
    ih = bg_image2.height/10
    bg_image2 = bg_image2.resize((int(iw) , int(ih)))
    iww, ihh = bg_image2.size
    bg_image2 = ImageTk.PhotoImage(bg_image2)
    bg_image3 = bg_image3.resize((int(sw) , int(sh)))
    bg_image3 = ImageTk.PhotoImage(bg_image3)

    tb = tb.resize((50 ,500))
    tb = ImageTk.PhotoImage(tb)

    open_lbl.destroy()
    new_lbl.destroy()
    bg_label3 = Label(root, image=bg_image3)
    bg_label3.pack()
    # def hi():
    #     print('hi')
    # hidden_btn = Button(root, text=" ",command=hi)
    # hidden_btn.place(x=1525, y=0, width=275, height=70)

    tb_label = Label(root, image=tb)
    tb_label.place(x=1525,y=0)
    


    bg_label2 = Label(root, image=bg_image2)
    bg_label2.place(anchor='center',relx=0.5, rely=0.5)
    
            
            

            

            




    tb_label.bind("<Button-1>", tools)

def open_n():
    
    r2 = Toplevel(root)
    r2.geometry('1000x700')
    r2.title('New File')
    r2.resizable(False,False)

    bg_image3 = Image.open("photos\\wall2.jpg")
    bg_image3 = bg_image3.resize((1000 , 700))
    bg_image3 = ImageTk.PhotoImage(bg_image3)

    bg_label3 = Label(r2, image=bg_image3)
    bg_label3.pack()

    

    def on_click(event):
        if 40 <= event.x <= 240 and 40 <= event.y <= 140:

            r2.destroy()
            open_nf()
        elif 360 <= event.x <= 560 and 290 <= event.y <= 390:
            r2.destroy()
            open_nf2()
        elif 500 <= event.x <= 1000 and 410 <= event.y <= 910:

            r2.destroy()
            open_nf3()


    r2.bind("<Button-1>", on_click)

        


    



    r2.mainloop()
    
open_lbl = Button(root,text='Open File',bg='#f2f2f2',fg='gray',activebackground='#f2f2f2',activeforeground='gray',command= open_f ,font=('Meows',80))
open_lbl.place(x=780,y=250)
new_lbl = Button(root,text='New File',bg='#a7a7a7',fg='#f2f2f2',activebackground='#a7a7a7',command = open_n,activeforeground='#f2f2f2',font=('Meows',80))
new_lbl.place(x=790,y=540)

root.mainloop()