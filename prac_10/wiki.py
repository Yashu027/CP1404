import wikipedia

title = input("A page title or search phrase: ")
while title != '':
    try:
        user_input = wikipedia.page(title, auto_suggest=False)
        print(user_input.summary)
        title = input("A page title or search phrase: ")
    except wikipedia.exceptions.DisambiguationError as disambiguation_error:
        print(disambiguation_error)
        title = input("A page title or search phrase: ")
    except wikipedia.exceptions.PageError as page_error:
        print(page_error)
        title = input("A page title or search phrase: ")


