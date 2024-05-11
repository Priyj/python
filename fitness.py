pip install requests
pip install pillow
pip install tkhtmlview
from tkhtmlview import HTMLLabel
from tkinter import messagebox
import simple_colors as color
import pygame
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import requests
from datetime import datetime, time as datetime_time
import threading
import time
from tkinter import ttk
import subprocess
import webbrowser
from tkinter import PhotoImage
from io import BytesIO

def show_window1():
    sign.withdraw()
    root.deiconify()

def show_window2():
    root.withdraw()
    sign.deiconify()

def dict_exercise(difficulty_level):
    beginner_weight_loss_exercise_dict = {
    "day1": {
        "\n<==Full Body==>\n": ["\tWalking", "\tJumping Jacks", "\tBodyweight Squats", "\tPush-Ups", "\tPlanks"]
    },
    "day2": {
        "\n<==Full Body==>\n": ["\tBicycling", "\tSwimming", "\tBodyweight Lunges", "\tPush-Ups", "\tPlanks"]
    },
    "day3": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Core==>\n": ["\tPlanks", "\tRussian Twists", "\tBicycle Crunches", "\tLeg Raises", "\tMountain Climbers"]
    },
    "day4": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Strength==>\n": ["\tPush-Ups", "\tSquats", "\tLunges", "\tDumbbell Rows", "\tDumbbell Press"]
    },
    "day5": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    },
    "day6": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Core==>\n": ["\tPlanks", "\tRussian Twists", "\tBicycle Crunches", "\tLeg Raises", "\tMountain Climbers"]
    },
    "day7": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Strength==>\n": ["\tPush-Ups", "\tSquats", "\tLunges", "\tDumbbell Rows", "\tDumbbell Press"]
    }}
    
     
    intermediate_weight_loss_exercise_dict = {
    "day1": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Core==>\n": ["\tPlanks", "\tRussian Twists", "\tBicycle Crunches", "\tLeg Raises", "\tMountain Climbers"]
    },
    "day2": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Strength==>\n": ["\tPush-Ups", "\tSquats", "\tLunges", "\tDumbbell Rows", "\tDumbbell Press"]
    },
    "day3": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Strength==>\n": ["\tBench Press", "\tDumbbell Flyes", "\tIncline Bench Press", "\tPush-Ups", "\tChest Press"]
    },
    "day4": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Strength==>\n": ["\tDeadlifts", "\tPull-Ups", "\tBent Over Rows", "\tLat Pulldowns", "\tT-Bar Rows"]
    },
    "day5": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    },
    "day6": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tJump Rope", "\tStair Climbing", "\tHigh Knees"],
        "\n<==Strength==>\n": ["\tMilitary Press", "\tLateral Raises", "\tFront Raises", "\tShrugs", "\tFace Pulls"]
    },
    "day7": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    }}
    
    
    advanced_weight_loss_exercise_dict = {
    "day1": {
        "\n<==Cardio==>\n": ["\tHigh-Intensity Interval Training (HIIT)", "\tRunning", "\tCycling", "\tSwimming", "\tJump Rope"]
    },
    "day2": {
        "\n<==Strength Training==>\n": ["\tFull-Body Resistance Workout", "\tDeadlifts", "\tSquats", "\tBench Press", "\tPull-Ups"]
    },
    "day3": {
        "\n<==Cardio==>\n": ["\tHigh-Intensity Interval Training (HIIT)", "\tRunning", "\tCycling", "\tSwimming", "\tJump Rope"]
    },
    "day4": {
        "\n<==Strength Training==>\n": ["\tFull-Body Resistance Workout", "\tDeadlifts", "\tSquats", "\tBench Press", "\tPull-Ups"]
    },
    "day5": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    },
    "day6": {
        "\n<==Cardio==>\n": ["\tHigh-Intensity Interval Training (HIIT)", "\tRunning", "\tCycling", "\tSwimming", "\tJump Rope"]
    },
    "day7": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    }}
    
    
    beginner_muscle_gain_exercise_dict = {
    "day1": {
        "\n<==Chest==>\n": ["\tBench Press", "\tPush-Ups", "\tDumbbell Flyes", "\tChest Press", "\tIncline Bench Press"],
        "\n<==Triceps==>\n": ["\tTricep Dips", "\tSkull Crushers", "\tTricep Pushdowns", "\tClose-Grip Bench Press", "\tDiamond Push-Ups"]
    },
    "day2": {
        "\n<==Back==>\n": ["\tDeadlifts", "\tPull-Ups", "\tBent Over Rows", "\tLat Pulldowns", "\tT-Bar Rows"],
        "\n<==Biceps==>\n": ["\tBicep Curls", "\tHammer Curls", "\tChin-Ups", "\tPreacher Curls", "\tIncline Dumbbell Curls"]
    },
    "day3": {
        "\n<==Legs==>\n": ["\tSquats", "\tLeg Press", "\tLunges", "\tDeadlifts", "\tCalf Raises"]
    },
    "day4": {
        "\n<==Shoulders==>\n": ["\tMilitary Press", "\tLateral Raises", "\tFront Raises", "\tShrugs", "\tFace Pulls"],
        "\n<==Traps==>\n": ["\tFarmer's Walks", "\tUpright Rows", "\tTrap Bar Shrugs", "\tBarbell Shrugs", "\tTrap 3 Raises"]
    },
    "day5": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    },
    "day6": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tSwimming", "\tJump Rope", "\tStair Climbing"],
        "\n<==Core==>\n": ["\tPlanks", "\tRussian Twists", "\tBicycle Crunches", "\tLeg Raises", "\tMountain Climbers"]
    },
    "day7": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    }}
    
    
    intermediate_muscle_gain_exercise_dict = {
    "day1": {
        "\n<==Chest==>\n": ["\tBench Press", "\tPush-Ups", "\tDumbbell Flyes", "\tChest Press", "\tIncline Bench Press"],
        "\n<==Triceps==>\n": ["\tTricep Dips", "\tSkull Crushers", "\tTricep Pushdowns", "\tClose-Grip Bench Press", "\tDiamond Push-Ups"]
    },
    "day2": {
        "\n<==Back==>\n": ["\tDeadlifts", "\tPull-Ups", "\tBent Over Rows", "\tLat Pulldowns", "\tT-Bar Rows"],
        "\n<==Biceps==>\n": ["\tBicep Curls", "\tHammer Curls", "\tChin-Ups", "\tPreacher Curls", "\tIncline Dumbbell Curls"]
    },
    "day3": {
        "\n<==Legs==>\n": ["\tSquats", "\tLeg Press", "\tLunges", "\tDeadlifts", "\tCalf Raises"]
    },
    "day4": {
        "\n<==Shoulders==>\n": ["\tMilitary Press", "\tLateral Raises", "\tFront Raises", "\tShrugs", "\tFace Pulls"],
        "\n<==Traps==>\n": ["\tFarmer's Walks", "\tUpright Rows", "\tTrap Bar Shrugs", "\tBarbell Shrugs", "\tTrap 3 Raises"]
    },
    "day5": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    },
    "day6": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tSwimming", "\tJump Rope", "\tStair Climbing"],
        "\n<==Core==>\n": ["\tPlanks", "\tRussian Twists", "\tBicycle Crunches", "\tLeg Raises", "\tMountain Climbers"]
    },
    "day7": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    }}
    
    
    advanced_muscle_gain_exercise_dict = {
    "day1": {
        "\n<==Chest==>\n": ["\tBench Press", "\tDumbbell Flyes", "\tIncline Bench Press", "\tPush-Ups", "\tChest Press"],
        "\n<==Triceps==>\n": ["\tTricep Dips", "\tSkull Crushers", "\tTricep Pushdowns", "\tClose-Grip Bench Press", "\tDiamond Push-Ups"]
    },
    "day2": {
        "\n<==Back==>\n": ["\tDeadlifts", "\tPull-Ups", "\tBent Over Rows", "\tLat Pulldowns", "\tT-Bar Rows"],
        "\n<==Biceps==>\n": ["\tBicep Curls", "\tHammer Curls", "\tChin-Ups", "\tPreacher Curls", "\tIncline Dumbbell Curls"]
    },
    "day3": {
        "\n<==Legs==>\n": ["\tSquats", "\tLeg Press", "\tLunges", "\tDeadlifts", "\tCalf Raises"]
    },
    "day4": {
        "\n<==Shoulders==>\n": ["\tMilitary Press", "\tLateral Raises", "\tFront Raises", "\tShrugs", "\tFace Pulls"],
        "\n<==Traps==>\n": ["\tFarmer's Walks", "\tUpright Rows", "\tTrap Bar Shrugs", "\tBarbell Shrugs", "\tTrap 3 Raises"]
    },
    "day5": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    },
    "day6": {
        "\n<==Cardio==>\n": ["\tRunning", "\tCycling", "\tSwimming", "\tJump Rope", "\tStair Climbing"],
        "\n<==Core==>\n": ["\tPlanks", "\tRussian Twists", "\tBicycle Crunches", "\tLeg Raises", "\tMountain Climbers"]
    },
    "day7": {
        "\n<==Rest Day==>\n": ["\n\t😁"]
    }}
    
    if difficulty_level == "beginner_weight_loss":
        return beginner_weight_loss_exercise_dict
    elif difficulty_level == "intermediate_weight_loss":
        return intermediate_weight_loss_exercise_dict
    elif difficulty_level == "advanced_weight_loss":
        return advanced_weight_loss_exercise_dict
    elif difficulty_level == "beginner_muscle_gain":
        return beginner_muscle_gain_exercise_dict
    elif difficulty_level == "intermediate_muscle_gain":
        return intermediate_muscle_gain_exercise_dict
    elif difficulty_level == "advanced_muscle_gain":
        return advanced_muscle_gain_exercise_dict
    else:
        raise ValueError("Invalid difficulty level")
        
          
