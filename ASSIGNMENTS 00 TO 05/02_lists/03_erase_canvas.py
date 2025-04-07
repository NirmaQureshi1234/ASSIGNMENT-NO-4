"""
Program: Eraser on a Canvas
----------------------------
This program creates a grid of blue cells on a canvas and an eraser rectangle.
Dragging the eraser across the canvas turns the blue cells it contacts to white.
"""

import tkinter as tk

def create_grid(canvas, rows, cols, cell_size):
    """
    Creates a grid of blue cells on the canvas.
    Parameters:
    - canvas: The tkinter Canvas widget.
    - rows: Number of rows in the grid.
    - cols: Number of columns in the grid.
    - cell_size: The size of each cell in pixels.
    """
    for i in range(rows):
        for j in range(cols):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white", tags="cell")

def on_drag(event):
    """
    Handles the eraser drag event to erase (turn white) the blue cells.
    Parameters:
    - event: The Tkinter event object containing cursor coordinates.
    """
    overlapping_items = canvas.find_overlapping(event.x - eraser_size // 2, event.y - eraser_size // 2,
                                                 event.x + eraser_size // 2, event.y + eraser_size // 2)
    for item in overlapping_items:
        canvas.itemconfig(item, fill="white")

def main():
    """
    Main function to set up the canvas, grid, and eraser functionality.
    """
    global canvas, eraser_size

    # Step 1: Create the main window
    root = tk.Tk()
    root.title("Eraser on a Canvas")

    # Step 2: Define canvas dimensions and cell size
    canvas_width = 400
    canvas_height = 400
    cell_size = 20
    rows = canvas_height // cell_size
    cols = canvas_width // cell_size
    eraser_size = 40  # Size of the eraser rectangle

    # Step 3: Create the canvas
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Step 4: Create the grid of blue cells
    create_grid(canvas, rows, cols, cell_size)

    # Step 5: Bind the mouse drag event to the eraser functionality
    canvas.bind("<B1-Motion>", on_drag)

    # Step 6: Start the Tkinter event loop
    root.mainloop()

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
