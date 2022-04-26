cateto1 = float(input("Comprimento do cateto oposto: "))
cateto2 = float(input("Comprimento do cateto adjacente: "))
hipotenusa = (cateto1**2 + cateto2**2) **(1/2)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))