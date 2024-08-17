def magic_square():
    magicSq = []
    n = int(input("Enter matrix size: "))  # Convert input to integer
    for i in range(n):
        l = []  # Create a new list for each row
        for j in range(n):
            l.append(0)  # Append 0 to the row
        magicSq.append(l)  # Append the row to the matrix


    p=n//2
    q=n-1
    
    num=n*n
    count=1
    
    while(count<=num):
        if p==-1 and q==n:
            p=0
            q=n-2
        else :
            if q==n:
                q=0
            if(p < 0):
                p=n-1
        if magicSq[p][q] != 0 :
            p=p+1
            q=q-2
            continue
        else:
            magicSq[p][q]=count
            count += 1
            
        p -= 1
        q += 1
    # Print the matrix
    for i in range(n):
        for j in range(n):
            print(magicSq[i][j], end=" ")  # Print elements in the same row
        print()  # New line after each row
        
        
    

magic_square()
