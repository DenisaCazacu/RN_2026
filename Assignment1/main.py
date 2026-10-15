from pathlib import Path

from cramer import solve_cramer
from helpers.system_file_parser import load_system
from inversion import solve_inversion
from matrix_operations import determinant
from matrix_operations import trace
from matrix_operations import norm 
from matrix_operations import transpose
from matrix_operations import multiply
from helpers.printer import print_matrix, print_vector

system_number = input("Enter the system number (1-4): ").strip()
while system_number not in ("1", "2", "3", "4"):
    print("Invalid system number. Choose a number from 1 to 4.")
    system_number = input("Enter the system number (1-4): ").strip()

system_path = Path(__file__).resolve().parent / "systems" / f"example{system_number}"
A, B = load_system(system_path)
print("A=")
print_matrix(A)
print(f"{B=}\n")

print(f"determinant(A)={determinant(A)}\n")
print(f"trace(A)={trace(A)}\n")
print(f"norm(B)={norm(B)}\n")
print("transpose(A)=")
print_matrix(transpose(A))
print(f"multiply(A, B)={multiply(A, B)}\n")
print("Solution Cramer=")
print_vector(solve_cramer(A, B))
print("Solution Inversion=")
print_vector(solve_inversion(A, B))