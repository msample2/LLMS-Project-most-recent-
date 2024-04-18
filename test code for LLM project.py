import tkinter as tk
from PIL import ImageTk, Image
import openai  

openai.api_key = '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'

def generate_model_text(model):
    about_text = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", 
        prompt=f"Generate information about the Audi {model}.\n",
        temperature=0.5,
        max_tokens=100
    )
    return about_text.choices[0].text.strip()

def display_about_info():
    about_text = generate_about_text()
    about_window = tk.Toplevel(window)
    about_window.title("About Audi")
    about_label = tk.Label(about_window, text=about_text, font=("Arial", 12), wraplength=500, justify=tk.LEFT)
    about_label.pack()
    
    # Add a Back button
    back_button = tk.Button(about_window, text="Back", command=about_window.destroy)
    back_button.pack()

def display_generation_info(model, generation):
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

def display_model_info(model):
    # Close the current window
    window.destroy()

    # Create a new window for model info
    model_info_window = tk.Tk()
    model_info_window.title(f"Audi {model} Info")

    # About button
    about_button = tk.Button(model_info_window, text="About Audi", command=display_about_info)
    about_button.pack()

    # Label for the model info
    header = tk.Label(model_info_window, text=f"Audi {model}", font=("Montserrat", 24))
    header.pack()

    # Display buttons for generations
    generations = ["B8", "B8.5", "B9"]
    for generation in generations:
        button = tk.Button(model_info_window, text=generation, command=lambda g=generation: display_generation_info(model, g))
        button.pack()

def display_models():
    # Create main window for model display
    global window
    window = tk.Tk()
    window.title("Audi: Past to Present")
    window.configure(bg="white")
    
    # Label for the text "Audi: Past to Present"
    header = tk.Label(window, text="Audi: Past to Present", font=("Montserrat", 24), bg="white")
    header.pack()

    # About button
    about_button = tk.Button(window, text="About Audi", command=display_about_info)
    about_button.pack()

    # Create frame for model buttons
    model_frame = tk.Frame(window, bg="white")
    model_frame.pack(pady=20)

    models = ["R8", "TT", "S5", "S4", "S3", "A5", "A4", "A3"]
    buttons_per_row = 4
    for i, model in enumerate(models):
        if i % buttons_per_row == 0:
            row_frame = tk.Frame(model_frame, bg="white")
            row_frame.pack()
        
        # Load image of the model
        model_image = Image.open(f"{model.lower()}_image.png")  
        model_image = model_image.resize((200, 100))  # Resize the image to fit the button
        model_image = ImageTk.PhotoImage(model_image)

        # Create button with image and text
        button = tk.Button(row_frame, text=f"Audi {model}", image=model_image, compound=tk.TOP, command=lambda m=model: display_model_info(m))
        button.image = model_image  # Keep a reference to the image to prevent garbage collection
        button.pack(side=tk.LEFT, padx=20)

    window.mainloop()

def generate_about_text():
    about_text = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt="Generate information about Audi.\n",
        temperature=0.5,
        max_tokens=100
    )
    return about_text.choices[0].text.strip()

# Display models on startup
display_models()
