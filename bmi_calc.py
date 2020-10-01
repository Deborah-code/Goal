from tkinter import *
from tkinter import messagebox

Screen = Tk()

Screen.geometry("400x400")
Screen.configure(background="#8B008B")
Screen.title("BMI Calculator")
Screen.resizable(width=False, height=False)

def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height
def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight



def calculate_bmi():
    '''
       This function calculates the result
    '''
    try:
        height = get_height()
        weight = get_weight()
        bmi = weight / (height**2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res =  name + "Your BMI is " + str(bmi) + name + "\nRemarks: Eat Some MEAT and more MEAT hunnay!!" 
            messagebox.showinfo("Result", res)
        elif bmi > 15.0 and bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: It's okay to eat yunno !"
            messagebox.showinfo("Result", res)
        elif bmi > 16.0 and bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Okay boo, we need some pounds, just a little more!"
            messagebox.showinfo("Result", res)
        elif bmi >= 18.5 and bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Damn boo, that body is banging!!!."
            messagebox.showinfo("Result", res)
        elif bmi > 25.0 and bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Please register at a gymn."
            messagebox.showinfo("Result", res)
        elif bmi > 30.0 and bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\n\nRemarks: You need an entire lifestyle change \n you cannot continue like this o!"
            messagebox.showinfo("Result", res)
        elif bmi > 35.0 and bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You need to buy a gym!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Ahh Its over dear, it is!!"
            messagebox.showinfo("Result", res)

#weightbox
Weight_label = Label(Screen, bg="pink", text="Enter Weight (in kg):", bd=6,
               font=("Helvetica", 10, "bold"))
Weight_label.place(x=80, y=30)
ENTRY1 = Entry(Screen, bd=7, width=6)
ENTRY1.place(x=230, y=30)

#heightbox
Height_label = Label(Screen, bg="pink", text="Enter Height (in m):", bd=6,
               font=("Helvetica", 10, "bold"))
Height_label.place(x=80, y=80)

ENTRY2 = Entry(Screen, bd=7, width=6)
ENTRY2.place(x=230, y=80)

#namefeature
name_label = Label(Screen, bg = "pink", text = "Enter your name:", bd = 6,
                    font = ("Helvetica", 10, "bold"))
name_label.place(x=80, y = 130)
ENTRY3 = Entry(Screen, bd=7, width=15)
ENTRY3.place(x= 230, y = 130)

def get_name():
    name = str(ENTRY3.get())
    return name
   
name = get_name()

#buttoncommand
BUTTON = Button(bg="#FF1493", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
                font=("Helvetica", 20, "bold"))
BUTTON.grid(row=3, column=0, sticky=W)
BUTTON.place(x=120, y=250)
Screen.mainloop()

#add name feature
