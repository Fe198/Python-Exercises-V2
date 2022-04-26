from math import sin, cos, tan, radians
angle = float(input("Digite um ângulo: "))
radianos = radians(angle)
print("Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(sin(radianos), cos(radianos), tan(radianos)))