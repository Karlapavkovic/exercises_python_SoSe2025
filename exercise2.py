def teilbar(x,y):
    if y == 0:
        print("Es ist nicht möglich durch Null zu teilen")
    elif x==y:
        print("x und y sind gleich")
    
    else: 
        if x%y == 0:
            print (x," ist durch ", y, "teilbar")
        else:
            print (x, " ist nicht durch", y, "teilbar")
    
teilbar(10,2)           
              
git add "exercise2.py"

               
