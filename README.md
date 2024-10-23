#   TheForce Password Tool

#   TheForce Password Tool is a comprehensive Python application designed for generating, mutating, filtering, and bruteforcing passwords through an intuitive graphical user interface (GUI). This tool serves as an educational resource to help users understand password security principles, the importance of strong passwords, and the methods employed in password cracking techniques.

#   With the increasing prevalence of cyber threats, understanding password security is crucial. TheForce Password Tool allows users to experiment with password generation and manipulation techniques, providing insights into how easily passwords can be compromised. It also emphasizes the need for robust password practices in securing personal and professional accounts.

#   Features
#   - Password Generation: Create passwords of varying lengths using a specified character set, including letters (uppercase and lowercase), numbers, and symbols. This feature allows users to generate strong passwords tailored to their security needs.
  
#   - Password Mutation: Modify existing passwords by applying various mutation rules. Users can change character cases, insert new characters, replace existing characters, or delete characters to create new variations of passwords.

#   - Password Filtering: Filter generated or mutated passwords based on user-defined regular expressions (regex). This feature helps users identify passwords that meet specific criteria, enhancing the ability to find secure passwords quickly.

#   - Bruteforce Login: Attempt to log in to a specified URL using a list of generated or mutated passwords. This feature demonstrates the effectiveness of brute-force attacks and highlights the importance of using strong, unique passwords.

Navigate to the Project Directory: Change into the project directory using:

cd TheForcePasswordTool

Install Required Packages: Ensure you have Python installed on your system (preferably version 3.6 or higher). Then, install the necessary packages using pip:

pip install -r requirements.txt

Note: If you encounter any issues with tkinter, ensure it is installed as part of your Python distribution. It usually comes pre-installed with standard Python installations.


Usage:

To run the application, execute the following command in your terminal:

python TheForce.py

GUI Interaction:

Upon launching the application, you will be greeted with the main interface, which presents various options for interacting with the tool. Below are detailed instructions for using each feature:


Generate Passwords:

Select option 1 from the menu.

Enter the minimum and maximum password lengths you wish to generate.

Specify the character set (e.g., "abc123!@#") from which the passwords will be created.
The tool will generate a list of passwords based on your input and display a success message.


Apply Mutations:

Select option 2 to modify existing passwords.
If you have generated passwords, enter mutation rules in the format (e.g., "upper 2", "insert 5 !").

Examples of Mutation Rules:
upper 2: Converts the character at index 2 to uppercase.

insert 5 !: Inserts the character ! at index 5.
replace 3 @: Replaces the character at index 3 with @.

delete 1: Deletes the character at index 1.
The tool will apply the mutations and display the modified passwords.


Apply Filters:

Select option 3 to filter passwords.

Enter regular expressions to filter the passwords (e.g., "[a-z]", "[0-9]").

The tool will display only the passwords that match the specified filters, allowing you to quickly identify secure options.


Bruteforce Password:

Select option 4 to attempt a login.
Enter the username, login URL, and social media name you want to test.
The tool will attempt to log in using the generated or mutated passwords, displaying success or failure messages for each attempt.
Important Note: TheForce Password Tool is intended for educational purposes only. Users are strongly encouraged to use this tool responsibly and ethically. Unauthorized access to computer systems or accounts is illegal and unethical. Always seek permission before attempting to test the security of any accounts or systems.

Contributions to the TheForce Password Tool are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.
