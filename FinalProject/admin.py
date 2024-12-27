from tkinter import *
import os

#path to store books data
BOOKS_FILE = "books.txt"

def load_books(sorted_by_first_letter=False):
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as f:
        books = [line.strip() for line in f]
    if sorted_by_first_letter:
        books = quick_sort(books, key=lambda x: x.split("|")[0])  
    return books

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        f.writelines(f"{book}\n" for book in books)

def quick_sort(array, key=lambda x: x):    
    if len(array) <= 1:
        return array
    pivot = key(array[0]) #use the first element as the pivot
    less = [x for x in array[1:] if key(x) < pivot]
    equal = [x for x in array if key(x) == pivot]
    greater = [x for x in array[1:] if key(x) > pivot]
    return quick_sort(less, key) + equal + quick_sort(greater, key)

class AdminSystem:
    def __init__(self, root, main_frame, admin_code="123"):
        self.root = root
        self.main_frame = main_frame
        self.admin_code = admin_code
        self.admin_frame = Frame(self.root, bg="midnight blue")
        self.admin_main_frame = None
        self.library_frame = None
        self.code_entry = None

    def show_admin_login(self):
        self.main_frame.pack_forget()
        self.admin_frame.pack(fill=BOTH, expand=True)       

        Label(self.admin_frame, text="Admin", font=("Tahoma", 18, "bold"), 
              fg="white", bg="midnight blue").pack(pady=20)

        admin_container = Frame(self.admin_frame, relief="ridge", bd=3, 
                                width=325, height=200, bg="azure3")
        admin_container.pack_propagate(False)
        admin_container.pack(pady=100, anchor="center")

        Label(admin_container, text="Enter the code:", font=("Tahoma", 14, "bold"), bg="azure3").pack(pady=(20, 10))
        self.code_entry = Entry(admin_container, font=("Tahoma", 14), width=20, relief="sunken", bg="gray64", show="*")
        self.code_entry.pack(pady=(0, 20))

        def validate_code():
            if self.code_entry.get() == self.admin_code:
                self.admin_frame.pack_forget()
                self.show_admin_main_frame()
            else:
                Label(admin_container, text="Invalid Code!", font=("Tahoma", 12), 
                  fg="red", bg="azure3").pack(pady=(5, 0))
            self.code_entry.delete(0, END)

        Button(admin_container, text="Log In", font=("Tahoma", 14, "bold"), 
               padx=5, pady=10, bg="blue4", width=20, fg="white", relief="raised", 
               command=validate_code).pack()

        Button(self.admin_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", width=10, fg="white", relief="raised", 
               command=lambda: [self.admin_frame.pack_forget(), self.main_frame.pack()]).pack(pady=40)

    def clear_code_entry(self):
        if self.code_entry:  # Ensure the entry widget exists
            self.code_entry.delete(0, END)

    def show_admin_main_frame(self):
        self.admin_main_frame = Frame(self.root, bg="midnight blue")
        self.admin_main_frame.pack(fill=BOTH, expand=True)

        Label(self.admin_main_frame, text="Admin Dashboard", font=("Tahoma", 18, "bold"), 
              fg="white", bg="midnight blue").pack(pady=20)

        admin_main_container = Frame(self.admin_main_frame, relief="ridge", bd=3, width=325, height=150, bg="azure3")
        admin_main_container.pack_propagate(False)
        admin_main_container.pack(pady=100, anchor="center")

        Button(admin_main_container, text="Manage Library", font=("Tahoma", 14, "bold"), 
               bg="blue4", width=15, fg="white", 
               command=self.show_manage_library).pack(pady=(20, 10))

        def logout():
            self.admin_main_frame.pack_forget()
            self.admin_frame.pack()

        Button(admin_main_container, text="Logout", font=("Tahoma", 14, "bold"), 
               bg="blue4", width=15, fg="white", 
               command=logout).pack(pady=10)       

    def show_manage_library(self):
        self.admin_main_frame.pack_forget()
        self.library_frame = Frame(self.root, bg="midnight blue")
        self.library_frame.pack(fill=BOTH, expand=True)

        Label(self.library_frame, text="Manage Library", font=("Tahoma", 18, "bold"), 
              fg="white", bg="midnight blue").pack(pady=20)
        
        library_container = Frame(self.library_frame, relief="ridge", bd=3, width=325, height=250, bg="azure3")
        library_container.pack_propagate(False)
        library_container.pack(pady=100, anchor="center")

        Button(library_container, text="View All Books", font=("Tahoma", 14, "bold"), 
               bg="blue4", fg="white", width=20, command=self.view_books).pack(pady=(20, 5))

        Button(library_container, text="Add Book", font=("Tahoma", 14, "bold"), 
               bg="blue4", fg="white", width=20, command=self.add_book).pack(pady=(10, 5))

        Button(library_container, text="Remove Book", font=("Tahoma", 14, "bold"), 
               bg="blue4", fg="white", width=20, command=self.remove_book).pack(pady=(10, 5))

        Button(library_container, text="Edit Book", font=("Tahoma", 14, "bold"), 
               bg="blue4", fg="white", width=20, command=self.edit_book).pack(pady=(10, 5))

        Button(self.library_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", width=15, command=lambda: [self.library_frame.pack_forget(), self.show_admin_main_frame()]).pack(pady=20)

    def view_books(self):
        for widget in self.library_frame.winfo_children():
            widget.destroy()

        Label(self.library_frame, text="All Books", font=("Tahoma", 18, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)

        #create a frame for the canvas and scrollbar
        table_frame = Frame(self.library_frame, bg="midnight blue")
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

        books = load_books(sorted_by_first_letter=True)
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

        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        back_button = Button(self.library_frame, text="Back", font=("Tahoma", 14, "bold"), 
                             bg="gray", fg="white", command=lambda: [self.library_frame.pack_forget(), self.show_manage_library()])
        back_button.pack(pady=20)


    def add_book(self):
        self.library_frame.pack_forget()
        def save_new_book():
            title = title_entry.get().strip()
            author = author_entry.get().strip()
            genre = genre_entry.get().strip()
            isbn = isbn_entry.get().strip()

            if title and author and genre and isbn:
                books = load_books()
                books.append(f"{title} | {author} | {genre} | {isbn}")
                save_books(books)
                Label(add_container, text="Book Added Successfully!", font=("Tahoma", 12), 
                      fg="green", bg="azure3").pack(pady=10)
            else:
                Label(add_container, text="All fields are required!", font=("Tahoma", 12), 
                      fg="red", bg="azure3").pack(pady=10)

        add_frame = Frame(self.root, bg="midnight blue")
        add_frame.pack(fill=BOTH, expand=True)

        Label(add_frame, text="Add New Book", font=("Tahoma", 18, "bold"), 
              fg="white", bg="midnight blue").pack(pady=20)

        add_container = Frame(add_frame, relief="ridge", bd=3, width=325, height=400, bg="azure3")
        add_container.pack_propagate(False)
        add_container.pack(pady=30, anchor="center")

        Label(add_container, text="Title:", font=("Tahoma", 14, "bold"), 
              bg="azure3", fg="black").pack(pady=5)
        title_entry = Entry(add_container, font=("Tahoma", 14), bg="gray64")
        title_entry.pack(pady=5)

        Label(add_container, text="Author:", font=("Tahoma", 14, "bold"), 
              bg="azure3", fg="black").pack(pady=5)
        author_entry = Entry(add_container, font=("Tahoma", 14), bg="gray64")
        author_entry.pack(pady=5)

        Label(add_container, text="Genre:", font=("Tahoma", 14, "bold"), 
              bg="azure3", fg="black").pack(pady=5)
        genre_entry = Entry(add_container, font=("Tahoma", 14), bg="gray64")
        genre_entry.pack(pady=5)

        Label(add_container, text="ISBN:", font=("Tahoma", 14, "bold"), 
              bg="azure3", fg="black").pack(pady=5)
        isbn_entry = Entry(add_container, font=("Tahoma", 14), bg="gray64")
        isbn_entry.pack(pady=5)

        Button(add_container, text="Save", font=("Tahoma", 14, "bold"), 
               bg="blue4", fg="white", command=save_new_book).pack(pady=(10, 5))

        Button(add_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [add_frame.pack_forget(), self.show_manage_library()]).pack(pady=10)


    def remove_book(self):
        for widget in self.library_frame.winfo_children():
            widget.destroy()

        Label(self.library_frame, text="Remove Book", font=("Tahoma", 18, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)

        remove_frame = Frame(self.library_frame, bg="midnight blue")
        remove_frame.pack(pady=20)

        remove_container = Frame(remove_frame, relief="ridge", bd=3, width=650, height=220, bg="azure3")
        remove_container.pack_propagate(False)
        remove_container.pack(pady=30, anchor="center")

        Label(remove_container, text="Enter any detail (Title, Author, Genre, ISBN) to remove:", 
              font=("Tahoma", 14, "bold"), bg="azure3", fg="black").pack(pady=10)

        search_entry = Entry(remove_container, font=("Tahoma", 14), width=30, bg="gray64", relief="ridge")
        search_entry.pack(pady=10)

        message_label = Label(remove_container, text="", font=("Tahoma", 12), bg="azure3", fg="red")
        message_label.pack(pady=10)

        def handle_remove():
            search_term = search_entry.get().strip().lower()
            if not search_term:
                message_label.config(text="Please enter a valid input.")
                return

            books = load_books()
            updated_books = []
            book_found = False

            for book in books:
                if search_term in book.lower(): #check if the search term matches any part of the book's details
                    book_found = True
                else:
                    updated_books.append(book)

            if book_found:
                save_books(updated_books)
                message_label.config(text="Book removed successfully!", fg="green")
            else:
                message_label.config(text="Book not found.", fg="red")

        Button(remove_container, text="Remove", font=("Tahoma", 14, "bold"), 
               bg="blue4", fg="white", command=handle_remove).pack(pady=10)

        Button(self.library_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [self.library_frame.pack_forget(), self.show_manage_library()]).pack(pady=20)

    def edit_book(self):
        for widget in self.library_frame.winfo_children():
            widget.destroy()

        Label(self.library_frame, text="Edit Book", font=("Tahoma", 18, "bold"), 
              bg="midnight blue", fg="white").pack(pady=20)

        edit_frame = Frame(self.library_frame, bg="midnight blue")
        edit_frame.pack(pady=20)

        edit_select_container = Frame(edit_frame, relief="ridge", bd=3, width=700, height=380, bg="azure3")
        edit_select_container.pack_propagate(False)
        edit_select_container.pack(pady=10, anchor="center")

        books = load_books()
        selected_book = StringVar(value="")

        if books:           
            Label(edit_select_container, text="Select a book to edit:", font=("Tahoma", 14, "bold"), 
                  bg="azure3", fg="black").pack(pady=10)
            listbox = Listbox(edit_select_container, listvariable=selected_book, height=10, width=60, font=("Tahoma", 12))
            listbox.pack(pady=10)

            for book in books:
                listbox.insert(END, book)

        else:
            Label(edit_select_container, text="No books available to edit.", font=("Tahoma", 14, "bold"), 
                  bg="azure3", fg="white").pack(pady=20)
            return

        message_label = Label(edit_select_container, text="", font=("Tahoma", 12), bg="azure3", fg="red")
        message_label.pack(pady=10)

        def handle_edit():
            selected_index = listbox.curselection()
            if not selected_index:
                message_label.config(text="Please select a book to edit.")
                return

            original_book = listbox.get(selected_index)
            book_details = original_book.split(" | ")
            book_details += [""] * (4 - len(book_details))  #ensure all fields are present

            edit_details_frame = Frame(self.library_frame, bg="midnight blue")
            edit_details_frame.pack(fill=BOTH, expand=True)
            edit_frame.pack_forget()

            edit_details_container = Frame(edit_details_frame, relief="ridge", bd=3, width=650, height=470, bg="azure3")
            edit_details_container.pack_propagate(False)
            edit_details_container.pack(pady=5, anchor="center")

            Label(edit_details_container, text="Edit Book Details", font=("Tahoma", 14, "bold"), 
                  bg="azure3", fg="black").pack(pady=20)

            fields = ["Title", "Author", "Genre", "ISBN"]
            entries = []

            for i, field in enumerate(fields):
                Label(edit_details_container, text=f"{field}:", font=("Tahoma", 14, "bold"), 
                      bg="azure3", fg="black").pack(pady=5, anchor="center", padx=100)
                entry = Entry(edit_details_container, font=("Tahoma", 14), width=40, bg="gray64")
                entry.insert(0, book_details[i])
                entry.pack(pady=5)
                entries.append(entry)

            def save_changes():
                new_details = [entry.get().strip() for entry in entries]
                if all(new_details):
                    books[books.index(original_book)] = " | ".join(new_details)
                    save_books(books)
                    message_label.config(text="Book updated successfully!", fg="green")
                    edit_details_frame.pack_forget()
                    self.edit_book()
                else:
                    message_label.config(text="All fields are required.", fg="red")

            Button(edit_details_container, text="Save Changes", font=("Tahoma", 14, "bold"), 
                   bg="blue4", fg="white", command=save_changes).pack(pady=20)

            Button(edit_details_frame, text="Back", font=("Tahoma", 14, "bold"), 
                   bg="gray", fg="white", command=lambda: [edit_details_frame.pack_forget(), self.edit_book()]).pack(pady=10)

        Button(edit_select_container, text="Edit Selected Book", font=("Tahoma", 14, "bold"), 
               bg="blue4", fg="white", command=handle_edit).pack(pady=10)
        Button(edit_frame, text="Back", font=("Tahoma", 14, "bold"), 
               bg="gray", fg="white", command=lambda: [self.library_frame.pack_forget(), self.show_manage_library()]).pack(pady=20)

        
        

