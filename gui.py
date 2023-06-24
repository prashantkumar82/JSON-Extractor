import tkinter as tk
from tkinter import filedialog, messagebox
from json_extractor import extract_data_from_json

def browse_json_file():
    json_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    json_entry.delete(0, tk.END)
    json_entry.insert(tk.END, json_file)

def browse_csv_file():
    csv_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    csv_entry.delete(0, tk.END)
    csv_entry.insert(tk.END, csv_file)

def extract_data():
    json_file = json_entry.get()
    csv_file = csv_entry.get()
    if json_file and csv_file:
        try:
            extract_data_from_json(json_file, csv_file)
            messagebox.showinfo("Extraction Complete", f"Data extracted from JSON file '{json_file}' and saved to CSV file '{csv_file}'.")
            window.destroy()  # Close the GUI window after extraction
        except Exception as e:
            messagebox.showerror("Extraction Error", f"An error occurred during data extraction: {str(e)}")
    else:
        messagebox.showwarning("Missing File", "Please select JSON and CSV files.")

# Create the main window
window = tk.Tk()
window.title("JSON to CSV Converter")

# Create and position the widgets
json_label = tk.Label(window, text="JSON File:")
json_label.grid(row=0, column=0, padx=10, pady=10)

json_entry = tk.Entry(window, width=50)
json_entry.grid(row=0, column=1, padx=10, pady=10)

json_button = tk.Button(window, text="Browse", command=browse_json_file)
json_button.grid(row=0, column=2, padx=10, pady=10)

csv_label = tk.Label(window, text="CSV File:")
csv_label.grid(row=1, column=0, padx=10, pady=10)

csv_entry = tk.Entry(window, width=50)
csv_entry.grid(row=1, column=1, padx=10, pady=10)

csv_button = tk.Button(window, text="Browse", command=browse_csv_file)
csv_button.grid(row=1, column=2, padx=10, pady=10)

extract_button = tk.Button(window, text="Extract Data", command=extract_data)
extract_button.grid(row=2, column=1, padx=10, pady=10)

# Start the main loop
window.mainloop()
