def read_text():
    quotes = open("/Users/Judy/Documents/Coding/Tutorials/Udacity/Programming Foundations w Python/Lesson2/movie_quotes.txt")
    contents = quotes.read()
    print (contents)
    quotes.close()

read_text()
