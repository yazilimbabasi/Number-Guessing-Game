import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("Number Guessing Game")
window.configure(bg="dark red")

lb = Listbox(window, bg="black", fg="blue")
lb.insert(1, "1-10")
lb.insert(2, "1-100")
lb.insert(3, "1-1000")
lb.insert(4, "1-10000")
lb.insert(5, "100-150")
lb.insert(6, "50-150")
lb.insert(7, "10-50")
lb.insert(8, "1-100000000")
lb.place(x=150, y=10)

random_number = 0
attempts = 0
used_attempts = 0
won = False

def start_game():
    global random_number, attempts, used_attempts, won
    won = False
    used_attempts = 0
    selected_indices = lb.curselection()
    if selected_indices:
        selected_index = selected_indices[0]  # only get the first selection
        selected_value = str(lb.get(selected_index))
        num_range = selected_value.split("-")
        max_num = int(num_range[1])
        min_num = int(num_range[0])
        random_number = random.randint(min_num, max_num)
        print(random_number)

        if min_num == 1 and max_num == 10:
            attempts = 5
        elif min_num == 1 and max_num == 100:
            attempts = 15
        elif min_num == 1 and max_num == 1000:
            attempts = 100
        elif min_num == 1 and max_num == 10000:
            attempts = 15
        elif min_num == 100 and max_num == 150:
            attempts = 10
        elif min_num == 50 and max_num == 150:
            attempts = 20
        elif min_num == 10 and max_num == 50:
            attempts = 18
        elif min_num == 1 and max_num == 100000000:
            attempts = 10000
    else:
        messagebox.showerror("Warning", "Please select the range of numbers \nyou want to guess.")

def guess_button():
    global random_number, attempts, used_attempts, won
    input_number = int(entry.get())
    if not won:
        if random_number == input_number:
            messagebox.showinfo("Congratulations", "Congratulations! You guessed the number correctly.\nPlease start a new game.")
            used_attempts = attempts
            won = True
        else:
            used_attempts += 1
            if used_attempts <= attempts:
                if used_attempts == attempts:
                    messagebox.showinfo("Wrong", "You guessed the number wrong. You ran out of attempts.\nPlease start a new game.")
                else:
                    messagebox.showinfo("Wrong!", "You guessed the number wrong.\nTry again.")
            else:
                messagebox.showinfo("Warning", "You ran out of attempts. Please start a new game.")
    else:
        messagebox.showinfo("!!!", "You already won. Please start a new game.")

entry = Entry(window, bg="black", fg="orange", width=10, insertbackground="blue")
entry.place(x=120, y=240)

bu1 = Button(text="Guess", fg="green", bg="blue", command=guess_button, width=7)
bu1.place(x=120, y=265)

bu2 = Button(text="Start Game", fg="green", bg="blue", command=start_game)
bu2.place(x=25, y=40)

window.mainloop()

