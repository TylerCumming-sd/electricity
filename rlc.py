import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

# Function to run the circuit simulation
def run_simulation():
    # Get values from the GUI
    R = float(entry_R.get())
    L = float(entry_L.get())
    C = float(entry_C.get())
    V = 5.0          # Step input voltage (Volts)
    t = 0.0
    dt = 0.0001
    t_max = 0.1

    # State variables
    q = 0.0          # Charge on the capacitor
    i = 0.0          # Current

    # Initialize lists to store time, voltage, and current for plotting
    time_list = []
    voltage_list = []
    current_list = []

    # Clear previous output
    text_output.delete(1.0, tk.END)

    # For output
    text_output.insert(tk.END, "Time(s)\tVoltage_Capacitor(V)\tCurrent(A)\n")

    # Simulation loop
    while t <= t_max:
        Vc = q / C                       # Voltage across capacitor
        dI_dt = (V - R * i - Vc) / L     # From Kirchhoff’s Law

        i += dI_dt * dt                  # Update current
        q += i * dt                       # Update charge

        # Append values to lists for plotting
        time_list.append(t)
        voltage_list.append(Vc)
        current_list.append(i)

        text_output.insert(tk.END, f"{t:.5f}\t{Vc:.5f}\t{i:.5f}\n")

        t += dt

    # Plot the results
    plot_results(time_list, voltage_list, current_list)

# Function to plot the results using matplotlib
def plot_results(time, voltage, current):
    plt.figure(figsize=(10, 6))
    
    # Plot Voltage across Capacitor
    plt.subplot(2, 1, 1)
    plt.plot(time, voltage, label="Voltage across Capacitor (Vc)", color="blue")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.title("Voltage across Capacitor vs Time")
    plt.grid(True)
    plt.legend()

    # Plot Current
    plt.subplot(2, 1, 2)
    plt.plot(time, current, label="Current (I)", color="red")
    plt.xlabel("Time (s)")
    plt.ylabel("Current (A)")
    plt.title("Current vs Time")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Create the main window
root = tk.Tk()
root.title("RC Circuit Simulation")

# Create and place labels and entry widgets for R, L, and C
label_R = tk.Label(root, text="Resistance (R) in Ohms:")
label_R.grid(row=0, column=0, padx=10, pady=5)
entry_R = tk.Entry(root)
entry_R.grid(row=0, column=1, padx=10, pady=5)
entry_R.insert(0, "100")  # Default value

label_L = tk.Label(root, text="Inductance (L) in Henrys:")
label_L.grid(row=1, column=0, padx=10, pady=5)
entry_L = tk.Entry(root)
entry_L.grid(row=1, column=1, padx=10, pady=5)
entry_L.insert(0, "0.1")  # Default value

label_C = tk.Label(root, text="Capacitance (C) in Farads:")
label_C.grid(row=2, column=0, padx=10, pady=5)
entry_C = tk.Entry(root)
entry_C.grid(row=2, column=1, padx=10, pady=5)
entry_C.insert(0, "0.001")  # Default value

# Button to start the simulation
button_run = tk.Button(root, text="Run Simulation", command=run_simulation)
button_run.grid(row=3, column=0, columnspan=2, pady=10)

# Text widget for output
text_output = tk.Text(root, width=50, height=15)
text_output.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
