def buchstabe_ändern(string, buchstabe):
    
    string_lower = string.lower()
    
    for v in "aeiou":                   
        
        new_sentence = []
        
        for char in string_lower:
            
            if char == buchstabe:
                new_sentence.append(v)
                
            else:
                
                new_sentence.append(char)
        print("".join(new_sentence))
        
buchstabe_ändern(string = "banana", buchstabe = "a")
