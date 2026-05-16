import customtkinter as ctk
from pathlib import Path

app = ctk.CTk()
app.geometry("400x540")
app.resizable(False, False)
app.title("AutoReply")
app.configure(fg_color=("#30302e"))

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

# --- status frame

# frame
status_frame = ctk.CTkFrame(app, width=350, height=230, corner_radius=10, fg_color="#262624")
status_frame.grid(row=0, column=0, columnspan=2, padx=25, pady=35)

# status text
status_text_stopped_primary = ctk.CTkLabel(status_frame, text="Stopped", font=ctk.CTkFont(family="SF Pro Display", size=28))
status_text_stopped_primary.grid(row=0, column=0, padx=175, pady=115)

start_btn = ctk.CTkButton(app,
                                                    width=350, 
                                                    height=35, 
                                                    fg_color="transparent",
                                                    border_color="grey",
                                                    border_width=1,
                                                    corner_radius=10, 
                                                    text="▶  Start", 
                                                    font=ctk.CTkFont(family="SF Pro Display", size=14)
                                                    )
start_btn.grid(row=1, column=0, columnspan=2, padx=20, pady=0)

replies_summary_frame = ctk.CTkFrame(app, 
                                     width=170,
                                     height=70,
                                     fg_color="#262624")
replies_summary_frame.grid(row=2, column=0, padx=(25, 5), pady=25, sticky="w")

report_time_frame = ctk.CTkFrame(app,
                                 width=170,
                                 height=70,
                                 fg_color="#262624"
                                 )
report_time_frame.grid(row=2, column=1, padx=(5, 25), pady=0, sticky="w")

# --- navigation buttons (home, whitelist, report, settings)

# frame
nav_frame = ctk.CTkFrame(app, fg_color="#30302e", corner_radius=0)
nav_frame.grid(row=3, column=0, columnspan=2, sticky="sew", padx=0, pady=0)

nav_frame.columnconfigure(0, weight=1)
nav_frame.columnconfigure(1, weight=1)
nav_frame.columnconfigure(2, weight=1)
nav_frame.columnconfigure(3, weight=1)

app.rowconfigure(3, weight=1)

# buttons
home_btn = ctk.CTkButton(nav_frame, text="⌂\nHome", fg_color="transparent", corner_radius=5, border_color="grey", border_width=1, )
home_btn.grid(row=0, column=0, sticky="ew", ipady=15)

whitelist_btn = ctk.CTkButton(nav_frame, text="👥\nWhitelist", fg_color="transparent", corner_radius=5, border_color="grey", border_width=1)
whitelist_btn.grid(row=0, column=1, sticky="ew", ipady=15)

home_btn = ctk.CTkButton(nav_frame, text="📊\nReport", fg_color="transparent", corner_radius=5, border_color="grey", border_width=1)
home_btn.grid(row=0, column=2, sticky="ew", ipady=15)

home_btn = ctk.CTkButton(nav_frame, text="⚙\nSettings", fg_color="transparent", corner_radius=5, border_color="grey", border_width=1)
home_btn.grid(row=0, column=3, sticky="ew", ipady=15)

app.mainloop()