def calculate_difficulty():
    global selected_difficulty  # Declare that we're using the global variable
    selected_objective = ov.get()
    selected_level = lv.get()

    if selected_objective == "Weight Loss":
        if selected_level == "Beginner":
            selected_difficulty.set("beginner_weight_loss")
        elif selected_level == "Intermediate":
            selected_difficulty.set("intermediate_weight_loss")
        elif selected_level == "Advanced":
            selected_difficulty.set("advanced_weight_loss")
        else:
            messagebox.showerror("Error", "Invalid fitness level")
    elif selected_objective == "Muscles":
        if selected_level == "Beginner":
            selected_difficulty.set("beginner_muscle_gain")
        elif selected_level == "Intermediate":
            selected_difficulty.set("intermediate_muscle_gain")
        elif selected_level == "Advanced":
            selected_difficulty.set("advanced_muscle_gain")
        else:
            messagebox.showerror("Error", "Invalid fitness level")
    else:
        messagebox.showerror("Error", "Invalid fitness objective")

    difficulty_level=selected_difficulty.get()
    my_dict=dict_exercise(difficulty_level)
    return my_dict

def anos1999():
    rank.withdraw()
    exercises_window.deiconify()
    
def anos2999():
    p.withdraw()
    exercises_window.deiconify()
        
