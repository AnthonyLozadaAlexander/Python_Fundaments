print("EjercicioPalindromos")

String = input("Introduce un String: \n")

String = String.lower()

listString = list(String)

listString_Reverse = list(String)
listString_Reverse.reverse()

while "" in listString:
  listString.remove(" ")
  
while "" in listString_Reverse:
  listString_Reverse.remove(" ")
  
  
if listString == listString_Reverse:
    print("El String es un palindromo")
else:
  print("El String no es un palindromo")
