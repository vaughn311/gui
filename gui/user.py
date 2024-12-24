class User:
    def __init__(self, root, library):
        self.root = root
        self.library = library

    def borrow_book(self):
        def select_book():
            selected_index = books_listbox.curselection()
            if selected_index:
                book = self.library.borrow_book(selected_index[0])
                if book:
                    messagebox.showinfo("Success", f"You borrowed: {book['title']} by {book['author']}")
                    borrow_window.destroy()
                else:
                    messagebox.showwarning("Unavailable", "Book is already borrowed.")
            else:
                messagebox.showwarning("Error", "Select a book to borrow")

        borrow_window = Toplevel(self.root)
        borrow_window.title("Borrow a Book")
        books_listbox = Listbox(borrow_window, width=50, height=20)
        books_listbox.pack(padx=20, pady=20)

        for book in self.library.books:
            books_listbox.insert(END, f"{book['title']} by {book['author']}")

        Button(borrow_window, text="Borrow Selected", command=select_book).pack(pady=10)

    def return_book(self):
        book = self.library.return_last_borrowed()
        if book:
            messagebox.showinfo("Success", f"You returned: {book['title']} by {book['author']}")
        else:
            messagebox.showwarning("Error", "No books to return.")

    def show_user_menu(self):
        user_menu = Toplevel(self.root)
        user_menu.title("User Menu")

        Button(user_menu, text="Borrow Book", command=self.borrow_book).pack(pady=10)
        Button(user_menu, text="Return Book", command=self.return_book).pack(pady=10)
        Button(user_menu, text="Exit", command=user_menu.destroy).pack(pady=10)