k=2  
rn=0
def day_menu():
    # Define a function to show exercises for a specific day
    
    def anos():
        day_menu()
        exercises_window.withdraw()
        
    def anos99() :
        global rn
        messagebox.showinfo("Congratulations", "You earned 30 points")
        rn=rn+30
        
    selected_time = ""

    # Function to set a reminder
    def set_reminder():
        global selected_time
        selected_time = selected_time_entry.get()  # Get the reminder time from the user
        messagebox.showinfo("Reminder Set", f"Reminder scheduled for {selected_time}")

    def anos19():
        global selected_time  # Declare that we're using the global variable

        # Create a reminder input window
        reminder_window = tk.Toplevel()
        reminder_window.title("Set Reminder")
        reminder_window.geometry("300x100")

        reminder_label = tk.Label(reminder_window, text="Enter reminder time (HH:MM): ")
        reminder_label.pack()

        global selected_time_entry
        selected_time_entry = tk.Entry(reminder_window)
        selected_time_entry.pack()

        set_reminder_button = tk.Button(reminder_window, text="Set Reminder", command=set_reminder)
        set_reminder_button.pack()
        
        
    def anos70() :
        exercises_window.withdraw()
        p.deiconify()
        v = tk.StringVar()
        v.set("Select the song to play")

        os.chdir(askdirectory())
        song_list = os.listdir()

        playing = tk.Listbox(p, font="Helvetica 12 bold", width=28, bg="black", fg="white", selectmode=tk.SINGLE)

        for item in song_list:
            playing.insert(0, item)

        pygame.init()
        pygame.mixer.init()

        def play():
            pygame.mixer.music.load(playing.get(tk.ACTIVE))
            name = playing.get(tk.ACTIVE)
            v.set(f"{name[:16]}..." if len(name) > 18 else name)
            pygame.mixer.music.play()

        def pause():
            pygame.mixer.music.pause()

        def resume():
            pygame.mixer.music.unpause()

        text = tk.Label(p, font="Helvetica", textvariable=v).grid(row=0, columnspan=3)
        playing.grid(columnspan=3)

        play_btn = tk.Button(p, width=7, height=1, font="Helvetica", text="Play", command=play, bg="lightgreen").grid(row=2, column=0)
        pause_btn = tk.Button(p, width=7, height=1, font="Helvetica", text="Pause", command=pause, bg="lightblue", fg="black").grid(row=2, column=1)
        resume_btn = tk.Button(p, width=9, height=1, font="Helvetica", text="Resume", command=resume, bg="lightpink", fg="black").grid(row=2, column=2)

        p.mainloop()

        

    def anos199():
        exercises_window.withdraw()
        rank.deiconify()
        
    def show_exercises(selected_day):
        exercises = exercise_dict[selected_day]
        exercises_window.deiconify()
        day.withdraw()

        # Clear the previous exercises by destroying all children widgets in exercises_window
        for widget in exercises_window.winfo_children():
            widget.destroy()

        # Create a back button to return to the day selection
        back_button = tk.Button(exercises_window, text="Back", command=anos)
        back_button.grid(row=0, column=0, sticky="nw")

        done_button = tk.Button(exercises_window, text="Task Completed", command=anos99)
        done_button.grid(row=0, column=7, sticky="nw")
        
        remind = tk.Button(exercises_window, text="Set reminder for later...", command=anos19)
        remind.grid(row=0, column=14, sticky="nw")
        
        show_rank = tk.Button(exercises_window, text="See Ranking", command=anos199)
        show_rank.grid(row=0, column=21, sticky="nw")
        

        # Display exercises with images
        row = 1
        for body_part, exercise_list in exercises.items():
            tk.Label(exercises_window, text=body_part, font=("Arial", 12)).grid(row=row, column=0, sticky="w")
            row += 1
            for exercise in exercise_list:
                tk.Label(exercises_window, text=exercise).grid(row=row, column=0, sticky="w")
                row += 1


    exercise_dict =calculate_difficulty()
    
    day.deiconify()
    week_.withdraw()
    global k
    if k==2 :
        day_frame1 = tk.Frame(day, bg ="white")
        day_frame1.pack(side="top", fill="x")
        day_frame = tk.Frame(day, bg ="white", height =1080)
        day_frame.pack(side="top", fill="both")
        tk.Button(day_frame1, text="back", highlightbackground="grey", command=anos1).pack(side="left")       
        tk.Button(day_frame1, text="Play Music...", highlightbackground="grey", command=anos70).pack(side="left")     
        # Create buttons for each day
        for day_number in range(1, 8):
            day_name = f"day{day_number}"
            day_button = tk.Button(day_frame, text=day_name, highlightbackground="white", command=lambda day_name=day_name: show_exercises(day_name))
            day_button.grid(row=day_number-1, column=0, sticky="w", padx=10, pady=5)
            button = tk.Button(day_frame, text="Open YouTube Video",highlightbackground="white", command=open_youtube)
            button.grid(row=day_number-1, column=7,padx=20, pady=20)
            
            k += 1
            
