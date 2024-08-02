import socket
import os
import time
import tkinter as tk
from tkinter import filedialog, Tk, Label, Entry, Button, messagebox
import threading

class Fxg(Tk):
    def __init__(log):
        super(Fxg, log).__init__()

        log.title("UDP Nav loger")
        log.minsize(150, 70)
        log.Ip()
        log.Ipe()
        log.Port()
        log.Porte()
        log.Start()
        log.Quit()

    def Ip(log):
        log.Ip_l = Label(log, text="Enter IP adress:")
        log.Ip_l.grid(column = 1, row = 1)

    def Ipe(log):
        
        log.Ip_e = tk.Entry(log)
        log.Ip_e.grid(column = 2, row = 1)
        log.Ip_e.insert(0,"10.146.144.63")

    def Port(log):
        
        log.Port_l = Label(log, text="Enter port:")
        log.Port_l.grid(column = 1, row = 2)

    def Porte(log):
        
        log.Port_e = tk.Entry(log)
        log.Port_e.grid(column = 2, row = 2)
        log.Port_e.insert(0,"1111")

    def Quit(log):
        log.exit = tk.Button(width = 16,text = "Exit ", command=log.Exit )
        log.exit.grid(column = 2, row = 3)

    def Run(log):
        
        
        try:
            IP_ADDRESS = log.Ip_e.get()
        except ValueError:
            messagebox.showinfo("failed to get IP")
            return
        
        try:
            PORT_set = int(log.Port_e.get())
        except ValueError:
            messagebox.showinfo("failed to get Port number")
            return
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((IP_ADDRESS, PORT_set))
        print(f"Listening on {IP_ADDRESS}:{PORT_set}...")

        try:
            log_file = open("udp_log.txt", "a")
        except ValueError:
            return

        while True:
            log_file = open("udp_log.txt", "a")
            data, addr = sock.recvfrom(1024)
            log_file.write(data.decode())
            print(f"Received data {data}")
            log_file.close()
                                                 
    def Start(log):
        t1 = threading.Thread(target=log.Run)
        log.start = tk.Button(width = 16,text = "Start", command=t1.start )
        log.start.grid(column = 1, row = 3)

    def Exit(log):
        
        log.destroy
        os._exit(1)
    
fxg = Fxg()
fxg.mainloop()
