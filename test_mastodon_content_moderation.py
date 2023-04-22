"""
Test Mastodon Project
===========================
Course:   CS 5001
Semester: Spring 2023
Student:  Yiwen Xu

Run tests on mastodon_content_moderation.py
"""

from mastodon_content_moderation import load_keywords, get_num_statuses, \
    fetch_public_statuses, search_statuses_for_keywords, \
    save_sensitive_statuses_to_file


def test_load_keywords_1():
    """
    Test to see if the function loads keywords list from a given file
    and returns a list as expected
    """
    actual = load_keywords("/Users/katexu/Desktop/test_keywords.txt")
    expected = ["aaa", "bbb", "ccc", "ddd"]
    if actual != expected:
        return True


def test_load_keywords_2():
    # Test handling of non-existent file
    actual = load_keywords("nonexistent.txt")
    expected = []
    if actual != expected:
        return True


def test_get_num_statuses():
    """Test to see if the function can catch and handle user input errors"""
    # Test with client input "100"
    actual = get_num_statuses()
    expected = 100
    if actual != expected:
        return True


def test_get_num_statuses_2():
    # Test handling of non-integer input "3.4"
    actual = get_num_statuses()
    expected = "Error: Please enter an integer."
    if actual != expected:
        return True


def test_get_num_statuses_3():
    # Test handling of negative input "-12"
    actual = get_num_statuses()
    expected = "Error: Please enter a positive integer."
    if actual != expected:
        return True


def test_get_num_statuses_4():
    # Test handling of letter "abc"
    actual = get_num_statuses()
    expected = "Error: Please enter an integer."
    if actual != expected:
        return True


def test_fetch_public_statuses():
    """Test to see if the function fetch the right number of public statuses"""
    actual = len(fetch_public_statuses(60))
    expected = int(60)
    if actual != expected:
        return True


def test_search_statuses_for_keywords():
    """Test searching for sensitive keywords in public statuses"""
    public_statuses = [
        {"content": "This is a public status containing the word abc"},
        {"content": "This is another public status"},
        {"content": "This is a public status containing the word def"},
    ]
    keywords = ["abc", "def"]
    sensitive = search_statuses_for_keywords(public_statuses, keywords)
    actual = len(sensitive)
    expected = 2
    if actual != expected:
        return True


def test_save_sensitive_statuses_to_file():
    """
    Test to see if the saved file is the same as
    the correct version
    """
    sensitive_statuses = [
        {"content": "This is a test statuses containing a sensitive keyword aaa."},
        {"content": "This is another test statuses containing a different sensitive keyword bbb."},
        {"content": "This is another test statuses containing a different sensitive keyword ccc."}
    ]
    save_sensitive_statuses_to_file(
        sensitive_statuses,
        "sensitive_statuses_3.txt")
    # correct version in test_correct.txt


def compare_files(filename_1, filename_2):
    """
    Compare two files and return True if their contents are the same,
    False otherwise.
    """
    with open(filename_1) as file1, open(filename_2) as file2:
        contents_one = file1.read()
        contents_two = file2.read()
        if contents_one != contents_two:
            return True


def main():
    """
    Check to see if all the tests are passed
    And if not how many tests were failed
    """
    counter = 0
    if test_load_keywords_1():
        counter += 1
    if test_load_keywords_2():
        counter += 1
    if test_get_num_statuses():
        counter += 1
    if test_fetch_public_statuses():
        counter += 1
    if test_search_statuses_for_keywords():
        counter += 1
    test_save_sensitive_statuses_to_file()
    if compare_files("sensitive_statuses_3.txt",
                     "test_correct.txt"):
        counter += 1
        print(f"Failed: {counter} tests.")
    else:
        print("All passed!")


if __name__ == '__main__':
    main()
