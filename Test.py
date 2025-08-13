import tkinter as tk

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

    #Load the image
    photo = tk.PhotoImage(file=r"C:\Users\npisani\Downloads\picture1.png")

    #image labeling
    image_label = tk.Label(window, image=photo, bg="white")
    image_label.image = photo #reference
    image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 5))

    #image caption
    image_caption = tk.Label(window, text="Looks like he smells!", font=("Time New Roman",
                        16), fg="navy", bg="white")
    image_caption.grid(row=2, column=0, columnspan=2, pady=(0,30))

    
    # Create a canvas to draw the arrow
    canvas = tk.Canvas(window, width=130, height=60, bg="white", highlightthickness=0)
    canvas.grid(row=1, column=0, sticky="w")

    # Draw a red arrow on the canvas
    canvas.create_line(10, 30, 120, 30, arrow=tk.LAST, fill="red", width=10)

    # Start the Tkinter event loop
    window.mainloop()

# Define the message you want to display
my_message = "Why do you smell?"

# Call the function to create and display the application
create_text_application(my_message)