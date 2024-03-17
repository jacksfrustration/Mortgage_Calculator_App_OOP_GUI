from tkinter import *
from tkinter import messagebox

class Mortgage_Calculator:
    def __init__(self,window):
        self.window=window
        self.window.title("Mortgage Calculator")
        self.window.config(padx=50, pady=50)
        self.canvas=Canvas(self.window,width=600,height=315)
        self.canvas.grid(row=0,column=0,columnspan=3)
        self.create_gui()


    def create_gui(self):
        self.bg_img=PhotoImage(file="Mortgage_1488379562.png")
        bg = self.canvas.create_image(300, 157, image=self.bg_img)
        self.calc_img=PhotoImage(file="calculate.png")
        Label(text="Loan Amount:").grid(column=0, row=1)

        self.loan_ent = Entry()
        self.loan_ent.grid(column=2, row=1)
        Label(text="Years to pay back:").grid(column=0, row=2)

        self.term_ent = Entry()
        self.term_ent.grid(column=2, row=2)
        Label(text="Payment Window:").grid(column=0, row=4)

        Label(text="Interest percentage:").grid(column=0, row=4)

        self.interest_ent = Entry()
        self.interest_ent.grid(column=2, row=4)
        Label(text="Deposit Percentage").grid(row=5, column=0)

        self.dep_ent = Entry()
        self.dep_ent.grid(row=5, column=2)

        Button(image=self.calc_img, text="Calculate", command=self.calc_mort, borderwidth=0, compound="bottom").grid(row=6, column=1)



    def calc_mort(self):
        '''gets years to pay back, interest and deposit percentage
        and total loan amount and outputs monthly payments
        this process is automated so if there are non-digits or empty
        entries the program will not crash and will output appropriate error message'''
        try:
            loan=round(float(self.loan_ent.get()),2)
        except ValueError:
            messagebox.showerror(title="Oops",message="Loan Amount not applicable")
        else:
            try:
                term=int(self.term_ent.get())
            except ValueError:
                messagebox.showerror(title="Oops",message="Time to pay back by not applicable")
            else:
                num_payments=term*12
                try:
                    interest=(float(self.interest_ent.get())/100)/12
                except ValueError:
                    messagebox.showerror(title="Oops",message="Interest rate not applicable")
                else:
                    try:
                        deposit_percentage=float(self.dep_ent.get())/100
                        deposit_amount=deposit_percentage*loan
                    except ValueError:
                        messagebox.showerror(title="Oops",message="Deposit percentage not applicable")
                    else:
                        loan_remainder=loan-deposit_amount
                        monthly_payments=abs(round((loan_remainder*interest)/(1-((1+interest)**(-num_payments))),2))
                        res=('{:,}'.format(monthly_payments))
                        loan_res=('{:,}'.format(loan))

                        messagebox.showinfo(title="Mortgage Payment",message=f"You have borrowed £{loan_res}0 and you have {term} years to pay it back!\n"
                                                                         f"Initial deposit percentage of {deposit_percentage*100}0%\n"
                        f"You have to pay £{res} a month.\n")
def main():
    window=Tk()
    mort=Mortgage_Calculator(window=window)
    window.mainloop()
if __name__=="__main__":
    main()