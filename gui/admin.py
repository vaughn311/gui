from tkinter import *
from tkinter import messagebox

class Admin:
    def __init__(self, root, library):
        self.root = root
        self.library = library

    def view_all_books(self):
        books_window = Toplevel(self.root)
        books_window.title("All Books")
        books_listbox = Listbox(books_window, width=50, height=20)
        books_listbox.pack(padx=20, pady=20)

        for book in self.library.get_sorted_books():
            books_listbox.insert(END, f"{book['title']} by {book['author']}")

    def add_book(self):
        def save_book():
            title = title_entry.get()
            author = author_entry.get()
            if title and author:
                self.library.add_book({"title": title, "author": author})
                messagebox.showinfo("Success", "Book added successfully!")
                add_book_window.destroy()
            else:
                messagebox.showwarning("Error", "Please fill all fields")

        add_book_window = Toplevel(self.root)
        add_book_window.title("Add a Book")

        Label(add_book_window, text="Book Title:").pack(pady=5)
        title_entry = Entry(add_book_window, width=30)
        title_entry.pack(pady=5)

        Label(add_book_window, text="Author:").pack(pady=5)
        author_entry = Entry(add_book_window, width=30)
        author_entry.pack(pady=5)

        Button(add_book_window, text="Add Book", command=save_book).pack(pady=20)

    def remove_book(self):
        def delete_selected():
            selected_index = books_listbox.curselection()
            if selected_index:
                self.library.remove_book(selected_index[0])
                books_listbox.delete(selected_index[0])
                messagebox.showinfo("Success", "Book removed successfully!")
                remove_book_window.destroy()
            else:
                messagebox.showwarning("Error", "Select a book to remove")

        remove_book_window = Toplevel(self.root)
        remove_book_window.title("Remove a Book")
        books_listbox = Listbox(remove_book_window, width=50, height=20)
        books_listbox.pack(padx=20, pady=20)

        for book in self.library.books:
            books_listbox.insert(END, f"{book['title']} by {book['author']}")

        Button(remove_book_window, text="Remove Selected", command=delete_selected).pack(pady=10)

    def show_admin_menu(self):
        admin_menu = Toplevel(self.root)
        admin_menu.title("Admin Menu")

        Button(admin_menu, text="View All Books", command=self.view_all_books).pack(pady=10)
        Button(admin_menu, text="Add a Book", command=self.add_book).pack(pady=10)
        Button(admin_menu, text="Remove a Book", command=self.remove_book).pack(pady=10)
        Button(admin_menu, text="Exit", command=admin_menu.destroy).pack(pady=10)