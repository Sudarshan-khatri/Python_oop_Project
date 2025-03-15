"""This is the first project of three month backend class using the concept of basic python and 
oop in python .The project tittle is "Personal Library management system" .It has following functionlity
#Adding the Book
#Views the Books
# Search the Books
#Updates the Books
# Delete the books"""

from colorama import*
from Book import*
from student import*
import time 
import os


#match the case 
print(Fore.LIGHTGREEN_EX+"\n\n\t\t\tChoose the option:")
print("\t\t\t1:Admin Portal")
print("\t\t\t2:Student portal")
user_option=int(input("Enter the status:"+Fore.RESET))
match user_option:
    case 1:
           #First login the admin then perform the following operation:
        id=input("\n\nEnter the admin id:")
        password=input("Enter the admin password:")
        if (id=="admin" and password=="admin"):
            print("Login sucessfully !!!")
            #To run the program multiple time:
            Run_time=1
            while Run_time:
                print(Fore.CYAN+"\n\n\t\t\twelcome to admin portal".upper())
                print("\t\t\t1:add book".upper())
                print("\t\t\t2:delete book".upper())
                print("\t\t\t3:Exit".upper()+Fore.RESET)
                choice_operation=int(input("Enter the operation:"))
                if(choice_operation==1):
                    Book_title=input("Enter the book_title:")
                    Book_author=input("Enter the book author:")
                    time=datetime.now()
                    print(f"Date:{time}")
                    Book_id=book_id()
                    print(f"Book_id:{Book_id}")
                    Book_version=input("Enter the book version:")
                    obj1=add_book(Book_id,Book_title,Book_author,time,Book_version)
                    obj1.add_book_in_file()


                elif(choice_operation==2):
                    #instance for the class delete:
                    try:
                        with open("book_data.json","r") as file2:
                              books = [json.loads(line.strip()) for line in file2]  #Read all books properly
                        #Details of book 
                        print("\nLists of Book:")
                        for book in books:
                            if isinstance(book, dict):
                                print(f"ID: {book.get('id')}, Title: {book.get('title')}, Year: {book.get('year')}, Author: {book.get('author')}, Version: {book.get('version')}")
                            else:
                                print("Invalid book data format.")
                        
                        b_id=int(input("Enter the book id:"))
                        book_obj=delete_book(b_id)
                        book_obj.delete()
                    except FileNotFoundError:
                        print("File of data not found !!!!!")
                else:
                    print("sorry ! Invalid operation")
                    break

        else:
            print("Invalid user_name or password !!!!")
    
    #user_case for the student portal :
    case 2:
        while True:

            print(Fore.LIGHTBLUE_EX+"\n\n\t\t\tWELCOME TO STUDENT PORTAL")
            print("\t\t\t1:register student".upper())
            print("\t\t\t2:student library".upper())
            print("\t\t\t3:Exit".upper())
            option=int(input("Choose the option:"+Fore.RESET))
            if(option==1):
            # Data of student taken for registeration:
                
                os.system('clear')
                std_name=input(Fore.LIGHTMAGENTA_EX+"Enter student name:")
                std_grade=int(input("Enter the grade:"))
                std_faculty=input("Enter the faculty:")
                std_sec=input("Enter the section:")
                print(Fore.RESET)
                time.sleep(2)
                os.system("clear")
                s_id=book_id()
                print(Fore.LIGHTYELLOW_EX+f"Information of student\nStudent id:{s_id}")
                print(f"Student Name:{std_name}")
                print(f"Student Grade:{std_grade}")
                print(f"Student Faculty:{std_faculty}")
                print(f"Student Section:{std_sec}")
                print(Fore.RESET)
                #create an instance of class student_profile
                std_obj1=student_profile(s_id,std_name,std_grade,std_faculty,std_sec)
                std_obj1.student_details()

            #option that is used to view the list of book or the purchase the book from library
            elif(option==2):
                #show the list of book to student:
                try:
                    print(Fore.LIGHTCYAN_EX)
                    with open("book_data.json","r") as file2:
                        books = [json.loads(line.strip()) for line in file2]  #Read all books properly
                        #Details of book 
                        print("\nLists of Book:")
                        for book in books:
                            if isinstance(book, dict):
                                print(f"ID: {book.get('id')}, Title: {book.get('title')}, Year: {book.get('year')}, Author: {book.get('author')}, Version: {book.get('version')}")
                            else:
                                print("Invalid book data format.")  

                    #Id of student 
                    with open("student_data.json","r") as s_file1:
                        students=[json.loads(line.strip()) for line in s_file1] #read all books properly
                        #Details of studnet
                        print("\n List of student Id:\n")
                        for students_Id in students:
                            if isinstance(students_Id,dict):
                                print(f"student_Id:{students_Id.get('s_id')}") 
                            else:
                                print("Invalid  student data format !!!"+Fore.RESET)
            
                except FileNotFoundError:
                    print("File of data not found !!!!!")
                #from student get the book id number and student id no:
                Book_id_1=int(input(Fore.LIGHTMAGENTA_EX+"Enter the book id:"))
                std_id_1=int(input("Enter the student id:"+Fore.RESET))
                #instance of class view book
                view_obj1=view_book(Book_id_1,std_id_1)
                view_obj1.purchase_book()

            elif(option==3):
                #To exit from the system if user want to exit        
                print("sorry ! Invalid operation")
                break


                            

                    

