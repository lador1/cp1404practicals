# importing the module
import wikipedia
from wikipedia import DisambiguationError, PageError

search_input = input("Enter what to search for : ")
while search_input != "":
    try:
        page = wikipedia.page(search_input, auto_suggest=False)
        print("Title:", page.title)
        print(wikipedia.summary(page))
        search_input = input("Enter what to search for: ")
    except DisambiguationError:
        print("Search for something more specific idiot")
    except PageError:
        print("Does not match any pages")

print("Thanks cya")


