import tkinter as tk
from tkinter import messagebox, simpledialog


class StudentPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Portal")
        self.root.geometry("600x700")
        self.root.config(bg="#E1F5FE")

        # Center window
        window_width = 600
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        # Student Data Dictionary
        self.students = {}

        # Login Frame
        self.login_frame = tk.Frame(self.root, bg="#E1F5FE")
        self.login_frame.pack(fill="both", expand=True)

        self.student_number_label = tk.Label(self.login_frame, text="Student Number:", font=("Arial", 14), bg="#E1F5FE",
                                             fg="#01579B")
        self.student_number_label.pack(pady=20)

        self.student_number_entry = tk.Entry(self.login_frame, font=("Arial", 14), relief="solid", bd=2)
        self.student_number_entry.pack(pady=10, ipadx=10)

        self.login_button = tk.Button(self.login_frame, text="Login", width=25, height=2, bg="#0288D1", fg="white",
                                      font=("Arial", 12), relief="solid", command=self.login)
        self.login_button.pack(pady=30)

    # Login Action
    def login(self):
        student_number = self.student_number_entry.get()

        if student_number:
            if student_number not in self.students:
                # Automatically create a student profile if not already registered
                name = simpledialog.askstring("New Student", "Enter Student Name:")
                age = simpledialog.askstring("New Student", "Enter Student Age:")
                major = simpledialog.askstring("New Student", "Enter Major:")

                if not name or not age or not major:
                    messagebox.showerror("Error", "All fields must be filled!")
                    return

                self.students[student_number] = {"Name": name, "Age": age, "Major": major}
                messagebox.showinfo("Success", f"Student profile created for {name}!")

            self.login_frame.pack_forget()  # Hide login frame
            self.create_portal(student_number)  # Create portal window
        else:
            messagebox.showerror("Error", "Please enter a valid student number!")

    # Create Student Portal Interface
    def create_portal(self, student_number):
        self.portal_frame = tk.Frame(self.root, bg="#E1F5FE")
        self.portal_frame.pack(fill="both", expand=True)

        # Title Label
        self.title_label = tk.Label(self.portal_frame, text="Student Portal", font=("Helvetica", 24, "bold"),
                                    bg="#E1F5FE", fg="#01579B")
        self.title_label.pack(pady=20)

        # Button to View Profile
        self.view_profile_btn = tk.Button(self.portal_frame, text="View Profile", width=25, height=2, bg="#0288D1",
                                          fg="white", font=("Arial", 12), relief="solid",
                                          command=lambda: self.view_profile(student_number))
        self.view_profile_btn.pack(pady=15)

        # Button to Search Student
        self.search_student_btn = tk.Button(self.portal_frame, text="Search Student", width=25, height=2, bg="#039BE5",
                                            fg="white", font=("Arial", 12), relief="solid", command=self.search_student)
        self.search_student_btn.pack(pady=15)

        # Button to View All Students
        self.view_all_btn = tk.Button(self.portal_frame, text="View All Students", width=25, height=2, bg="#0288D1",
                                      fg="white", font=("Arial", 12), relief="solid", command=self.view_all_students)
        self.view_all_btn.pack(pady=15)

        # Button to Register Student
        self.register_student_btn = tk.Button(self.portal_frame, text="Register Student", width=25, height=2,
                                              bg="#039BE5", fg="white", font=("Arial", 12), relief="solid",
                                              command=self.register_student)
        self.register_student_btn.pack(pady=15)

        # Button to Logout
        self.logout_btn = tk.Button(self.portal_frame, text="Logout", width=25, height=2, bg="#D32F2F", fg="white",
                                    font=("Arial", 12), relief="solid", command=self.logout)
        self.logout_btn.pack(pady=15)

    # Action for Registering a Student
    def register_student(self):
        student_number = simpledialog.askstring("Register Student", "Enter Student Number to Register:")
        if student_number:
            if student_number in self.students:
                messagebox.showerror("Error", "Student already registered!")
                return

            name = simpledialog.askstring("Register Student", "Enter Student Name:")
            age = simpledialog.askstring("Register Student", "Enter Student Age:")
            major = simpledialog.askstring("Register Student", "Enter Major:")

            if not name or not age or not major:
                messagebox.showerror("Error", "All fields must be filled!")
                return

            self.students[student_number] = {"Name": name, "Age": age, "Major": major}
            messagebox.showinfo("Success", f"Student {name} successfully registered!")

    # Action for Viewing a Student Profile
    def view_profile(self, student_number):
        if student_number in self.students:
            student_info = self.students[student_number]
            info = f"Name: {student_info['Name']}\nAge: {student_info['Age']}\nMajor: {student_info['Major']}"
            messagebox.showinfo("Student Profile", info)
        else:
            messagebox.showerror("Error", "Student not found!")

    # Action for Searching a Student by ID
    def search_student(self):
        student_number = simpledialog.askstring("Search Student", "Enter Student Number to Search:")
        if student_number in self.students:
            student_info = self.students[student_number]
            info = f"Name: {student_info['Name']}\nAge: {student_info['Age']}\nMajor: {student_info['Major']}"
            messagebox.showinfo("Student Found", info)
        else:
            messagebox.showerror("Error", "Student not found!")

    # Action for Viewing All Registered Students
    def view_all_students(self):
        if self.students:
            all_students = "\n".join([f"{sid}: {data['Name']}" for sid, data in self.students.items()])
            messagebox.showinfo("All Students", all_students)
        else:
            messagebox.showinfo("No Students", "No students are registered.")

    # Action for Logging Out
    def logout(self):
        result = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if result:
            self.portal_frame.pack_forget()  # Hide portal frame
            self.login_frame.pack(fill="both", expand=True)  # Show login frame again


# Create the main window
root = tk.Tk()
portal = StudentPortal(root)

# Run the application
root.mainloop()
