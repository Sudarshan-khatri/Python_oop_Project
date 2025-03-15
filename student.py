"""This  program  help to view the list of  book in library and search the book and purchase the book from 
library .student.py file help to  show the student protion"""
import json
from colorama import*
from datetime import datetime
from Book import*
import os



class student_profile:
    def __init__(self,s_id,user_name,grade,faculty,section):
        self.s_id=s_id
        self.user_name=user_name
        self.grade=grade
        self.faculty=faculty
        self.section=section
    
    def student_details(self):
        try:
            
            #dictionary to store the details of students
            s_data={
                "s_id":self.s_id,
                "s_user_name":self.user_name,
                "s_grade":self.grade,
                "s_stream":self.faculty,
                "s_sect":self.section
            }

            student_list=[]

            try:   
                if os.path.exists("student_data.json"):
                #store the data in json file:
                    with open("student_data.json","r") as s_file1:
                        for line_1 in s_file1:
                            student_list.append(json.loads(line_1.strip())) # read the existing data

            except FileExistsError:
                print("File not found !!!!")

            #append the new student list
            student_list.append(s_data)
            #write data back in json format 
            with open("student_data.json","w") as s_file1:
                for student in student_list:
                    json.dump(student,s_file1)
                    s_file1.write("\n")  #write  new line to seperate entries

            print("Student record stored sucessfully !!!")

        except Exception as e:
            print(f"Error :{e}")
         

class view_book(student_profile,add_book):
    def __init__(self, book_id,std_id):
        self.book_id=str(book_id)
        self.std_id=str(std_id)
    
    """This function is used to read the student id and book id then if the student id and book id match then the book in book_data.json is deleted and automatically write in purchase_book.json"""
    def purchase_book(self):
        try:
            # Read books from file
            with open("book_data.json", "r") as s_book:
                s_books = [json.loads(line.strip()) for line in s_book]

            # Read students from file
            with open("student_data.json", "r") as s_record:
                student_list = [json.loads(line.strip()) for line in s_record]

            # Check if the book exists
            book_found = False
            book_to_remove = None
            for book in s_books:
                if str(book.get("id")) == self.book_id:
                    book_found = True
                    book_to_remove = book
                    break

            if not book_found:
                print(f"Book with ID {self.book_id} not found.")
                return

            # Check if the student exists
            student_found = False
            student_name = None
            for student in student_list:
                if str(student.get("s_id")) == self.std_id:
                    student_found = True
                    student_name = student.get("s_user_name")
                    break

            if not student_found:
                print(f"Student with ID {self.std_id} not found.")
                return

            # Create purchase record
            purchase_record = {
                "student_id": self.std_id,
                "student_name": student_name,
                "book_id": self.book_id,
                "book_title": book_to_remove.get("title"),
                "author": book_to_remove.get("author")
            }

            # Write purchase details to purchase file
            with open("purchase_book.json", "a") as purchase_file:
                purchase_file.write(json.dumps(purchase_record) + "\n")

            # Remove the purchased book from the list
            updated_books = [book for book in s_books if str(book.get("id")) != self.book_id]

            # Write the updated list of books back to book_data.json
            with open("book_data.json", "w") as s_book:
                for book in updated_books:
                    s_book.write(json.dumps(book) + "\n")

            print(f"Book with ID {self.book_id} purchased by student with ID {self.std_id} and removed from available books.")

        except FileNotFoundError:
            print("One or more files not found. Please check the file paths.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file contents.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

