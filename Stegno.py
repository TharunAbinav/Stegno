'''This Project is about using Quantum key to secure the data 
and then using Steganography to hide the data in an image.'''
import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root=tk.Tk()
root.withdraw()

print("Opening file section")
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")]
)

if file_path:
    img = Image.open(file_path)
    print(f"Successfully selected: {file_path}")
    print(f"Image Size: {img.size}")
    img.show()
else:
    print("User canceled image selection.")

def generate_quantum_number(num_bits=8):
    # 1. Create a quantum circuit with the desired number of bits
    circuit = QuantumCircuit(num_bits, num_bits)
    
    # 2. Put every qubit into a 50/50 quantum superposition
    for qubit in range(num_bits):
        circuit.h(qubit)
        
    # 3. Measure the qubits to collapse their states into 0s and 1s
    circuit.measure(range(num_bits), range(num_bits))
    
    # 4. Simulate the circuit execution exactly 1 time (1 shot)
    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1, memory=True).result()
    
    # 5. Extract the bitstring and convert it to a decimal integer
    bitstring = result.get_memory()[0]
    return int(bitstring, 2)

# Generate a random integer between 0 and 255 (8 bits)
print(f"Your quantum random number: {generate_quantum_number(8)}")