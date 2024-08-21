import cv2
import numpy as np
import tensorflow as tf
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Placeholder for vehicle detection model (You should replace this with an actual model)
class VehicleDetector:
    def __init__(self):
        # Load your pre-trained model here
        pass

    def detect(self, image):
        # Dummy detection logic (Replace with actual detection code)
        return True

# Function to calculate the billing amount
def calculate_bill(start_time, end_time):
    duration = end_time - start_time
    hours = duration.total_seconds() / 3600
    if hours <= 24:
        return hours * 50  # Hourly charge
    else:
        days = duration.days
        return days * 500  # Daily charge

# Initialize vehicle detector
detector = VehicleDetector()

# Dictionary to store vehicle entry times
vehicle_entry_times = {}

# Function to process uploaded image
def process_image(image_path):
    image = cv2.imread(image_path)
    if detector.detect(image):
        vehicle_id = "vehicle_1"  # Unique identifier for the vehicle (This is a placeholder)
        current_time = datetime.now()
        
        if vehicle_id in vehicle_entry_times:
            start_time = vehicle_entry_times[vehicle_id]
            bill_amount = calculate_bill(start_time, current_time)
            messagebox.showinfo("Billing Info", f"Bill Amount: Rs. {bill_amount:.2f}")
            # Update the entry time
            vehicle_entry_times[vehicle_id] = current_time
        else:
            # New vehicle entry
            vehicle_entry_times[vehicle_id] = current_time
            messagebox.showinfo("Vehicle Detected", f"Vehicle detected. Start time recorded: {current_time}")
    else:
        messagebox.showerror("Error", "No vehicle detected in the image.")

# Function to open file dialog and process the selected image
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        process_image(file_path)

# Create the main window
root = tk.Tk()
root.title("Vehicle Image Upload System")

# Create a button to upload images
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
