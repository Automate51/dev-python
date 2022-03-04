def glouton(R=15, S = [5, 14, 2, 4, 10 , 14, 5, 6, 9, 8, 5, 12, 14, 15, 13, 14]):
    di = 0
    d = S[di]
    nb_stations = len(S) - 1
    while di != nb_stations:

        if R < d:
            print("Vous tombez en panne !!!")
            
            break
        else:
            while  d <= R:
                 di += 1
                 d += S[di]
                 arret = di-1
        
            
        print (arret)
        d = S[di]
    print ("Arrêt final: arrêt numéro ",di)

    
    
    
glouton()
    
