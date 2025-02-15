import tkinter as tk
from tkinter import messagebox

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}"

class BankingSystem:
    def __init__(self, root):
        self.accounts = {}

        self.root = root
        self.root.title("Banking System")

        # Set background color
        self.root.configure(bg="#f0f0f0")

        # Define font styles here
        font = ('Arial', 12)
        button_font = ('Arial', 12, 'bold')

        # Widgets for account creation
        self.create_account_frame = tk.Frame(root, bg="#f0f0f0")
        self.create_account_frame.pack(pady=15)

        self.acc_num_label = tk.Label(self.create_account_frame, text="Account Number:", font=font, bg="#f0f0f0")
        self.acc_num_label.grid(row=0, column=0, pady=5)
        self.acc_num_entry = tk.Entry(self.create_account_frame, font=font)
        self.acc_num_entry.grid(row=0, column=1, pady=5)

        self.acc_holder_label = tk.Label(self.create_account_frame, text="Account Holder:", font=font, bg="#f0f0f0")
        self.acc_holder_label.grid(row=1, column=0, pady=5)
        self.acc_holder_entry = tk.Entry(self.create_account_frame, font=font)
        self.acc_holder_entry.grid(row=1, column=1, pady=5)

        self.initial_balance_label = tk.Label(self.create_account_frame, text="Initial Balance:", font=font, bg="#f0f0f0")
        self.initial_balance_label.grid(row=2, column=0, pady=5)
        self.initial_balance_entry = tk.Entry(self.create_account_frame, font=font)
        self.initial_balance_entry.grid(row=2, column=1, pady=5)

        self.create_acc_button = tk.Button(self.create_account_frame, text="Create Account", command=self.create_account, font=button_font, bg="#4CAF50", fg="white", width=20, height=2)
        self.create_acc_button.grid(row=3, columnspan=2, pady=10)

        # Widgets for transactions
        self.transaction_frame = tk.Frame(root, bg="#f0f0f0")
        self.transaction_frame.pack(pady=15)

        self.trans_acc_num_label = tk.Label(self.transaction_frame, text="Account Number:", font=font, bg="#f0f0f0")
        self.trans_acc_num_label.grid(row=0, column=0, pady=5)
        self.trans_acc_num_entry = tk.Entry(self.transaction_frame, font=font)
        self.trans_acc_num_entry.grid(row=0, column=1, pady=5)

        self.amount_label = tk.Label(self.transaction_frame, text="Amount:", font=font, bg="#f0f0f0")
        self.amount_label.grid(row=1, column=0, pady=5)
        self.amount_entry = tk.Entry(self.transaction_frame, font=font)
        self.amount_entry.grid(row=1, column=1, pady=5)

        self.deposit_button = tk.Button(self.transaction_frame, text="Deposit", command=self.deposit, font=button_font, bg="#2196F3", fg="white", width=15, height=2)
        self.deposit_button.grid(row=2, column=0, pady=10)

        self.withdraw_button = tk.Button(self.transaction_frame, text="Withdraw", command=self.withdraw, font=button_font, bg="#FF5722", fg="white", width=15, height=2)
        self.withdraw_button.grid(row=2, column=1, pady=10)

        # Widgets for account information
        self.info_frame = tk.Frame(root, bg="#f0f0f0")
        self.info_frame.pack(pady=15)

        self.info_acc_num_label = tk.Label(self.info_frame, text="Account Number:", font=font, bg="#f0f0f0")
        self.info_acc_num_label.grid(row=0, column=0, pady=5)
        self.info_acc_num_entry = tk.Entry(self.info_frame, font=font)
        self.info_acc_num_entry.grid(row=0, column=1, pady=5)

        self.info_button = tk.Button(self.info_frame, text="Display Info", command=self.display_info, font=button_font, bg="#9C27B0", fg="white", width=20, height=2)
        self.info_button.grid(row=1, columnspan=2, pady=10)

    def create_account(self):
        acc_num = self.acc_num_entry.get()
        acc_holder = self.acc_holder_entry.get()
        initial_balance = float(self.initial_balance_entry.get())

        if acc_num and acc_holder:
            self.accounts[acc_num] = Account(acc_num, acc_holder, initial_balance)
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showwarning("Error", "Account number and holder name cannot be empty!")

    def deposit(self):
        acc_num = self.trans_acc_num_entry.get()
        amount = float(self.amount_entry.get())

        if acc_num in self.accounts:
            try:
                self.accounts[acc_num].deposit(amount)
                messagebox.showinfo("Success", f"Deposited {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            except ValueError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Account not found!")

    def withdraw(self):
        acc_num = self.trans_acc_num_entry.get()
        amount = float(self.amount_entry.get())

        if acc_num in self.accounts:
            try:
                self.accounts[acc_num].withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            except InsufficientFundsError as e:
                messagebox.showwarning("Error", str(e))
            except ValueError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Account not found!")

    def display_info(self):
        acc_num = self.info_acc_num_entry.get()

        if acc_num in self.accounts:
            account_info = self.accounts[acc_num].display_account_info()
            messagebox.showinfo("Account Info", account_info)
        else:
            messagebox.showwarning("Error", "Account not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()
