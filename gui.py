import customtkinter as ctk
from pathlib import Path

app = ctk.CTk()
app.geometry("400x540")
app.resizable(False, False)
app.title("AutoReply")
app.configure(fg_color=("#30302e"))

frame = ctk.CTkFrame(app, width=350, height=230, corner_radius=10, fg_color="#262624")
frame.grid(row=0, column=0, padx=25, pady=35)

start_btn = ctk.CTkButton(app,
                                                    width=350, 
                                                    height=35, 
                                                    fg_color="transparent",
                                                    border_color="grey",
                                                    border_width=1,
                                                    corner_radius=10, 
                                                    text="Start", 
                                                    font=ctk.CTkFont(family="SF Pro Display", size=14)
                                                    )
start_btn.grid(row=1, column=0, padx=20, pady=0)

replies_summary_frame = ctk.CTkFrame(app, 
                                     width=170,
                                     height=70,
                                     fg_color="#262624")
replies_summary_frame.grid(padx=0, pady=20, )

app.mainloop()
