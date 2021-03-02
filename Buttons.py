import tkinter as tk


def addition():
	a=40
	b=50
	add_num = a+b
	label.configure(text=str(add_num))

root = tk.Tk()
root.title("Buttons in Tkinter")
root.geometry("500x400")

button = tk.Button(root,text="Add Button",command=addition)
button.pack(padx=20,pady=20)

label = tk.Label(root,text="Hi ! I am a label")
label.pack(padx=20,pady=20)



root.mainloop()