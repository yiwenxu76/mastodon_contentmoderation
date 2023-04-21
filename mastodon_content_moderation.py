"""
Final Project: Mastodon Content Moderation
===========================
Student:  Yiwen Xu
Semester: Spring 2023
Class: CS 5001

Fetch public statuses from Mastodon and search for sensitive content.
The program handles errors such as invalid user input and file paths,
and ensures that no duplicate sensitive statuses are returned.
"""

from mastodon import Mastodon

"""Set up Mastodon API credentials"""
Mastodon.create_app(
    "CS5001",
    api_base_url="https://mastodon.social",
    to_file="crJC4Kg_pinpGjG2OSmxl_Q6RbD3M8FsmwqUXM5XEec"
)
mastodon = Mastodon(
    client_id="crJC4Kg_pinpGjG2OSmxl_Q6RbD3M8FsmwqUXM5XEec",)
mastodon.log_in(
    "xuyiwen76@126.com",
    "Fuzeren1!",
    to_file="crJC4Kg_pinpGjG2OSmxl_Q6RbD3M8FsmwqUXM5XEec"
)


# load sensitive keywords from files
def load_keywords(file_path):
    """
    Load keywords from a text file, separated by commas.

    Args:
        file_path (str): Absolute path to the file containing the keywords.

    Returns:
        list: A list of keywords.
    """
    keywords = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                keywords.extend(line.strip().split(","))
        return keywords
    except OSError:
        print(f"Error: could not load keywords from file {file_path}")
        return []


def get_num_statuses():
    """
    Prompts the user to input the number of public statuses to fetch.
    Returns an integer representing the number of statuses.
    """
    while True:
        try:
            num_statuses = int(
                input("Enter the number of public statuses to fetch: "))
            if num_statuses <= 0:
                print("Error: Please enter a positive integer.")
            else:
                return num_statuses
        except ValueError:
            print("Error: Please enter an integer.")


def fetch_public_statuses(num_statuses: int):
    """
    Fetches the public timeline using Mastodon API,
    not including replies

    Args:
        num_statuses (int): The number of public statuses to fetch.

    Returns:
        A list of status dicts.
    """
    public_statuses = []
    max_id = None
    while len(public_statuses) < num_statuses:
        statuses = mastodon.timeline_public(max_id=max_id)
        if not statuses:
            # no more statuses to fetch
            break
        public_statuses.extend(statuses)
        # retrieves the id of the last status in the public_timeline list
        # and assigns it to the max_id variable
        max_id = statuses[-1]["id"]
    return public_statuses


# search for sensitive keywords in statuses
def search_statuses_for_keywords(public_statuses, keywords):
    """
    Search a list of statuses for the given keywords.

    Args:
        public_statuses (list): A list of status dictionaries to search through.
        keywords (list): A list of keywords to search for.

    Returns:
        list: A list of dictionaries, where each dictionary represents a sensitive
        status and includes the following keys:
            - content (str): The content of the sensitive status.
            - timestamp (str): The timestamp of the sensitive status.
            - user_id (str): The ID of the user who posted the sensitive status.
    """
    # Initialize a list to hold statuses containing sensitive keywords
    sensitive_statuses = []
    # Loop through each status in the list of statuses
    for status in public_statuses:
        # convert the status text to lowercase for case-insensitive matching
        content = status["content"].lower()
        # Check if any of the sensitive keywords are found in the status
        for keyword in keywords:
            # add whitespace before and after the keyword,
            # so we can filter statuses containing the exact word
            if f" {keyword} " in content:
                sensitive_status = {
                    "content": status.get("content"),
                    "timestamp": status.get("created_at"),
                    "user_id": status.get("id"),
                    "keyword": keyword
                }
                # prevent duplicate sensitive statuses from being added to the sensitive_statuses list
                if sensitive_status not in sensitive_statuses:
                    # Only add status once per keyword
                    sensitive_statuses.append(sensitive_status)
    return sensitive_statuses


def print_sensitive_statuses(sensitive_statuses):
    """
    Prints out the content, timestamp, ID, and which sensitive keywords each status contains.

    Parameters:
    -----------
    sensitive_statuses : list of dictionaries
        A list of dictionaries representing each sensitive status.
    """
    if sensitive_statuses:
        print("Sensitive statuses found:")
        for status in sensitive_statuses:
            print(f"Content: {status['content']}")
            print(f"Timestamp: {status['timestamp']}")
            print(f"User ID: {status['user_id']}")
            print(f"Contains Keyword: {status['keyword']}")
            print("-" * 50)
    else:
        print("No sensitive statuses found.")


def save_sensitive_statuses_to_file(sensitive_statuses, filename):
    """
    Saves the given statuses to a file, with each status separated by a blank line.

    Args:
        sensitive_statuses (list): A list of statuses to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as file:
        for status in sensitive_statuses:
            file.write(status["content"] + "\n\n")


def main():
    """
    This is the main entry point for the program.
    """
    # keywords = load_keywords_files()
    keywords = load_keywords(
        "/Users/katexu/Downloads/sensitive_words_list.txt")
    # Fetch public statuses
    num_statuses = get_num_statuses()
    public_statuses = fetch_public_statuses(num_statuses)
    # search for sensitive keywords in public statuses
    sensitive_statuses = search_statuses_for_keywords(
        public_statuses, keywords)
    # print a list of dictionaries
    print_sensitive_statuses(sensitive_statuses)
    # Print number of sensitive statuses found
    print(f"{len(sensitive_statuses)} sensitive statuses found within {num_statuses} statuses.")
    # Save sensitive statuses into a file
    save_sensitive_statuses_to_file(sensitive_statuses, f"sensitive_statuses_{len(sensitive_statuses)}.txt")


if __name__ == "__main__":
    main()
