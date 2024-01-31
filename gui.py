import tkinter as tk
import tkinter.filedialog as fd
import os

window = tk.Tk()
window.geometry("600x250")
window.title('Data Charter')

window_font = ('Calibri', 13)
window_font_bold = ('Calibri', 14, 'bold')

sel_files = ''
columns = []

def select_files():
    global sel_files
    filetype = [('CSV file', '*.csv')]
    sel_files = fd.askopenfilenames(filetypes=filetype, title='Choose File(s)')
    file_names = strip_file_names(sel_files)
    files_label.config(text=file_names)

def confirm_form():
    global columns
    input_columns = columns_input.get().split(',')
    for col in input_columns:
      columns.append(col.strip())
    window.destroy()

def strip_file_names(files):
  file_names = []
  for file in files:
    file_names.append(os.path.basename(file).strip('.csv'))
  return file_names

files_btn = tk.Button(
   window,
   text='Select File(s)',
   padx=5,
   cursor='hand2',
   foreground='#ffffff',
   background='#9ba5b3',
   activeforeground='#ffffff',
   activebackground='#717985',
   font=window_font_bold, 
   command=lambda: select_files()
)
files_btn.pack(pady=10, side='top')

files_label = tk.Label(text=sel_files, wraplength=400, font=window_font)
files_label.pack(pady=10)

columns_label = tk.Label(text="Input comma separated column names", justify='left', font=window_font)
columns_label.pack()

columns_input = tk.Entry(window, width=50, font=window_font)
columns_input.pack()

confirm_btn = tk.Button(
   window, 
   text='OK', 
   width=10, 
   font=window_font_bold, 
   cursor='hand2', 
   foreground='#ffffff', 
   background='#3f6fe8', 
   activeforeground='#ffffff', 
   activebackground='#113899', 
   command=lambda: confirm_form()
)
confirm_btn.pack(pady=10, side='bottom')

window.mainloop()