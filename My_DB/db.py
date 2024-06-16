import sqlite3

con=sqlite3.connect('library_db.db',timeout=5.0)


def Add_Book(S_no,name,Author):
    qry='Insert into Library(Serial_no,Book_Name,Author) values(?,?,?);'
    con.execute(qry,(S_no,name,Author))
    con.commit()
    print("Added Sucessfully!")


def Update_book(S_no,name,Author,Availability,s_no):
    qry='Update Library set Serial_no = ?,Book_Name=?,Author=?,Availability = ? where Serial_no = ?;'
    con.execute(qry,(S_no,name,Author,Availability,s_no))
    con.commit()
    print("Updated Sucessfully!")


def view_Books():
    qry='Select * from Library;'
    book=list(con.execute(qry))
    for i in book:
        print(i)


def delete_book(S_no):
    qry='Delete from Library where Serial_no = ?;'
    con.execute(qry,(S_no,))
    con.commit()
    print("Record Sucessfully Deleted")

    
def main():
    while True:
        print("\nSelect an option:")
        print("1. Add Book")
        print("2. Update Book Details")
        print("3. View Books")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            S_no = int(input("Enter Serial_no: "))
            name = input("Enter Book_name: ")
            Author = input("Enter Author Name: ")
            Add_Book(S_no,name,Author)
        elif choice == '2':
            S_no = int(input("Enter Serial_no: "))
            name = input("Enter Book_name: ")
            Author = input("Enter Author Name: ")
            Availability=input("Enter whether its available or not :")
            s_no =int(input('Enter the s_no of Book you need to update:'))
            Update_book(S_no,name,Author,Availability,s_no)
        elif choice == '3':
            view_Books()
        elif choice == '4':
            S_no = int(input("Enter S/no of book to delete: "))
            delete_book(S_no)
        elif choice == '5':
            print("Exiting...")
            quit()
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


con.close()
