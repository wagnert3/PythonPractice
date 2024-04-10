#IMPORTING THE LIBRARIES
import tkinter as tk
from tkinter import messagebox

#FUNCTIONS

def calculate_bmi(weight, height):

    return weight / (height **2)
 
def calculate_and_show_bmi():
      
    try:
       weight = float(entry_weight.get())
       height = float(entry_height.get())
       bmi = calculate_bmi(weight, height)
       bmi_rounded = round(bmi, 2)
                    
    # Determine the BMI category
    #    if bmi < 18.5:
    #         category = "Underweight"
    #    elif bmi < 25:
    #         category = "Normal weight"
    #    elif bmi < 30:
    #         category = "Overweight"
    #    else:
    #         category = "Obese"

        # Show the result in a messagebox
       messagebox.showinfo("BMI Calculator", f"Your BMI is: {bmi_rounded} ({category})")
        
             
    # except ValueError:
    
    #         messagebox.showerror("Input error", "Please enter valid numbers for weight and height.")

    except Exception as e:
        print(f"An error occurred: {e}")
            
# Setting up the Tkinter window
root = tk.Tk()
root.title("BMI Calculator")

# Creating and placing widgets in the window (label, entry, button)

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
root.mainloop() 