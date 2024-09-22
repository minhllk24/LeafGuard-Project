import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import webbrowser

class StudentInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Group name")
        self.root.geometry("600x800")
        self.root.configure(bg='#E0F2F1')  

        self.setup_ui()

    def setup_ui(self):
        # Logo
        try:
            logo_image = Image.open("aptech.jpg")  # Change your logo file path
            logo_photo = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(self.root, image=logo_photo, bg='#E6E6FA')  
            logo_label.image = logo_photo
            logo_label.pack(pady=20)
        except FileNotFoundError:
            messagebox.showerror("Error", "Logo image not found")
        
        # Project Names
        project_label = tk.Label(self.root, text="Leaf Name and Disease Identifying App", font=("Arial", 18, "bold"), bg='#90EE90')  # Đặt màu nền xanh
        project_label.pack(pady=10)

        

        # Segmented Images
        images_frame = tk.Frame(self.root, bg='#98FB98')
        images_frame.pack(pady=20)

        # Path to your UI photo
        # Change the image_paths according to your  image location

        image_paths = [
            "closeup-selective-focus-shot-green-plant-leaf.jpg",
            "close-up-water-texture-leaf.jpg",
            "green-leaves-closeup.jpg"
        ]

        for path in image_paths:
            try:
                img = Image.open(path)
                img = img.resize((224, 224), Image.LANCZOS)    # Điều chỉnh kích thước ảnh nếu cần
                photo = ImageTk.PhotoImage(img)
                button = tk.Button(images_frame, image=photo, bg='#E0F2F1', command=lambda p=path: self.open_image(p))
                button.image = photo
                button.pack(side=tk.LEFT, padx=10)
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image file not found: {path}")

        # Labels
        teacher_label = tk.Label(self.root, text="Techwiz 5 - 2024 - Global IT Competition - 43 nations - over 810 teams.\nCategory: Big Data in Data Science\nProject: LeafGuard\n\nLecturer: MSc. Hồ Nhựt Minh", font=("Arial", 12), bg='#E0F2F1')  # Đặt màu nền xanh nhạt
        teacher_label.pack(pady=5)
        # Group Info
        students = [
            
            {"Group": "Data Not Found", "Member": "Nguyen Thi Tuyet Nhung\nTran Kim Khoi\nLy Le Minh\nLe Minh Triet"}
        ]

        for student in students:
            student_info = tk.Label(self.root, text=f"Data Not Found team members:\n{student['Member']}", font=("Arial", 12), bg='#E0F2F1')  # Đặt màu nền xanh nhạt
            student_info.pack(pady=5)

    

        # Start button
        start_button = tk.Button(self.root, text="Start", command=self.run_program, font=("Arial", 14), bg="lightblue", padx=20, pady=10)
        start_button.pack(pady=20)

    def open_image(self, path):
        try:
            webbrowser.open(path)  # Open image by default path
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def run_program(self):
        try:
            # Change the file camera_test_model.py  path according to your file location, here is my  file location
            subprocess.run(['python', 'camera_test_model.py'], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentInfoApp(root)
    root.mainloop()

