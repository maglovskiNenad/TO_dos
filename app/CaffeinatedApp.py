from customtkinter import *
import json
from app.CustomButton import Button
from datetime import datetime

class CaffeinatedMainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("CaffeinatedApp")
        self.geometry("550x500")
        self.columnconfigure(0, minsize=20, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.left_frame = None
        self.main_frame = None
        self.right_frame = None
        self.refresh_the_page()

        #Left side of the screen field
        self.left_frame = CTkFrame(self, height=200, width=250, corner_radius=10)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        #Descriptive label
        label = CTkLabel(self.left_frame, text="To Do List", font=("bahnschrift semilight", 18))
        label.grid(row=1, column=0, padx=10, pady=10)

        #Adding todos btn
        statistic = Button(self.left_frame, text="Add", command=self.add_todos, corner_radius=10)
        statistic.grid(row=2, column=0, padx=10, pady=10)

        #Entry for adding todos
        self.todo = CTkEntry(self.left_frame, placeholder_text="New Todos")
        self.todo.grid(row=3, column=0, padx=10, pady=10)

        goods = Button(self.left_frame, text="Remove", command=self.remove_todo, corner_radius=10)
        goods.grid(row=4, column=0, padx=10, pady=10)

        self.id = CTkEntry(self.left_frame, placeholder_text="Please enter Id:")
        self.id.grid(row=5, column=0, padx=10, pady=10)

    def refresh_the_page(self):
        # Main side of the screen field
        self.main_frame = CTkFrame(self, height=200, width=700, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        #Opening all todos that are in the json list
        with open("todos.json") as file:
            data = json.load(file)
            for text in data:
                todo_label = CTkLabel(self.main_frame,text=f"Id od todo:{str(text["id"])}.\n "
                                                           f"Description of Todo:{text["description"]}\n"
                                                           f"Time: {text["createdAd"]}")
                todo_label.grid(row=text["id"], column=0, padx=10, pady=10)


    def add_todos(self):
        """Adding new in the list"""
        entered_todo = self.todo.get()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("todos.json") as file:
            data = json.load(file)

        one_todo = {
            'description': entered_todo,
            'id': len(data) + 1,
            'status': 'todo',
            'createdAd': current_time,
            'updatedA': current_time
        }

        data.append(one_todo)

        with open("todos.json","w") as file:
            json.dump(data,file,indent=4)

        self.todo.delete(0, END)
        self.refresh_the_page()

    def remove_todo(self):
        entered_id = self.id.get()

        with open("todos.json") as file:
            data = json.load(file)

        new_todos = [todo for todo in data if todo["id"] != int(entered_id)]
        print(new_todos)

        with open("todos.json", "w") as file:
            json.dump(new_todos,file,indent=4)

        self.id.delete(0,END)
        self.refresh_the_page()



if __name__ == "__main__":#
    app = CaffeinatedMainWindow()
    app.mainloop()
