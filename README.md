# mastodon_content_moderation
Yiwen Xu/CS 5001/Spring 2023/
Final Project

**Introduction**

This program is the final project of CS 5001. It is designed to fetch public statuses from Mastodon timeline through Mastodon API and search for potentially sensitive content. 

To be more specific, it first prompts the user for the number of statuses to fetch and the file path for the keywords to search for. It then retrieves the specified number of public statuses, searches them for the specified keywords, and returns a list of dictionaries, where each dictionary represents a potentially sensitive status, along with its timestamp and user ID. The program also prints out the content, timestamp, ID, and which sensitive keywords are contained in the status. The program handles errors such as invalid user input and file paths, and ensures that no duplicate sensitive statuses are returned.


**Key Aspects of the Project**
- Use of external libraries: The program uses the Mastodon.py library, the Mastodon API library uses object-oriented programming principles, such as encapsulation and inheritance, to provide a cleaner and more organized way of interacting with the Mastodon API. This highlights the importance of leveraging external libraries to save time and effort in developing complex projects.
- Use of dictionaries: Dictionaries are used in the program to store and manipulate data, such as statuses and sensitive keywords. This highlights the importance of data structures, particularly dictionaries, in managing complex data.
- Use of functions: The program has several functions, each of which performs a specific task. This shows the importance of breaking down complex programs into smaller parts that are easier to manage and test.
- Handling errors and exceptions: The program includes several error-handling mechanisms, including try-except blocks and input validation, to handle exceptions that might arise during the execution of the program. This demonstrates the importance of anticipating and handling errors in software development.

