import tkinter as tk
from tkinter import Canvas


class MusicSheet(tk.Tk):
    def __init__(self, measure):
        super().__init__()
        self.title("Musical Sheet Layout")
        self.canvas = Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()
        self.draw_entire_section(50, 60, measure)

    def draw_entire_section(self, x, y, time_signature):
        self.draw_staff_lines(x, y)
        self.draw_treble_clef(x, y - 25)
        self.draw_time_signature(x + 50, y - 10, time_signature)

    def draw_staff_lines(self, x_offset, y_offset):
        """Draw the staff lines on the canvas."""
        num_lines = 5
        spacing = 20
        for i in range(num_lines):
            y = y_offset + i * spacing
            self.canvas.create_line(x_offset, y, x_offset + 700, y, width=2, fill = 'black')

    def draw_treble_clef(self, x, y):
        """Draw a treble clef at the given x, y position."""
        self.canvas.create_text(x, y, text="𝄞", font=("Arial", 100), anchor="nw", fill = 'black')

    def draw_time_signature(self, x, y, signature):
        """Draw a time signature at the given x, y position."""
        self.canvas.create_text(x,y, text = signature[0], font=("BiauKaiHK", 50), anchor="n", fill ='black')
        self.canvas.create_text(x,y + 40, text = signature[2], font=("BiauKaiHK", 50), anchor="n", fill ='black')

    
    def draw_quarter_note(self, x, y):
        """Draw a quarter note at the given x, y position."""
        self.canvas.create_oval(x, y, x + 10, y + 15, fill="black")
        self.canvas.create_line(x + 10, y, x + 10, y - 35, width=2, fill = 'black')

    def draw_half_note(self, x, y):
        """Draw a half note at the given x, y position."""
        self.canvas.create_oval(x, y, x + 10, y + 15, fill="white", outline= 'black')
        self.canvas.create_line(x + 10, y, x + 10, y - 35, width=2, fill = 'black')

    def draw_whole_note(self, x, y):
        """Draw a whole note at the given x, y position."""
        self.canvas.create_oval(x, y, x + 15, y + 10, fill="white", outline = 'black')

    def draw_dotted_half_note(self, x, y):
        """Draw a dotted half note at the given x, y position."""
        self.draw_half_note(x, y)
        # Draw the dot
        self.canvas.create_oval(x + 15, y + 5, x + 20, y + 10, fill="black")


    