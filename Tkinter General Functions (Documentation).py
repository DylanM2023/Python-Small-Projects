import tkinter as tk

window = tk.Tk()

window.geometry("1920x1080") # Changes Window Size

window["bg"] = "blue" # Changes Background Colour of the window to blue

def buttonpress(): 
    contents = textbox.get() #gets content from text box (User Data)
    print(contents)
    textbox.delete("0" , "end") #Deletes all the text in the text box
    
    if contents == "Dylan": # If data in the text box == 'Dylan'
        print("Correct User")
    else:
        print("Not Valid User")
    logged_in(contents)

def logged_in(contents):
    if contents == "Dylan":
        new_message = tk.Label(text="You have logged in") # Creates new widget to show that the user has successfully logged in
        textbox.destroy()
        label.destroy() # .destroy() removes a widget to create a new window
        button.destroy()
        new_message.pack() # adds the new widget


label = tk.Label(
    text="Please Log In",
    fg="red",               
    bg="black",             # label which asks user to login 
    width=10,   
    height=5
)

label.pack()    # adds the label

textbox= tk.Entry(fg="black", bg="white", width=50) #Creates the text box for user to enter login info
textbox.pack()

button = tk.Button(
    text="Submit",
    width=10,               # Size / colour etc for 'submit' button
    height=5,
    bg="black",
    fg="red",
    command=buttonpress # calls the 'buttonpress' funtion on the click of the button
)

button.pack()   #adds the button

window.mainloop()

