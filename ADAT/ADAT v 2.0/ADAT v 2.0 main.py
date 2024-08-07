import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("ADAT advanced dos attack tool")


# Set the window size
root.geometry("800x600")

# Function to display help message
def show_help():
    messagebox.showinfo("Help", "ADAT advanced Dos attack tool "
                                "By NVRK SAI KAMESH YADAVALLI")

# Create the menu bar
menu_bar = tk.Menu(root)

# Create the "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_help)

# Add the "Help" menu to the menu bar
menu_bar.add_cascade(label="Help", menu=help_menu)

# tool banner
banner_ui = tk.Label(root,text="ADAT \n Advanced Dos Attack Tool")
banner_ui_2 = tk.Label(root,text="By NVRK SAI KAMESH YADAVALLI")

# Display the menu bar in the main window
root.config(menu=menu_bar)

# Create labels 
ip_name = tk.Label(root,text="Enter the ip or server name ")
port_num = tk.Label(root,text="Enter the port ")
packet_sel = tk.Label(root,text="PAcket type Ex icmp tcp udp")
command_line = tk.Label(root,width=50,height=50)

# Create input fields
ip = tk.Entry(root)
port = tk.Entry(root)
packet_sel_entry = tk.Entry(root)
# Create the button
button = tk.Button(root, text="Submit")

# Use grid layout to arrange the widgets
banner_ui.grid(row=0,column=0,padx=20,pady=20)
banner_ui_2.grid(row=0,column=1,padx=20,pady=20)
ip_name.grid(row=1,column=0,padx=20,pady=20)
ip.grid(row=1, column=1, padx=20, pady=20)
port_num.grid(row=2,column=0,padx=20,pady=20)
port.grid(row=2, column=1, padx=20, pady=20)
packet_sel.grid(row=3,column=0,padx=20,pady=20)
packet_sel_entry.grid(row=3,column=1,padx=20,pady=20)
button.grid(row=4, column=1, padx=20, pady=20)
command_line.grid(row=5,column=0,padx=20,pady=20)


# Start the main event loop
root.mainloop()