i = 1
def Exercise_menu():
    global i
    week_.deiconify()
    main_menu.withdraw()
  
    f7 = tk.Frame(week_, bg="grey", height=70)
    f7.pack(side="top", fill="x")
    l7 = tk.Label(f7, text="Let's Get Started", bg="grey", fg="white")
    l7.pack(side="top")  
    Exercise = tk.Frame(week_, bg="white", highlightbackground="white", height=1000)
    Exercise.pack(side="top", fill="both")
    
    # Get the user input from the 'de' Entry widget
    duration_input = de.get()

    # Check if the input is a valid integer
    try:
        duration_weeks = int(duration_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer for duration.")
    
    frame_list = []  # Create an empty list to store frames
    label_list = []  # Create an empty list to store labels
    button_list = []  # Create an empty list to store buttons

    while i <= duration_weeks:
        if (i - 1) % 7 == 0:
            # Start a new row every 7 weeks
            row_num = (i - 1) // 7
            column_num = 0
        else:
            # Continue in the same row
            row_num = (i - 1) // 7
            column_num = (i - 1) % 7
        
        # Create a new frame
        new_frame = tk.Frame(Exercise, bg="white", highlightbackground="white")
        new_frame.grid(row=row_num, column=column_num, padx=10, pady=20)  # Use grid to place the frames
        
        # Create a label for the week
        label_text = f"WEEK {i}"
        new_label = tk.Label(new_frame, text=label_text, fg="blue", bg="white", highlightbackground="white")
        new_label.grid(row=0, column=0, padx=10)  # Place labels in column 0 of each frame

        # Append the frame, label, and button to their respective lists
        frame_list.append(new_frame)
        label_list.append(new_label)

        def change_label_color(label, week_number):
            label.config(fg="cyan")
            label.config(bg="white")   

        def on_button_click(i):
            change_label_color(label_list[i-1], i)
            day_menu()  # Call your day_menu function here

        new_button = tk.Button(new_frame, text="Go >", highlightbackground="white", command=lambda i=i: on_button_click(i))
        new_button.grid(row=1, column=0, padx=10)  # Place buttons in column 0 of each frame
        button_list.append(new_button)

        i += 1 
    # Create a button_frame to hold all buttons
    button_frame = tk.Frame(Exercise, bg="white", highlightbackground="white")
    button_frame.grid(row=row_num + 1, columnspan=7)  # Span columns to cover all weeks in the last row

# Function to update the rank table
def update_rank_table():
    # Clear the previous data in the Treeview
    global logged_in_user
    global rn
    for item in rank_treeview.get_children():
        rank_treeview.delete(item)

    # Create a list of users and their corresponding points (you can modify this based on your data)
    user_points = {
        logged_in_user:rn,
        "User1": 100,
        "User2": 75,
        "User3": 120,
        "User4": 90,
    }

    # Sort the users based on points in descending order
    sorted_users = sorted(user_points.items(), key=lambda x: x[1], reverse=True)

    # Add data to the Treeview
    for index, (username, points) in enumerate(sorted_users, start=1):
        rank_treeview.insert("", "end", values=(index, username, points))


# Function to open the main menu
def open_main_menu(username):
    main_menu.deiconify()
    root.withdraw()  
    sign.withdraw()
    global de
    global ov
    global lv
    
    f4 = tk.Frame(main_menu, bg="white", height=70)
    f4.pack(side="top", fill="x")    
    
    f5 = tk.Frame(main_menu, bg="grey", width=540, height=980)
    f5.pack(side="left", fill="x")

    l2 = tk.Label(f4, text="Choose Your LEVEL", bg="white", fg="black")
    l2.pack(side="top")
    
    def anos3():
        Exercise_menu()
        calculate_difficulty()
        
    
    # Create a frame to center the widgets
    cf = tk.Frame(main_menu, bd=2, relief=tk.RAISED)
    cf.pack(side="left", padx=40, pady=10)
    
    # Fitness objectives
    ol = tk.Label(cf, text="Select your fitness objective:")
    ol.grid(row=1, column=1)

    objectives = ["Weight Loss", "Muscles"]
    ov = tk.StringVar()
    ov.set(objectives[0])  # Default selection

    om = tk.OptionMenu(cf, ov, *objectives)
    om.grid(row=1, column=2)

    # Fitness levels
    ll = tk.Label(cf, text="Select Difficulty level:")
    ll.grid(row=3, column=1)

    levels = ["Beginner", "Intermediate", "Advanced"]
    lv = tk.StringVar()
    lv.set(levels[0])  # Default selection

    lm = tk.OptionMenu(cf, lv, *levels)
    lm.grid(row=3, column=2)

    # Duration entry
    dl = tk.Label(cf, text="Enter duration (in weeks):")
    dl.grid(row=5, column=1)

    de = tk.Entry(cf)
    de.grid(row=5, column=2)   
 
    # ov,lv,de1
    tk.Button(cf, text="Go", command=anos3).grid(row=7, column=2)


# login setup *_*
logged_in_user = None
# Function to handle login
def login():
    global logged_in_user
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        logged_in_user = username
        messagebox.showinfo("Login Successful", "Welcome " + username)
        open_main_menu(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Function to handle sign up
def signup():
    username = new_username_entry.get()
    password = new_password_entry.get()
    mobile_no = mobile_no_entry.get()
    age = age_entry.get()
    if username and password:
        if username in users:
            messagebox.showerror("Sign Up Failed", "Username already exists")
        else:
            users[username] = password
            messagebox.showinfo("Sign Up Successful", "Account created successfully")
            sign.withdraw()
            root.deiconify()
    else:
        messagebox.showerror("Sign Up Failed", "Please enter both username and password")
        
def anos1():
    week_.deiconify()
    day.withdraw()

def open_youtube():
    url = "https://youtu.be/imnbWGCmDTs"
    webbrowser.open(url)
    
root=tk.Tk()
root.title("FITNESS CHALLENGES APP")
root.geometry("1080x1080")
root.maxsize(1080,1080)

sign = tk.Toplevel(root)
sign.title("SIGN UP")
sign.geometry("1080x1080")
sign.withdraw()

rank = tk.Toplevel(root)
rank.title("rank")
rank.geometry("1080x1080")
rank.withdraw()
tk.Button(rank, text="back", highlightbackground="grey", command=anos1999).pack(side="top")
rank_treeview = ttk.Treeview(rank, columns=("Rank", "Username", "Points"), show="headings")
# Add column headings
rank_treeview.heading("Rank", text="Rank")
rank_treeview.heading("Username", text="Username")
rank_treeview.heading("Points", text="Points")
# Set column widths
rank_treeview.column("Rank", width=50)
rank_treeview.column("Username", width=150)
rank_treeview.column("Points", width=100)
# Place the Treeview widget on the rank window
rank_treeview.pack(fill="both", expand=True)
# Create a button to refresh the rank table
refresh_button = tk.Button(rank, text="Refresh Rank", command=update_rank_table)
refresh_button.pack()
# Call the function to initially populate the rank table
update_rank_table()

main_menu = tk.Toplevel()
main_menu.title("FITNESS CHALLENGES APP")
main_menu.geometry("1080x1080")
main_menu.withdraw()

week_ = tk.Toplevel()
week_.title("FITNESS CHALLENGES APP")
week_.geometry("1080x1080")
week_.withdraw()

p = tk.Tk()
p.title("Music Player")
p.geometry("310x325")
p.withdraw()

day = tk.Toplevel()
day.title("Select a Day")
day.geometry("1080x1080")
day.withdraw()

exercises_window = tk.Toplevel()
exercises_window.title("Day")
exercises_window.geometry("1080x1080")
exercises_window.withdraw()

f1 = tk.Frame(root, bg="white", height=50)
f1.pack(side="top", fill="x")

l1 = tk.Label(f1, text="WELCOME TO YODHA", bg="white", fg="black")
l1.pack(side="top")

selected_difficulty = tk.StringVar()

f2 = tk.Frame(root, bg="grey", width=540, height=980)
f2.pack(side="left", fill="x")

users = {"user1": "password1", "user2": "password2","0":"0","":""}
    
# sign up frame

signup_container = tk.Frame(sign, bd=2, relief=tk.RAISED)
signup_container.pack(padx=20, pady=150)

signup_frame = tk.Frame(signup_container)
signup_frame.pack(padx=20, pady=20)

new_username_label = tk.Label(signup_frame, text="New Username:")
new_username_label.grid(row=0, column=0)
new_username_entry = tk.Entry(signup_frame)
new_username_entry.grid(row=0, column=1)

new_password_label = tk.Label(signup_frame, text="New Password:")
new_password_label.grid(row=1, column=0)
new_password_entry = tk.Entry(signup_frame, show="*")
new_password_entry.grid(row=1, column=1)

mobile_no_label = tk.Label(signup_frame, text="Mobile Number:")
mobile_no_label.grid(row=2, column=0)
mobile_no_entry = tk.Entry(signup_frame)
mobile_no_entry.grid(row=2, column=1)

age_label = tk.Label(signup_frame, text="Age:")
age_label.grid(row=3, column=0)
age_entry = tk.Entry(signup_frame)
age_entry.grid(row=3, column=1)

signup_button = tk.Button(signup_frame, text="Sign Up", command=signup)
signup_button.grid(row=4, columnspan=2)        

tk.Button(signup_frame, text="Back",relief="sunken", command=show_window1,).grid(row=6, columnspan=2)
        
# login frame

f3 = tk.Frame(root, width=750, height=980)
f3.pack(side="top", fill="x")

login_frame = tk.Frame(f3)
login_frame.pack(side="top",padx=50, pady=50)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

button1 = tk.Button(login_frame, text="New Here? Create an Account.", command=show_window2,)
button1.grid(row=4, columnspan=2)



# tk.Button(f1,text="Hi", command=login, highlightbackground="white", borderwidth=0,bg="white", highlightthickness=0, fg="black").pack(side="left")

root.mainloop()
