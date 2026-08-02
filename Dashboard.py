from tkinter import *
from tkinter import messagebox
from Analysis import *

# ----------------------------------------------------------
# Load and Clean Dataset
# ----------------------------------------------------------
clean_data()

# ----------------------------------------------------------
# Function to Open Description First, Then Graph
# ----------------------------------------------------------

def open_graph_with_description(graph_function, title, description):

    desc = Toplevel(root)
    desc.title(title)
    desc.geometry("800x450")
    desc.configure(bg="white")

    # Heading
    Label(
        desc,
        text=title,
        font=("Helvetica", 18, "bold"),
        bg="white",
        fg="#E50914"
    ).pack(pady=15)

    # Description
    msg = Message(
        desc,
        text=description,
        width=720,
        font=("Arial", 13),
        bg="white",
        fg="black",
        justify=LEFT
    )

    msg.pack(pady=20)

    # Show Graph Button
    Button(
        desc,
        text="Show Graph",
        font=("Arial", 13, "bold"),
        bg="#E50914",
        fg="white",
        width=20,
        command=lambda: graph_function()
    ).pack(pady=10)

    # Close Button
    Button(
        desc,
        text="Close",
        font=("Arial", 13, "bold"),
        bg="gray30",
        fg="white",
        width=20,
        command=desc.destroy
    ).pack(pady=10)
    

# ----------------------------------------------------------
# Create Main Window
# ----------------------------------------------------------
root = Tk()
root.title("Netflix Data Analysis Dashboard")
root.state("zoomed")
root.configure(bg="#252525")   # Dark Background

# ----------------------------------------------------------
# Hover Effects
# ----------------------------------------------------------
def on_enter(e):
    e.widget["background"] = "#E50914"

def on_leave(e):
    e.widget["background"] = "#252525"

# ----------------------------------------------------------
# Dashboard Title
# ----------------------------------------------------------
title = Label(
    root,
    text="NETFLIX DATA ANALYSIS DASHBOARD",
    font=("Helvetica", 28, "bold"),
    bg="#E50914",
    fg="white",
    pady=18
)
title.pack(fill=X)

# ----------------------------------------------------------
# Subtitle
# ----------------------------------------------------------
subtitle = Label(
    root,
    text="Interactive Visualization using Python • Pandas • Plotly • Tkinter",
    font=("Calibri", 16),
    bg="#1A1A1A",
    fg="#DDDDDD",
    pady=10
)
subtitle.pack()

# ----------------------------------------------------------
# Welcome Message
# ----------------------------------------------------------
welcome = Label(
    root,
    text="Select any visualization below to explore the Netflix dataset",
    font=("Calibri", 14, "italic"),
    bg="#1A1A1A",
    fg="white",
    pady=10
)
welcome.pack()

# ----------------------------------------------------------
# Button Frame
# ----------------------------------------------------------
button_frame = Frame(root, bg="#1A1A1A")
button_frame.pack(expand=True)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

# ----------------------------------------------------------
# Button Style
# ----------------------------------------------------------
button_font = ("Calibri", 14, "bold")

button_width = 32
button_height = 2

button_bg = "#252525"
button_fg = "white"

active_bg = "#FF0000"
active_fg = "white"

# ----------------------------------------------------------
# Button 1
# ----------------------------------------------------------
btn1 = Button(
    button_frame,
    text="📊 Distribution of Content Ratings",
    font=button_font,
    width=button_width,
    height=button_height,
    bg=button_bg,
    fg=button_fg,
    activebackground=active_bg,
    activeforeground=active_fg,
    relief=FLAT,
    bd=0,
    cursor="hand2",
   command=lambda: open_graph_with_description(
    show_content_rating_pie,
    "Distribution of Content Ratings",
    """This pie chart illustrates the distribution of Netflix content based on different content ratings
      such as TV-MA, TV-14, TV-PG, PG-13, and others. It helps understand the type of audience targeted 
      by Netflix. The visualization indicates that a significant portion of Netflix's library is intended
        for mature audiences, while the remaining content is distributed across family-friendly and
          children's categories."""
)
)
btn1.grid(row=0, column=0, padx=25, pady=20)
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)

# ----------------------------------------------------------
# Button 2
# ----------------------------------------------------------
btn2 = Button(
    button_frame,
    text="🎬 Top 5 Directors",
    font=button_font,
    width=button_width,
    height=button_height,
    bg=button_bg,
    fg=button_fg,
    activebackground=active_bg,
    activeforeground=active_fg,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=lambda: open_graph_with_description(
    show_top5_directors,
    "Top 5 Directors",
    """This bar chart presents the top five directors who have directed the highest number of titles 
    available on Netflix. The data was obtained by separating multiple directors listed in each record, 
    counting their occurrences, and ranking them accordingly. This analysis highlights the directors who 
    have made the greatest contribution to Netflix's content library and provides insight into the 
    platform's most frequently featured filmmakers."""
)
)
btn2.grid(row=0, column=1, padx=25, pady=20)
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)

