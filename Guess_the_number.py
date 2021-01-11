from tkinter import *
import random

window = Tk()  # initiate window
window.geometry('500x500')
window.title('Guess the number')
window.resizable(False, False)  # making sure they can't resize
number = random.randint(1, 100)
guess = ''
counter = 0
num_input = Entry(window, width=50)
num_input.pack()


def click():
    global counter
    label = Label(window, text='Your guess was: ' + num_input.get(),
                  bd=10, bg='lightblue3', fg='black').place(x=20, y=50)

    guess = int(num_input.get())

    print(guess)
    if number == guess:
        label2 = Label(window, text='You got it!', bd=5, bg='lightblue3', fg='black').place(
            x=20, y=125)

    elif number < guess:
        label2 = Label(window, text='Aim lower!', bd=5, bg='lightblue3', fg='black').place(
            x=20, y=125)
        counter += 1


    elif number > guess:
        label2 = Label(window, text='Aim higher!', bd=5, bg='lightblue3', fg='black').place(
            x=20, y=125)
        counter += 1

    if 6 > counter >= 3:
        if (number % 2) == 0:
            label4 = Label(window, text='The number is even', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=185)
        else:
            label4 = Label(window, text='The number is odd', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=185)

    elif 9 > counter >= 6:
        if (number % 2) == 0:
            label4 = Label(window, text='The number is even', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=185)
        else:
            label4 = Label(window, text='The number is odd', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=185)
        if number > 50:
            label5 = Label(window, text='The number is bigger than 50', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=215)
        else:
            label5 = Label(window, text='The number is smaller than 50', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=215)

    elif counter >= 9:
        if (number % 2) == 0:
            label4 = Label(window, text='The number is even', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=185)
        else:
            label4 = Label(window, text='The number is odd', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=185)
        if number > 50:
            label5 = Label(window, text='The number is bigger than 50', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=215)
        else:
            label5 = Label(window, text='The number is smaller than 50', bd=5, bg='lightblue3',
                           fg='black').place(x=20, y=215)
        label6 = Label(window, text='The number is between ' + str(number - 2) + ' and '
                                    + str(number + 2)
                       , bd=5, bg='' 'lightblue3', fg='black').place(x=20, y=245)

    label3 = Label(window, text=str(counter) + ' tries', bd=5, bg='lightblue3', fg='black').place(
        x=20, y=155)


print(number)
button1 = Button(window, text='Take a guess, the number is between 1 and 100', command=click)
button1.pack()

window.mainloop()
