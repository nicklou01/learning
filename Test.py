import tkinter as tk


###############

import math

def draw_rotated_arrow(canvas, x, y, length, angle_deg, color="red", width=10):
    angle_rad = math.radians(angle_deg)
    x_end = x + length * math.cos(angle_rad)
    y_end = y - length * math.sin(angle_rad)  # y-axis is inverted in canvas
    canvas.create_line(x, y, x_end, y_end, arrow=tk.LAST, fill=color, width=width)

############
def create_text_application(message_text):
    # Create the main window
    window = tk.Tk()
    window.title("Basic GUI")
    window.configure(bg="white")

    # Create a Label widget to display the text
    message_label = tk.Label(window, text=message_text, font=("Times New Roman", 24, "bold italic"),
                    fg = "navy", bg = "white")
    message_label.grid(row=0, column=0, columnspan=2,
                    padx=50, pady=(50,20)) # Add padding around the label and location info

    #Load the images
    photo = tk.PhotoImage(file=r"C:\Users\npisani\Downloads\picture1.png")
    photo2 = tk.PhotoImage(file=r"C:\Users\npisani\Downloads\picture3.png")

    #image labeling
    #image_label = tk.Label(window, image=photo, bg="white")
    #image_label.image = photo #reference
    #image_label.grid(row=1, column=0, columnspan=2, padx=(0,30), pady=(0,280))

    image_label2 = tk.Label(window, image=photo2, bg="white")
    image_label2.image = photo2
    image_label2.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 5))

    image_label = tk.Label(window, image=photo, bg="white")
    image_label.image = photo #reference
    image_label.grid(row=1, column=0, columnspan=2, padx=(0,50), pady=(0,260))
    #image caption
    image_caption = tk.Label(window, text="Looks like he smells!", font=("Time New Roman",
                        16), fg="navy", bg="white")
    image_caption.grid(row=3, column=0, columnspan=2, pady=(0,30))

    
    # Create a canvas to draw the arrow
    canvas1 = tk.Canvas(window, width=130, height=60, bg="white", highlightthickness=0)
    canvas1.grid(row=2, column=0, sticky="w")
    canvas2 = tk.Canvas(window, width=130, height=60, bg="white", highlightthickness=0)
    canvas2.grid(row=2, column=1, sticky="e")

    # Draw a red arrow on the canvas
    #canvas1.create_line(10, 30, 120, 30, arrow=tk.LAST, fill="red", width=10)
    #canvas2.create_line(120, 30, 10, 30, arrow=tk.LAST, fill="red", width=10)

    #rotated arrows drawing 
    draw_rotated_arrow(canvas1, 10, 50, 100, 20)  # Slightly angled right
    draw_rotated_arrow(canvas2, 120, 50, 100, 160)  # Slightly angled left

    # Start the Tkinter event loop
    window.mainloop()

# Define the message you want to display
my_message = "Why do you smell?"

# Call the function to create and display the application
create_text_application(my_message)