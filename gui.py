import customtkinter as ctk
from pathlib import Path

app = ctk.CTk()
app.geometry("500x500")
app.title("AutoReply")


frame = ctk.CTkFrame(app, width=400, height=150, fg_color="grey")
frame.grid(row=0, column=0, padx=15, pady=15)

change_busy_intervals_btn = ctk.CTkButton(app,
                                                    width=100, 
                                                    height=25, 
                                                    corner_radius=5, 
                                                    text="Change busy intervals", 
                                                    font=ctk.CTkFont(family="SF Pro Display", size=14)
                                                    )
change_busy_intervals_btn.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()

