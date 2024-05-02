import tkinter as tk
from PIL import ImageTk, Image
import openai  

openai.api_key = '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'

def generate_model_text(model):
    about_text = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", 
        prompt=f"Generate information about the Audi {model}.\n",
        temperature=0.5,
        max_tokens=100,
        stop=["\n\n"]
    )
    return about_text.choices[0].text.strip()

def display_about_info(window):
    about_text = generate_about_text()
    about_window = tk.Toplevel(window)
    about_window.title("About Audi")
    about_label = tk.Label(about_window, text=about_text, font=("Arial", 12), wraplength=400, justify=tk.LEFT)
    about_label.pack()
    
    # Add a Back button
    back_button = tk.Button(about_window, text="Back", command=about_window.destroy)
    back_button.pack()

def display_generation_info(window, model, generation):
    generation_window = tk.Toplevel(window)
    generation_window.title(f"Audi {model} {generation} Info")
    header = tk.Label(generation_window, text=f"Audi {model} {generation} Info", font=("Montserrat", 24))
    header.pack()

    # Generate text about the Audi model generation
    generation_text = generate_model_text(f"{model} {generation}")

    generation_label = tk.Label(generation_window, text=generation_text, font=("Arial", 12), wraplength=500, justify=tk.LEFT)
    generation_label.pack()
    
    # Add a Back button
    back_button = tk.Button(generation_window, text="Back", command=generation_window.destroy)
    back_button.pack()

def display_model_info(window, model):
    # Close the current window
    window.destroy()

    # Create a new window for model info
    model_info_window = tk.Tk()
    model_info_window.title(f"Audi {model} Info")
    model_info_window.configure(bg="grey")  # Set background color to grey
    model_info_window.attributes('-fullscreen', False)  # Disable fullscreen

    # Label for the model info
    header = tk.Label(model_info_window, text=f"Audi {model}", font=("Montserrat", 24), bg="midnightblue", fg="white")  # Set text color to white
    header.pack()

    # Display buttons for generations
    generations = ["B8", "B8.5", "B9"]
    for generation in generations:
        button = tk.Button(model_info_window, text=generation, command=lambda g=generation: display_generation_info(model_info_window, model, g), font=("Arial", 12))
        button.pack()

    # About button
    about_button_frame = tk.Frame(model_info_window, bg="midnightblue")
    about_button_frame.pack()

def display_models():
    # Create main window for model display
    window = tk.Tk()
    window.title("Audi ")
    window.configure(bg="midnightblue")  # Set background color to midnightblue
    window.attributes('-fullscreen', False)  # Disable fullscreen
    
    # Label for the text "Audi: Past to Present"
    header = tk.Label(window, text="Audi: Past to Present", font=("Montserrat", 24), bg="Midnightblue", fg="white")  # Set text color to white
    header.pack()

    # Load and display Audi evolution image
    audi_evolution_image = Image.open("audi-evolution.jpg")
    audi_evolution_image = audi_evolution_image.resize((int(window.winfo_screenwidth()/2), int(window.winfo_screenheight()*0.8)))
    audi_evolution_photo = ImageTk.PhotoImage(audi_evolution_image)
    audi_evolution_label = tk.Label(window, image=audi_evolution_photo)
    audi_evolution_label.image = audi_evolution_photo
    audi_evolution_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create frame for model buttons
    model_frame = tk.Frame(window, bg="midnightblue")  # Set background color to midnightblue
    model_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # About button
    about_button = tk.Button(model_frame, text="About Audi", command=lambda: display_about_info(window), font=("Arial", 14), height=3, width=1)
    about_button.pack(fill=tk.X, padx=10, pady=5)

    models = ["R8", "TT", "S5", "S4", "S3", "A5", "A4", "A3"]
    buttons_per_row = 2
    rows = (len(models) + buttons_per_row - 1) // buttons_per_row
    for i in range(rows):
        row_frame = tk.Frame(model_frame, bg="midnightblue")  # Set background color to midnightblue
        row_frame.pack(fill=tk.X)

        for j in range(buttons_per_row):
            index = i * buttons_per_row + j
            if index < len(models):
                model = models[index]
                # Load image of the model
                model_image = Image.open(f"{model.lower()}_image.png")  
                model_image = model_image.resize((200, 100))  # Resize the image to fit the button
                model_image = ImageTk.PhotoImage(model_image)

                # Create button with image and text
                button = tk.Button(row_frame, text=f"Audi {model}", image=model_image, compound=tk.TOP, command=lambda m=model: display_model_info(window, m), font=("Arial", 12))
                button.image = model_image  # Keep a reference to the image to prevent garbage collection
                button.pack(side=tk.LEFT, padx=20, pady=10)

    # Bind the F11 key to prevent toggling fullscreen
    window.bind("<F11>", lambda event: window.attributes("-fullscreen", False))
    window.mainloop()

def generate_about_text():
    about_text = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt="Generate information about Audi.\n",
        temperature=0.5,
        max_tokens=100,
        stop=["\n\n"]
    )
    return about_text.choices[0].text.strip()

# Display models on startup
display_models()

