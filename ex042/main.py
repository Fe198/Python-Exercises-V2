print("-=" * 10)
print("Analisador de triângulos")
print("-=" * 10)
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
try1 = bool((b-c)<a<b+c)
try2 = bool((a-c)<b<a+c)
try3 = bool((a-b)<c<a+b)
if try3 == True and try2 == True and try1 == True:
    if a == b and a == c:
        print("Os segmentos acima podem formar um triângulo equilátero")
    elif a != b and a == c:
        print("Os segmentos acima podem formar um triângulo isóceles")
    elif a == b and a != c:
        print("Os segmentos acima podem formar um triângulo isóceles")
    elif a != b and a != c and b != c:
        print("Os segmentos acima podem formar um triãngulo escaleno")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")