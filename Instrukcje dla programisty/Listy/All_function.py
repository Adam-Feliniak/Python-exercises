languages = ["polski", "angielski", "niemiecki", "ukraiński"]
print(languages[0].title())
print(f"Moim ojczystym jęzeykiem jest: {languages[0]}")
languages.append("francuski")
print(languages)
languages.insert(2, 'hiszpański')
print(languages)
del languages[4]
print(languages)
popped_language = languages.pop()
print(languages)
print(popped_language)
languages.remove("niemiecki")
print(languages)
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
sorted(languages,reverse=True)
print(languages)
