def zamena(text, samohlaska):
    for i in range(len(text)):
        if text[i] in samohlasky:
            text = text[:i] + samohlaska + text[i+1:]
    return text

samohlasky='aáeéiíoóôuúyý'
riekanka = 'sedí mucha na stene a spí'
print(riekanka)
print(zamena(riekanka, 'o'))
