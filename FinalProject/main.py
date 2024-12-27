from tkinter import *
from functools import partial
from user import UserSystem
from admin import AdminSystem

win = Tk()
win.title("Library Management System")
win.configure(bg="midnight blue")
win.geometry(
    f"1280x700+{(win.winfo_screenwidth() - 1280) // 2}+{(win.winfo_screenheight() - 700) // 2}"
)

main_frame = Frame(win, bg="midnight blue")
welcome_label = Label(
    main_frame,
    text="Library Management System",
    fg="white",
    font=("Tahoma", 18, "bold"),
    bg="midnight blue"
)
menu_container = Frame(
    main_frame,
    relief="ridge",
    bd=3,
    width=325,
    height=200,
    bg="azure3"
)

main_frame.pack()
welcome_label.pack(pady=30)
menu_container.pack_propagate(False)
menu_container.pack(pady=100, anchor="center")

user_system = UserSystem(win, main_frame)
admin_system = AdminSystem(win, main_frame)

# handle user button click
def user_func():
    main_frame.pack_forget()
    user_system.user_frame.pack()

# handle admin button click
def admin_func():
    admin_system.show_admin_login()

user_btn = Button(
    menu_container,
    text="User",
    font=("Tahoma", 14, "bold"),
    padx=5,
    pady=10,
    bg="blue4",
    fg="white",
    width=20,
    relief="raised",
    command=user_func
)
admin_btn = Button(
    menu_container,
    text="Admin",
    font=("Tahoma", 14, "bold"),
    padx=5,
    pady=10,
    bg="blue4",
    fg="white",
    width=20,
    relief="raised",
    command=admin_func
)
exit_btn = Button(
    main_frame,
    text="Exit",
    font=("Tahoma", 14, "bold"),
    padx=5,
    pady=10,
    bg="gray",
    width=10,
    fg="white",
    relief="raised",
    command=win.quit
)

user_btn.pack(pady=(20, 20))
admin_btn.pack(pady=(0, 20))
exit_btn.pack(pady=(0, 40))

win.mainloop()
