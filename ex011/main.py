largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
metrosQuadrados = largura*altura
print("Sua parede tem a dimensão de {}x{} e a sua área é de {}m²".format(largura, altura, metrosQuadrados))
print("Para pintar essa parede, você precisará de {} litros de tinta".format(metrosQuadrados/2))