# This script generates a multiplication table and writes it to a file.
# It was done as I am studying a Diploma in IT and I am learning Python.
# So I converted the code I did using HTML and JavaScript to Python.
# The code is simple and easy to understand, and it uses basic Python features.


def generate_multiplication_table(rows, cols):
    # Generate multiplication table with given rows and columns
    table = []
    for i in range(1, rows + 1):
        row = [i * j for j in range(1, cols + 1)]
        table.append(row)
    return table

def write_table_to_file(table, filename="table.txt"):
    with open(filename, "w") as f:
        for row in table:
            line = "\t".join(str(cell) for cell in row)
            f.write(line + "\n")
    print(f"Your multiplication table has been written to: {filename}.")

def main():
     while True:
        print("Type 'exit' at any time to quit.")
        row_input = input("Enter the number of rows: ")
        if row_input.lower() == "exit":
            print("👋 Exiting the program.")
            break

        col_input = input("Enter the number of columns: ")
        if col_input.lower() == "exit":
            print("👋 Exiting the program.")
            break

        try:
            rows = int(row_input)
            cols = int(col_input)
            table = generate_multiplication_table(rows, cols)
            write_table_to_file(table)
        except ValueError:
            print("❗ Please enter valid integers.\n")

if __name__ == "__main__":
    main()
