import sys

print("=== Command Quest ===")

# Nome do programa
print("Program name:", sys.argv[0])

# Número de argumentos (sem contar o nome do programa)
arg_count = len(sys.argv) - 1

if arg_count == 0:
    print("No arguments provided!")
else:
    print("Arguments received:", arg_count)

    i = 1
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

# Total incluindo o nome do programa
print("Total arguments:", len(sys.argv))
