import tkinter as tk

def show_output():
    number = int(number_input.get())
    if number == 0:
        output_label.configure(text='0 x Everything = 0')
        return

    output = ''
    for i in range(1, 26):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)

windows = tk.Tk()
windows.title('Multiplication table')
windows.minsize(width = 500, height = 500)

title_label = tk.Label(master=windows, text='Table')
title_label.pack(pady=5)

number_input = tk.Entry(master=windows)
number_input.pack(pady=5)

ex_button = tk.Button(
    master=windows, text='Execute',
    command=show_output, width=12, height=2,
    font=('Helvetica', 12)
    )
ex_button.pack(pady=5)

output_label = tk.Label(master=windows)
output_label.pack(pady=15)

windows.mainloop()