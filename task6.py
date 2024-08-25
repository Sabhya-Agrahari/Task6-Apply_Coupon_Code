import tkinter as tk
import random
from tkinter import messagebox

def generate_coupon_code():
    """Generate a random 5-digit coupon code."""
    return ''.join([str(random.randint(0, 9)) for _ in range(5)])

def calculate_discount(coupon_code):
    """Calculate the discount based on the coupon code."""
    digit_sum = sum(int(digit) for digit in coupon_code)
    if digit_sum % 2 == 0:
        return 0.15  # 15% discount
    else:
        return 0.10  # 10% discount

def apply_coupon_code(total_price, coupon_code):
    """Apply the coupon code to the total price."""
    discount = calculate_discount(coupon_code)
    discounted_price = total_price * (1 - discount)
    return discounted_price, discount * 100  # Return discount percentage

def on_apply_coupon():
    """Event handler for applying the coupon."""
    try:
        total_price = float(entry_total_price.get())
        coupon_code = entry_coupon_code.get()

        if len(coupon_code) != 5 or not coupon_code.isdigit():
            messagebox.showerror("Invalid Coupon Code", "Please enter a valid 5-digit numeric coupon code.")
            return

        discounted_price, discount_percentage = apply_coupon_code(total_price, coupon_code)
        label_discounted_price.config(text=f"Discounted Price: {discounted_price:.2f}")
        label_discount_percentage.config(text=f"Discount Applied: {discount_percentage}%")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid total price.")

def on_generate_coupon():
    """Event handler for generating a coupon code."""
    coupon_code = generate_coupon_code()
    entry_coupon_code.delete(0, tk.END)
    entry_coupon_code.insert(0, coupon_code)

# Create the main window
root = tk.Tk()
root.title("Shopping Cart - Apply Coupon Code")
# Create a canvas
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack()

heading_text = "My Shopping Cart"
canvas.create_text(200, 20, text=heading_text, font=("Arial", 20), fill="Black")

# Create and place the widgets on the canvas
label_total_price = tk.Label(root, text="Total Price:")
canvas.create_window(100, 60, window=label_total_price)

entry_total_price = tk.Entry(root)
canvas.create_window(250, 60, window=entry_total_price)

label_coupon_code = tk.Label(root, text="Coupon Code:")
canvas.create_window(100, 100, window=label_coupon_code)

entry_coupon_code = tk.Entry(root)
canvas.create_window(250, 100, window=entry_coupon_code)

button_generate_coupon = tk.Button(root, text="Generate Coupon Code", command=on_generate_coupon)
canvas.create_window(100, 140, window=button_generate_coupon)

button_apply_coupon = tk.Button(root, text="Apply Coupon", command=on_apply_coupon)
canvas.create_window(250, 140, window=button_apply_coupon)

label_discounted_price = tk.Label(root, text="Discounted Price: 0.00")
canvas.create_window(200, 180, window=label_discounted_price)

label_discount_percentage = tk.Label(root, text="Discount Applied: 0%")
canvas.create_window(200, 220, window=label_discount_percentage)

# Run the main loop
root.mainloop()