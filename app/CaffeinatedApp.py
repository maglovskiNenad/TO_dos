
from customtkinter import *
from pandas.io.sas.sas_constants import column_name_length_length


class CaffeinatedMainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.left_frame = None
        self.main_frame = None
        self.right_frame = None
        self.user_main_frame()

    def user_main_frame(self):
        self.title("CaffeinatedApp")
        self.geometry("980x700")
        self.columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.user_button_window()
        self.user_main_window()
        self.billing_window()


    def user_button_window(self):
        self.left_frame = CTkFrame(self,height=700, width=250,corner_radius=10)
        self.left_frame.grid(row=0, column=0,padx=10, pady=10, sticky="ns")

        label = CTkLabel(self.left_frame,text="Caffeinated",font=("bahnschrift semilight", 18))
        label.grid(row=0,column=0,padx=10,pady=10)

        statistic = CTkButton(self.left_frame,text="Statistic",corner_radius=10)
        statistic.grid(row=1, column=0,padx=10,pady=10)

        goods = CTkButton(self.left_frame,text="Goods",corner_radius=10)
        goods.grid(row=2,column=0)

        sales = CTkButton(self.left_frame,text="Sales",corner_radius=10)
        sales.grid(row=3,column=0,padx=10,pady=10)

        signup = CTkButton(self.left_frame,text="Login",corner_radius=10)
        signup.grid(row=6,column=0,padx=10,pady=10)

        toggle_theme = CTkButton(self.left_frame,text="Toggle me",corner_radius=10)
        toggle_theme.grid(row=7,column=0)

    def user_main_window(self):
        self.main_frame = CTkFrame(self,height=700,width=500,corner_radius=10)
        self.main_frame.grid(row=0,column=1,padx=10, pady=10,sticky="nsew")
        name = CTkLabel(self.main_frame, text="Caffeinated table", font=("bahnschrift semilight", 18))
        name.grid(row=0, column=0, padx=20, pady=20)

    def billing_window(self):
        self.right_frame = CTkFrame(self,height=700, width=250, corner_radius=10)
        self.right_frame.grid(row=0, column=2,padx=10, pady=10, sticky="nsew")

        name = CTkLabel(self.right_frame,text="Caffeinated billing proces",font=("bahnschrift semilight", 18))
        name.grid(row=0,column=0,padx=20,pady=20)




if __name__ == "__main__":#
    app = CaffeinatedMainWindow()
    app.mainloop()
