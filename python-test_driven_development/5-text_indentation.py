#!/usr/bin/python3

def text_indentation(text):
    """Print text with two new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        """Raise an error if text is not a string"""
        raise TypeError("text must be a string")
    
    for char in ".?:":
        text = (char + "\n\n").join([line.strip() for line in text.split(char)])
    
    print(text)
