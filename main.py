import tkinter as tk

def create_table(root, rows, columns, table_width, table_height, column_names):
    # Calculate the width and height of each cell
    cell_width = table_width // columns
    cell_height = table_height // (rows + 1)  # +1 for the heading row

    # Create a frame for the table
    table_frame = tk.Frame(root, width=table_width, height=table_height)
    table_frame.pack_propagate(False)  # Prevent frame from resizing to its contents
    table_frame.pack()

    # Create headings for columns
    for j in range(columns):
        heading = tk.Label(table_frame, text=column_names[j], relief=tk.RIDGE, width=10, height=5, bg="lightblue")
        heading.grid(row=0, column=j, sticky="nsew")

    # Create cells for each row and column
    for i in range(1, rows+1):
        for j in range(columns):
            cell = tk.Entry(table_frame, width=20)
            cell.grid(row=i, column=j, sticky="nsew")

    # Configure row heights and column widths to make them equal
    for i in range(rows + 1):  # +1 for the heading row
        table_frame.grid_rowconfigure(i, minsize=cell_height)
    for j in range(columns):
        table_frame.grid_columnconfigure(j, minsize=cell_width)

# Create the main window
root = tk.Tk()
root.title("Table")

# Set the size of the window and the size of the table
table_width = 1200
table_height = 700
table_rows = 8
table_columns = 4
column_names = ["TOKEN", "COUNTER", "TOKEN", "COUNTER"]  # Specify custom names for each column
root.geometry(f"{table_width}x{table_height}")

# Create the table with specified rows, columns, and column names
create_table(root, table_rows, table_columns, table_width, table_height, column_names)

# Start the GUI
root.mainloop()
