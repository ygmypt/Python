import tkinter as tk
import matplotlib.pyplot as plt

def calculate_chart():
    vitamin_a_values = [int(entry_vitamin_a_1.get()), int(entry_vitamin_a_2.get()), int(entry_vitamin_a_3.get()), int(entry_vitamin_a_4.get())]
    vitamin_b_values = [int(entry_vitamin_b_1.get()), int(entry_vitamin_b_2.get()), int(entry_vitamin_b_3.get()), int(entry_vitamin_b_4.get())]
    vitamin_d_values = [int(entry_vitamin_d_1.get()), int(entry_vitamin_d_2.get()), int(entry_vitamin_d_3.get()), int(entry_vitamin_d_4.get())]

    total_vitamin_a = sum(vitamin_a_values)
    total_vitamin_b = sum(vitamin_b_values)
    total_vitamin_d = sum(vitamin_d_values)

    labels = 'Витамин A', 'Витамин B', 'Витамин D'
    sizes = [total_vitamin_a, total_vitamin_b, total_vitamin_d]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()

root = tk.Tk()
root.title("Расчет витаминов")

label_vitamin_a = tk.Label(root, text="Витамин A")
label_vitamin_a.grid(row=0, column=0)
entry_vitamin_a_1 = tk.Entry(root)
entry_vitamin_a_1.grid(row=1, column=0)
entry_vitamin_a_2 = tk.Entry(root)
entry_vitamin_a_2.grid(row=2, column=0)
entry_vitamin_a_3 = tk.Entry(root)
entry_vitamin_a_3.grid(row=3, column=0)
entry_vitamin_a_4 = tk.Entry(root)
entry_vitamin_a_4.grid(row=4, column=0)

label_vitamin_b = tk.Label(root, text="Витамин B")
label_vitamin_b.grid(row=0, column=1)
entry_vitamin_b_1 = tk.Entry(root)
entry_vitamin_b_1.grid(row=1, column=1)
entry_vitamin_b_2 = tk.Entry(root)
entry_vitamin_b_2.grid(row=2, column=1)
entry_vitamin_b_3 = tk.Entry(root)
entry_vitamin_b_3.grid(row=3, column=1)
entry_vitamin_b_4 = tk.Entry(root)
entry_vitamin_b_4.grid(row=4, column=1)

label_vitamin_d = tk.Label(root, text="Витамин D")
label_vitamin_d.grid(row=0, column=2)
entry_vitamin_d_1 = tk.Entry(root)
entry_vitamin_d_1.grid(row=1, column=2)
entry_vitamin_d_2 = tk.Entry(root)
entry_vitamin_d_2.grid(row=2, column=2)
entry_vitamin_d_3 = tk.Entry(root)
entry_vitamin_d_3.grid(row=3, column=2)
entry_vitamin_d_4 = tk.Entry(root)
entry_vitamin_d_4.grid(row=4, column=2)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_chart)
calculate_button.grid(row=5, columnspan=3)

root.mainloop()
