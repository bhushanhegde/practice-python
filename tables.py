for i in range (1,21):
    for j in range (1,11):
        print("%6d"%(i*j),end='')
        
        if (i*j)%1==0:
            print()
            if(i*j)%10==0:
                print(end='')
                
        
    print()    
       
