from pynput import mouse
import tkinter as tk
from tkinter import ttk
import pyautogui
import time
# Tạo một cửa sổ tkinter
root = tk.Tk()
root.title('Toa_Do (⌐■_■)')
root.geometry('50x20')
label_X = tk.Label(root)  
label_Y = tk.Label(root)  
label_T = tk.Label(root)  
label_P = tk.Label(root)  
 
# entry_Y = tk.Entry(root)  
# entry_T = tk.Entry(root)  
# entry_P = tk.Entry(root)  
label_X.pack()
label_Y.pack()

# X = tk.StringVar()
# Y = tk.StringVar()

def on_move(x, y):
    # t = int(entry_T.get())
    # print(f'Coordinates: ({x}, {y}, {t}')
    # int(entry_Y.get())
    # Cập nhật tọa độ chuột lên cửa sổ tkinter
    label_X.config(text=' (X: {0}__Y: {1})'.format(x,y))
    # label_X.config(text=' (X: {0})'.format(x))
    # label_Y.config(text=' (Y: {0})'.format(y))
    # pyautogui.moveTo(x, y)
    
    root.update()
    
    # label_T.config(text='Time:')
    # entry_T = tk.Entry(root)
    # entry_T.pack()

# TextBox Creation 
#     X1 = X_entry.get(1.0, "end-1c") 

# X_label = ttk.Label( text="X1:")
# X_label.pack(fill='x', expand=False)

# X_entry = ttk.Entry( textvariable=X)
# X_entry.pack(padx=2, pady=2,fill='x', expand=False)
# X_entry.focus()

# Y_label = ttk.Label( text="Y1:")
# Y_label.pack(fill='x', expand=False)

# Y_entry = ttk.Entry( textvariable=Y)
# Y_entry.pack(padx=2, pady=2,fill='x', expand=False)
# Y_entry.focus()

# inputtxt1 = tk.Text(root, 
#                    height = 3, 
#                    width = 5) 

# inputtxt2 = tk.Text(root, 
#                    height = 3, 
#                    width = 5) 
  
# inputtxt1.pack() 
# inputtxt2.pack() 
# Khởi tạo một listener cho sự kiện di chuyển của chuột


with mouse.Listener(on_move=on_move) as listener:
    root.mainloop()
# #!/usr/bin/env python3



# # Move the mouse to the coordinates where you want to click
# pyautogui.moveTo(100, 150)

# # Perform a left-click
# pyautogui.click()

# # Wait for a short duration before pressing the key
# time.sleep(0.5)

# # Perform the key press
# pyautogui.press('a')