# ----------------------------------------------------------
# Button 3
# ----------------------------------------------------------
btn3 = Button(
    button_frame,
    text="⭐ Top 5 Actors",
    font=button_font,
    width=button_width,
    height=button_height,
    bg=button_bg,
    fg=button_fg,
    activebackground=active_bg,
    activeforeground=active_fg,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=lambda: open_graph_with_description(
    show_top5_actors,
    "Top 5 Actors",
    """This visualization displays the five actors who appear most frequently in Netflix movies and 
    TV shows. The cast information was processed by separating individual actor names and counting their
    total appearances across all titles. The graph helps identify the actors who have the strongest
    presence on the platform and reflects the popularity and recurring collaborations of these
    performers in Netflix content."""
)
)
btn3.grid(row=1, column=0, padx=25, pady=20)
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)

# ----------------------------------------------------------
# Button 4
# ----------------------------------------------------------
btn4 = Button(
    button_frame,
    text="🌍 Top 5 Countries",
    font=button_font,
    width=button_width,
    height=button_height,
    bg=button_bg,
    fg=button_fg,
    activebackground=active_bg,
    activeforeground=active_fg,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=lambda: open_graph_with_description(
    show_top5_countries,
    "Top 5 Countries",
    """This bar chart shows the five countries that have contributed the highest number of movies and
      TV shows to Netflix. The country information was processed by separating multiple countries 
      listed for a title and counting their occurrences individually. This analysis provides an overview 
      of the major content-producing countries and demonstrates Netflix's global distribution of 
      entertainment content."""
)
)
btn4.grid(row=1, column=1, padx=25, pady=20)
btn4.bind("<Enter>", on_enter)
btn4.bind("<Leave>", on_leave)

# ----------------------------------------------------------
# Button 5
# ----------------------------------------------------------
btn5 = Button(
    button_frame,
    text="📈 Content Produced by Year",
    font=button_font,
    width=button_width,
    height=button_height,
    bg=button_bg,
    fg=button_fg,
    activebackground=active_bg,
    activeforeground=active_fg,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=lambda: open_graph_with_description(
    show_content_trend,
    "Content Produced by Year",
    """This line chart illustrates the yearly trend of movies and TV shows released on Netflix from 
    recent years onward. It compares the growth of both content types over time, enabling users to 
    observe production patterns and changes in content availability. The visualization highlights the 
    rapid increase in Netflix content production in recent years, reflecting the platform's expansion 
    and growing investment in original programming."""
)
)
btn5.grid(row=2, column=0, padx=25, pady=20)
btn5.bind("<Enter>", on_enter)
btn5.bind("<Leave>", on_leave)

# ----------------------------------------------------------
# Button 6
# ----------------------------------------------------------
btn6 = Button(
    button_frame,
    text="😊 Sentiment Analysis",
    font=button_font,
    width=button_width,
    height=button_height,
    bg=button_bg,
    fg=button_fg,
    activebackground=active_bg,
    activeforeground=active_fg,
    relief=FLAT,
    bd=0,
    cursor="hand2",
   command=lambda: open_graph_with_description(
    show_sentiment_analysis,
    "Sentiment Analysis",
    """This bar chart represents the sentiment analysis of Netflix content descriptions using the 
    TextBlob library. Each description was classified as Positive, Neutral, or Negative based on its 
    polarity score, and the results were grouped by release year. The visualization provides an overview 
    of the emotional tone of Netflix content over time and demonstrates how natural language processing 
    techniques can be applied to analyze textual data."""
)
)
btn6.grid(row=2, column=1, padx=25, pady=20)
btn6.bind("<Enter>", on_enter)
btn6.bind("<Leave>", on_leave)

# ----------------------------------------------------------
# Exit Function
# ----------------------------------------------------------
def exit_dashboard():
    answer = messagebox.askyesno(
        "Exit Dashboard",
        "Do you really want to exit the dashboard?"
    )

    if answer:
        root.destroy()

# ----------------------------------------------------------
# Exit Button
# ----------------------------------------------------------
exit_btn = Button(
    root,
    text="EXIT DASHBOARD",
    font=("Calibri", 15, "bold"),
    width=22,
    height=2,
    bg="#B22222",
    fg="white",
    activebackground="#8B0000",
    activeforeground="white",
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=exit_dashboard
)
exit_btn.pack(pady=20)

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------
footer = Label(
    root,
    text="Netflix Data Analysis Project | Summer Training | Python | Pandas | Plotly | Tkinter",
    font=("Calibri", 11),
    bg="#111111",
    fg="#DDDDDD",
    pady=10
)
footer.pack(side=BOTTOM, fill=X)

# ----------------------------------------------------------
# Run Dashboard
# ----------------------------------------------------------
root.mainloop()