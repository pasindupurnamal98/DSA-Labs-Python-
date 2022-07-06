#string matching
T="SusiraChamathJayasekaraJaya"
p="Jaya"

def Naive_String_Matcher(T,P):
    n=len(T)
    m=len(P)
    for S in range(0,n-m+1):
        if P[0:m] == T[S:(S+m)]:
            print("Pattern Occurs with shift",S)
    
Naive_String_Matcher(T,p)      
