"""
Erklärung wie die Funktion funktioniert

"""



def cagr_berechnung(AK, EK, t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    cagr = (EK/AK_abs)**(1/t_abs)-1
    return cagr
    
    
    
print(cagr_berechnung(AK=100, 
                      EK=700, 
                      t=30))    

    