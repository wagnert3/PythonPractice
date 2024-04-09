#IMPORTING THE LIBRARIES


#FUNCTIONS

##def calculate_bmi(weight, height):
    
    
    

##def calculate_and_show_bmi():
    
      
      
      
    # try:
       
        
        # Determine the BMI category
        
        
        
        
        
        
        
        # Show the result in a messagebox
        
        
    # except ValueError:
        
            

# Setting up the Tkinter window




# Creating and placing widgets in the window (label, entry, button)

# label_weight = tk.Label(root, text="Enter your weight in kg:")
# label_weight.pack() #pack() is used to display the widget on the window

# entry_weight = tk.Entry(root)
# entry_weight.pack()





# Start the Tkinter event loop






import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    """Calculate and return the BMI based on weight and height.""" # we use three double quotes to write a multi-line comment
    return weight / (height ** 2)

def calculate_and_show_bmi():
    """Get input from the user, calculate BMI, and show the category."""  
      
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = calculate_bmi(weight, height)
        bmi_rounded = round(bmi, 2)
        
        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        # Show the result in a messagebox
        messagebox.showinfo("BMI Calculator", f"Your BMI is: {bmi_rounded} ({category})")
        
    except ValueError: # except block is used to handle the exceptions and ValueError is used to handle the error related to the value of the input
        
            messagebox.showerror("Input error", "Please enter valid numbers for weight and height.")

# Setting up the Tkinter window
root = tk.Tk() #root is the name of the window, Tk() is the constructor of the window and tk is the module name
root.title("BMI Calculator")

# Creating and placing widgets in the window
label_weight = tk.Label(root, text="Enter your weight in kg:")
label_weight.pack() #pack() is used to display the widget on the window

entry_weight = tk.Entry(root)
entry_weight.pack()

label_height = tk.Label(root, text="Enter your height in meters:")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_show_bmi)
calculate_button.pack()

# Start the Tkinter event loop
root.mainloop() #mainloop() is used to run the window in an infinite loop until the user closes it







