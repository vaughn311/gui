from tkinter import *
import os

USERS_FILE = "users.txt"
BOOKS_FILE = "books.txt"

def save_user(username, age, email, phone, password):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{age},{email},{phone},{password}\n")

def load_users(sorted_by_first_letter=False):
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        users = [line.strip().split(",") for line in f]
    if sorted_by_first_letter:
        users = quick_sort(users, key=lambda x: x[0])  # Sort by username (first element)
    return users

def load_books(sorted_by_first_letter=False):
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as f:
        books = [line.strip() for line in f]
    if sorted_by_first_letter:
        books = quick_sort(books, key=lambda x: x.split("|")[0]) #sort by book title
    return books

def save_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write(book + "\n")

def quick_sort(array, key=lambda x: x):    
    if len(array) <= 1:
        return array
    pivot = key(array[0])  # use the first element as the pivot
    less = [x for x in array[1:] if key(x) < pivot]
    equal = [x for x in array if key(x) == pivot]
    greater = [x for x in array[1:] if key(x) > pivot]
    return quick_sort(less, key) + equal + quick_sort(greater, key)


class UserSystem:
    def __init__(self, root, main_frame):
        self.root = root
        self.main_frame = main_frame
        self.borrowed_books_stack = []
        self.reserved_books_queue = []
        self.user_frame = Frame(self.root, bg="midnight blue")

        Label(self.user_frame, text="Log In/Sign Up", font=("Tahoma", 18, "bold"), fg="white", bg="midnight blue").pack(pady=20)

        user_container = Frame(self.user_frame, relief="ridge", bd=3, width=325, height=200, bg="azure3")
        user_container.pack_propagate(False)
        user_container.pack(pady=100, anchor="center")

        Button(user_container, text="Log In", font=("Tahoma", 14, "bold"), padx=5, pady=10, bg="blue4", width=20, fg="white", relief="raised", command=self.login_screen).pack(pady=(20, 20))
        Button(user_container, text="Sign Up", font=("Tahoma", 14, "bold"), padx=5, pady=10, bg="blue4", width=20, fg="white", relief="raised", command=self.signup_screen).pack()
        Button(self.user_frame, text="Back", font=("Tahoma", 14, "bold"), padx=5, pady=10, bg="gray", width=10, fg="white", relief="raised", command=self.go_to_main_menu).pack()

    def go_to_main_menu(self):
        self.user_frame.pack_forget()
        self.main_frame.pack()

    def signup_screen(self):
        self.user_frame.pack_forget()  
        signup_frame = Frame(self.root, bg="midnight blue")
        signup_frame.pack(fill=BOTH, expand=True)

        Label(signup_frame, text="Sign Up", font=("Tahoma", 18, "bold"), fg="white", bg="midnight blue").pack(pady=20)

        signup_container = Frame(signup_frame, relief="ridge", bd=3, width=325, height=425, bg="azure3")
        signup_container.pack_propagate(False)
        signup_container.pack(pady=25, anchor="center")

        Label(signup_container, text="Username:", font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=(10, 0))
        username_entry = Entry(signup_container, bg="gray64", font=("Tahoma", 14, "bold"))
        username_entry.pack()

        Label(signup_container, text="Age:", font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=(10, 0))
        age_entry = Entry(signup_container, bg="gray64", font=("Tahoma", 14, "bold"))
        age_entry.pack()

        Label(signup_container, text="Email:", font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=(10, 0))
        email_entry = Entry(signup_container, bg="gray64", font=("Tahoma", 14, "bold"))
        email_entry.pack()

        Label(signup_container, text="Phone:", font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=(10, 0))
        phone_entry = Entry(signup_container, bg="gray64", font=("Tahoma", 14))
        phone_entry.pack()

        Label(signup_container, text="Password:", font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=(10, 0))
        password_entry = Entry(signup_container, bg="gray64", font=("Tahoma", 14), show="*")
        password_entry.pack()

        def signup():
            username = username_entry.get()
            age = age_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            password = password_entry.get()

            if not all([username, age, email, phone, password]):
                Label(signup_container, text="All fields are required!", font=("Tahoma", 12), fg="red", bg="azure3").pack()
                return

            save_user(username, age, email, phone, password)
            Label(signup_container, text="Sign Up Successful!", font=("Tahoma", 12), fg="green", bg="midnight blue").pack()

        Button(signup_container, text="Sign Up", font=("Tahoma", 14, "bold"), bg="blue4", fg="white", command=signup).pack(pady=20)
        Button(signup_frame, text="Back", font=("Tahoma", 14, "bold"), width=10, bg="gray", fg="white", command=lambda: [signup_frame.pack_forget(), self.user_frame.pack()]).pack()

    def login_screen(self):
        self.user_frame.pack_forget()  
        login_frame = Frame(self.root, bg="midnight blue")
        login_frame.pack(fill=BOTH, expand=True)

        Label(login_frame, text="Log In", font=("Tahoma", 18, "bold"), fg="white", bg="midnight blue").pack(pady=20)

        login_frame_container = Frame(login_frame, relief="ridge", bd=3, width=325, height=250, bg="azure3")
        login_frame_container.pack_propagate(False)
        login_frame_container.pack(pady=100, anchor="center")

        Label(login_frame_container, text="Username:", font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=(10, 0))
        username_entry = Entry(login_frame_container, font=("Tahoma", 14), bg="gray64", relief="sunken")
        username_entry.pack()

        Label(login_frame_container, text="Password:", font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=(10, 0))
        password_entry = Entry(login_frame_container, font=("Tahoma", 14), show="*", bg="gray64", relief="sunken")
        password_entry.pack()

        def login():
            username = username_entry.get()
            password = password_entry.get()
            users = load_users()

            #verify username and password
            for user in users:
                if user[0] == username and user[4] == password:
                    login_frame.pack_forget()  
                    self.user_main_frame()  
                    return

            Label(login_frame, text="Invalid Credentials!", font=("Tahoma", 12), fg="red", bg="midnight blue").pack()

        Button(login_frame_container, text="Log In", font=("Tahoma", 14, "bold"), bg="blue4", padx=5, pady=10, width=10, fg="white", command=login).pack(pady=20)
        Button(login_frame, text="Back", font=("Tahoma", 14, "bold"), width=10, bg="gray", fg="white", command=lambda: [login_frame.pack_forget(), self.user_frame.pack()]).pack()

    def borrow_book(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        borrow_book_frame = Frame(self.root, bg="midnight blue")
        borrow_book_frame.pack(fill=BOTH, expand=True)

        Label(borrow_book_frame, text="Borrow a Book", font=("Tahoma", 18, "bold"),
              bg="midnight blue", fg="white").pack(pady=20)
        
        borrow_book_container = Frame(borrow_book_frame, relief="ridge", width=750, height=300, bg="azure3", bd=3)
        borrow_book_container.pack_propagate(False)
        borrow_book_container.pack(pady=70,  anchor="center")

        books = [book for book in load_books() if book not in self.reserved_books_queue]
        if books:
            Label(borrow_book_container, text="Available Books", font=("Tahoma", 14, "bold"),
                  bg="azure3", fg="black").pack(pady=10)

            for book in books:
                Button(borrow_book_container, text=book, font=("Tahoma", 12), width=70, bg="blue4", fg="white",
                       command=lambda b=book: self.confirm_borrow(b, borrow_book_frame)).pack(pady=5)
        else:
            Label(borrow_book_frame, text="No books available to borrow.", font=("Tahoma", 14, "bold"),
                  bg="midnight blue", fg="white").pack(pady=20)

        Button(borrow_book_frame, text="Back", font=("Tahoma", 14, "bold"),
               bg="gray", fg="white", command=lambda: [borrow_book_frame.pack_forget(), self.user_main_frame()]).pack(pady=20)

    def confirm_borrow(self, book, frame):
        #rdd the book to the borrowed_books_stack
        if book not in self.borrowed_books_stack:
            self.borrowed_books_stack.append(book)

            #remove the book from the available books
            books = load_books()
            books.remove(book)
            save_books(books)

            #refresh the borrow book frame
            for widget in frame.winfo_children():
                widget.destroy()

            Label(frame, text=f"You have borrowed the book: {book}", font=("Tahoma", 14, "bold"),
                  bg="midnight blue", fg="white").pack(pady=20)

            Button(frame, text="Back", font=("Tahoma", 14, "bold"),
                   bg="gray", fg="white", command=lambda: [frame.pack_forget(), self.user_main_frame()]).pack(pady=20)


    def return_book(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        #create the frame for returning books
        return_books_frame = Frame(self.root, bg="midnight blue")
        return_books_frame.pack(fill=BOTH, expand=True)

        return_book_container = Frame(return_books_frame, relief="ridge", width=750, height=300, bg="azure3", bd=3)
        return_book_container.pack_propagate(False)
        return_book_container.pack(pady=70,  anchor="center")

        #check if the borrowed_books_stack is empty
        if not self.borrowed_books_stack:
            Label(
                return_book_container, text="No books to return.", font=("Tahoma", 14, "bold"),
                fg="black", bg="azure3"
            ).pack(pady=20)

            Button(
                return_books_frame, text="Back", font=("Tahoma", 14, "bold"),
                bg="gray", fg="white", command=lambda: [return_books_frame.pack_forget(), self.user_main_frame()]
            ).pack(pady=20)
            return

        Label(
            return_book_container, text="Your Borrowed Books", font=("Tahoma", 18, "bold"),
            fg="black", bg="azure3"
        ).pack(pady=20)

        #display borrowed books
        for book in self.borrowed_books_stack:
            Button(
                return_book_container, text=book, font=("Tahoma", 14), fg="white", bg="blue4",
                command=lambda b=book: self.confirm_return(b, return_books_frame)
            ).pack(pady=5)

        Button(
            return_books_frame, text="Back", font=("Tahoma", 14, "bold"),
            bg="gray", fg="white", command=lambda: [return_books_frame.pack_forget(), self.user_main_frame()]
        ).pack(pady=20)
        
    def confirm_return(self, book, frame):
        if book in self.borrowed_books_stack:
            #add the book back to available books
            books = load_books()
            books.append(book)
            save_books(books)

            #remove the book from the borrowed books stack
            self.borrowed_books_stack.remove(book)

            for widget in frame.winfo_children():
                widget.destroy()

            Label(frame, text=f"You have returned the book: {book}", font=("Tahoma", 14, "bold"),
                  bg="midnight blue", fg="white").pack(pady=20)

            Button(frame, text="Back", font=("Tahoma", 14, "bold"),
                   bg="gray", fg="white", command=lambda: [frame.pack_forget(), self.user_main_frame()]).pack(pady=20)

    def reserve_book(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        #create a new frame for reserving books
        reserve_book_frame = Frame(self.root, bg="midnight blue")
        reserve_book_frame.pack(fill=BOTH, expand=True)

        Label(reserve_book_frame, text="Reserve a Book", font=("Tahoma", 18, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)
        reserve_book_container = Frame(reserve_book_frame, relief="ridge", width=750, height=300, bg="azure3", bd=3)
        reserve_book_container.pack_propagate(False)
        reserve_book_container.pack(pady=50,  anchor="center")

        self.reserve_message_label = Label(reserve_book_frame, text="", font=("Tahoma", 14, "bold"), 
                                           bg="midnight blue", fg="white")
        self.reserve_message_label.pack(pady=10)

        # Load books to display
        books = [book for book in load_books() if book not in self.reserved_books_queue]
        available_books = [book for book in books if book not in self.borrowed_books_stack and book not in self.reserved_books_queue]

        if available_books:
            Label(reserve_book_container, text="Available Books for Reservation", font=("Tahoma", 14, "bold"), 
                  bg="azure3", fg="black").pack(pady=10)

            # display books as a list with selection
            for book in available_books:
                Button(reserve_book_container, text=book, font=("Tahoma", 12), width=70, bg="blue4", fg="white",
                       command=lambda b=book: self.confirm_reserve(b, reserve_book_frame)).pack(pady=5)
        else:
            Label(reserve_book_frame, text="No books available for reservation.", font=("Tahoma", 14, "bold"), 
                  bg="azure3", fg="black").pack(pady=20)
        
        Button(reserve_book_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [reserve_book_frame.pack_forget(), self.user_main_frame()]).pack(pady=20)

    def confirm_reserve(self, book, frame):
        
        self.reserved_books_queue.append(book)

        # update the screen after canceling the reservation
        for widget in frame.winfo_children():
            widget.destroy()
      
        Label(frame, text=f"You have reserved the book: {book}", font=("Tahoma", 14, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)

        
        Button(frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [frame.pack_forget(), self.user_main_frame()]).pack(pady=20)

    def cancel_reservation(self):
        # clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        #create a frame for canceling reservations
        cancel_reservation_frame = Frame(self.root, bg="midnight blue")
        cancel_reservation_frame.pack(fill=BOTH, expand=True)
        Label(cancel_reservation_frame, text="Cancel a Reservation", font=("Tahoma", 18, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)

        cancel_reservation_container = Frame(cancel_reservation_frame, relief="ridge", width=750, height=300, bg="azure3", bd=3)
        cancel_reservation_container.pack_propagate(False)
        cancel_reservation_container.pack(pady=70,  anchor="center")


        # check if there are any reserved books
        if not self.reserved_books_queue:
            Label(cancel_reservation_container, text="No reserved books to cancel.", font=("Tahoma", 14, "bold"), 
                  bg="azure3", fg="black").pack(pady=20)

            # Back button to return to main menu
            Button(cancel_reservation_frame, text="Back", font=("Tahoma", 14, "bold"), 
                   bg="gray", fg="white", command=lambda: [cancel_reservation_frame.pack_forget(), self.user_main_frame()]).pack(pady=20)
            return

        Label(cancel_reservation_container, text="Your Reserved Books:", font=("Tahoma", 14, "bold"), 
              bg="azure3", fg="black").pack(pady=10)

        #display reserved books with cancel options
        for book in list(self.reserved_books_queue):  #convert to list for iteration
            Button(cancel_reservation_container, text=book, font=("Tahoma", 12), bg="blue4", fg="white", width=70,
                   command=lambda b=book: self.confirm_cancel_reservation(b, cancel_reservation_frame)).pack(pady=5)

        Button(cancel_reservation_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [cancel_reservation_frame.pack_forget(), self.user_main_frame()]).pack(pady=20)

    def confirm_cancel_reservation(self, book, frame):
        #remove the book from the reservation queue
        self.reserved_books_queue.remove(book)

        for widget in frame.winfo_children():
            widget.destroy()

        Label(frame, text=f"You have canceled the reservation for: {book}", font=("Tahoma", 14, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)

        Button(frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [frame.pack_forget(), self.user_main_frame()]).pack(pady=20)

    def search_book(self):
        #clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        #create a frame for searching books
        search_frame = Frame(self.root, bg="midnight blue")
        search_frame.pack(fill=BOTH, expand=True)

        Label(search_frame, text="Search for a Book", font=("Tahoma", 18, "bold"),
              bg="midnight blue", fg="white").pack(pady=20)
        search_container = Frame(search_frame, relief="ridge", width=750, height=350, bg="azure3", bd=3)
        search_container.pack_propagate(False)
        search_container.pack(pady=70, anchor="center")

        #dropdown menu to select search field
        field_var = StringVar(value="title")
        Label(search_container, text="Search by:", font=("Tahoma", 14), bg="azure3", fg="black").pack(pady=5)
        OptionMenu(search_container, field_var, "title", "author", "genre", "ISBN").pack(pady=5)

        search_entry = Entry(search_container, font=("Tahoma", 14), bg="gray64")
        search_entry.pack(pady=10)

        search_result_label = Label(search_container, text="", font=("Tahoma", 14, "bold"),
                                    bg="azure3", fg="black")
        search_result_label.pack(pady=10)

        def perform_search():
            query = search_entry.get().strip().lower()  #query for case-insensitive search
            field = field_var.get()
            raw_books = load_books()

            #parse books from raw lines into dictionaries
            books = []
            for line in raw_books:
                if "|" in line:
                    parts = line.split("|")
                    if len(parts) == 4:
                        books.append({
                            "title": parts[0].strip(),
                            "author": parts[1].strip(),
                            "genre": parts[2].strip(),
                            "ISBN": parts[3].strip(),
                        })

            #perform binary search
            books.sort(key=lambda b: b[field].lower())
            search_values = [b[field].lower() for b in books]
            index = self.binary_search(search_values, query)

            if index != -1:
                book = books[index]
                search_result_label.config(
                    text=f"Book Found:\nTitle: {book['title']}\nAuthor: {book['author']}\nGenre: {book['genre']}\nISBN: {book['ISBN']}")
            else:
                search_result_label.config(text="Book not found.")

        Button(search_container, text="Search", font=("Tahoma", 14, "bold"), bg="blue4", fg="white",
               command=perform_search).pack(pady=20)

        Button(search_frame, text="Back", font=("Tahoma", 14, "bold"),
               bg="gray", fg="white", command=lambda: [search_frame.pack_forget(), self.user_main_frame()]).pack(pady=20)

    def binary_search(self, sorted_list, query):
        low, high = 0, len(sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid] == query:
                return mid
            elif sorted_list[mid] < query:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def user_main_frame(self):
        self.main_frame.pack_forget() 
        user_main_frame = Frame(self.root, bg="midnight blue")
        user_main_frame.pack(fill=BOTH, expand=True)

        Label(user_main_frame, text="Welcome to User Dashboard", font=("Tahoma", 18, "bold"), fg="white", bg="midnight blue").pack(pady=20)

        user_main_container = Frame(user_main_frame, relief="ridge", bd=3, width=325, height=500, bg="azure3")
        user_main_container.pack_propagate(False)
        user_main_container.pack(pady=20, anchor="center")

        Button(user_main_container, text="View All Books", font=("Tahoma", 14, "bold"), width=15, fg="white", bg="blue4", command=self.view_all_books).pack(pady=(20, 10))
        Button(user_main_container, text="Borrow book", font=("Tahoma", 14, "bold"), width=15, fg="white", bg="blue4", command=self.borrow_book).pack(pady=(20, 10))
        Button(user_main_container, text="Return book", font=("Tahoma", 14, "bold"), width=15, fg="white", bg="blue4", command=self.return_book).pack(pady=(20, 10))
        Button(user_main_container, text="Reserve book", font=("Tahoma", 14, "bold"), width=15, fg="white", bg="blue4", command=self.reserve_book).pack(pady=(20, 10))
        Button(user_main_container, text="Cancel Reservation", font=("Tahoma", 14, "bold"), 
           width=15, fg="white", bg="blue4", command=self.cancel_reservation).pack(pady=(20, 10))

        Button(user_main_container, text="Search book", font=("Tahoma", 14, "bold"), width=15, fg="white", bg="blue4", command=self.search_book).pack(pady=(20, 10))

        def logout():
            #destroy all widgets and go to the login screen
            user_main_frame.pack_forget()
            self.login_screen()  

        Button(user_main_container, text="Logout", font=("Tahoma", 14, "bold"), width=15, fg="white", bg="blue4", command=logout).pack(pady=(20, 10))

    def view_all_books(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        view_books_frame = Frame(self.root, bg="midnight blue")
        view_books_frame.pack(fill=BOTH, expand=True)
                
        Label(view_books_frame, text="All Books", font=("Tahoma", 18, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)

        #create a frame for the canvas and scrollbar
        table_frame = Frame(view_books_frame, bg="midnight blue")
        table_frame.pack(pady=20)

        #create canvas and scrollbar for scrolling
        canvas = Canvas(table_frame, bg="gray", width=900, height=400, relief="ridge", bd=2)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(table_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        #create a scrollable frame inside the canvas
        scrollable_frame = Frame(canvas, bg="gray", relief="ridge")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        #load books and display them in a table-like structure
        books = [book for book in load_books(sorted_by_first_letter=True) if book not in self.reserved_books_queue]
        if books:
            #table header
            header_font = ("Tahoma", 12, "bold")
            headers = ["Title", "Author", "Genre", "ISBN"]
            for j, header in enumerate(headers):
                Label(scrollable_frame, text=header, font=header_font, bg="blue4", 
                      fg="white", width=20, anchor="w").grid(row=0, column=j, sticky="w", padx=5, pady=5)

            #table rows for books
            for i, book in enumerate(books):
                #split the book entry into its components
                book_details = book.split(" | ") if " | " in book else [book, "", "", ""]
                for j, detail in enumerate(book_details):
                    Label(scrollable_frame, text=detail, font=("Tahoma", 12, "bold"), 
                          bg="gray", fg="white", width=20, anchor="w").grid(row=i+1, column=j, sticky="w", padx=5, pady=5)
        else:
            Label(scrollable_frame, text="No books available.", font=("Tahoma", 14, "bold"), 
                  bg="midnight blue", fg="white").grid(row=0, column=0, columnspan=4, pady=20)
        #update scroll region to fit content
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        Button(view_books_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [view_books_frame.pack_forget(), self.user_main_frame()]).pack(pady=20)


