def vokon_zählen(x):
    x_lower = x.lower()
    x_lower_list = list(x_lower)
    vokalen = "aeiou"
    
    v = [] # hier speicher wie die Vokale
    k = [] # hier speicher wir alle Buchstaben
    
    for b in x_lower_list:
        if b.isalpha():
            k.append(b)
        if b in vokalen:
            v.append(b)
    return f"Im string {x} gibt es {len(v)} Vokalen und {len(k)-len(v)} Konsonanten"

print(vokon_zählen("Berlin"))
        

