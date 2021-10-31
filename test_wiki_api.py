import wikipediaapi
import wikipedia
wiki = wikipediaapi.Wikipedia('en')

paje = wiki.page("github")
print(paje.exists())