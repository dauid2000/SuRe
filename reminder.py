import datetime
import tkinter as tk
import tkinter.simpledialog
from PIL import Image, ImageTk
import courses


def ask_topic():
    thebox = tk.simpledialog.askstring("Input", "Enter topic:")
    return thebox


class Reminder(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Reminder")
        self.geometry("500x500")
        self.center_window()
        self.show_logo()
        self.show_courses_buttons()

    def center_window(self):
        w = 500
        h = 500

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def show_logo(self):
        logo = Image.open("C:\\Users\\dmusu\\PycharmProjects\\MyApps\\correct logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(logo)
        tk.Label(self, image=self.logo).pack(pady=20)

    def show_courses_buttons(self):
        tk.Label(self, text="COURSES", font=("Helvetica", 13, "bold")).pack()
        courses_frame = tk.Frame(self)
        courses_frame.pack(pady=10)
        for i, course in enumerate(courses.courses):
            if i // 4 == 1:
                tk.Label(courses_frame, text="").grid(row=i // 4, column=0, columnspan=4, pady=20)
            tk.Button(courses_frame, text=course, relief=tk.GROOVE, bg="blue", font=("Helvetica", 12, "bold"),
                      command=lambda c=course: self.remind(c), width=7, height=1).grid(row=i // 4, column=i % 4,
                                                                                       padx=20)

    def remind(self, course):
        topic = ask_topic().title()
        self.show_spaced_repetition_schedule(course, topic)

    def show_spaced_repetition_schedule(self, course, topic):
        spaced_dates = [datetime.datetime.now() + datetime.timedelta(days=i) for i in [1, 3, 7, 14, 30, 60]]
        spaced_dates_window = tk.Toplevel(self)
        spaced_dates_window.title("Spaced Repetition Schedule")
        spaced_dates_window.geometry("400x400")
        spaced_dates_window.configure(bg="blue")

        tk.Label(spaced_dates_window, text="Spaced Repetition Schedule:", font=("Helvetica", 16, "bold")).pack()
        for i, spaced_date in enumerate(spaced_dates):
            spaced_date_str = spaced_date.strftime("%b %d")
            entry_text = f"{course}: {topic} on {spaced_date_str}"
            tk.Label(spaced_dates_window, text=entry_text, font=("Helvetica", 14)).pack()
            copy_button = tk.Button(spaced_dates_window, text="Copy",
                                    command=lambda e=entry_text: self.copy_to_clipboard(e))

            copy_button.configure(bg="gold")
            copy_button.pack()

    def copy_to_clipboard(self, entry_text):
        self.clipboard_clear()
        self.clipboard_append(entry_text)
