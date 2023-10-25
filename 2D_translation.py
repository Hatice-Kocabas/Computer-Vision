import tkinter as tk
import math

root = tk.Tk()
root.title("2D Translation")
root.geometry("600x400")

point_list = []

tx = tk.StringVar()
ty = tk.StringVar()
rotation_angle = tk.StringVar()
scaling_ratio = tk.StringVar()


def show_transformed_points(transformed_points):
    canvas.delete("all")
    for point in transformed_points:
        x, y = point
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3,
                           fill="green")


def transform():
    tx_value = float(tx.get())
    ty_value = float(ty.get())
    rot_angle_val = math.radians(float(rotation_angle.get()))
    scaling_ratio_val = float(scaling_ratio.get())

    transformed_points = []
    for point in point_list:
        x, y = point
        new_x = scaling_ratio_val * (x * math.cos(rot_angle_val) -
                                     y * math.sin(rot_angle_val)) + tx_value
        new_y = scaling_ratio_val * (x * math.sin(rot_angle_val) +
                                     y * math.cos(rot_angle_val)) + ty_value
        transformed_points.append((new_x, new_y))

    show_transformed_points(transformed_points)


def on_click(event):
    x, y = event.x, event.y
    point_list.append((x, y))
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="blue")


canvas = tk.Canvas(root, width=300, height=300, bg="lightgray")
canvas.pack(side=tk.LEFT)
canvas.bind("<Button-1>", on_click)

input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=10)

tk.Label(input_frame, text="Tx:", fg="blue").grid(
    row=0, column=0)
tx_input = tk.Entry(input_frame, textvariable=tx, width=10)
tx_input.grid(row=0, column=1)

tk.Label(input_frame, text="Ty:", fg="blue").grid(
    row=1, column=0)
ty_input = tk.Entry(input_frame, textvariable=ty, width=10)
ty_input.grid(row=1, column=1)

tk.Label(input_frame, text="Rotation Angle :",
         fg="blue").grid(row=2, column=0)
rot_angle_input = tk.Entry(input_frame, textvariable=rotation_angle,
                           width=10)
rot_angle_input.grid(row=2, column=1)

tk.Label(input_frame, text="Scaling Ratio:", fg="blue").grid(
    row=3, column=0)
scaling_ratio_input = tk.Entry(
    input_frame, textvariable=scaling_ratio, width=10)
scaling_ratio_input.grid(row=3, column=1)

btn_transform = tk.Button(input_frame, text="Transform",
                          command=transform, bg="red", fg="white")
btn_transform.grid(row=4, columnspan=2)

root.mainloop()
