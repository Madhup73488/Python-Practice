messy_names = ["  john DOE ", "alice smith", "   ", "BOB  "]

def clean_names(names):
    cleaned = []
    for name in names:
        processed = name.strip().title()
        if processed: 
            cleaned.append(processed)
            
    return cleaned

print(clean_names(messy_names))
