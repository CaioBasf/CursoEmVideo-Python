frase = 'Curso em Vídeo Python'
print(frase[3:15]) #Mostrar de 3 a 14
print(frase[:15]) #Mostra do começo até 14
print(frase[5:]) #Mostra do 5 até o final
print(frase[5:15:2]) #Mostra do 5 até o 14 e pula de 2 em 2
print(frase[::3]) #Mostra do começo ao fim e pula de 3 em 3

print('Oi')

print("""Python is a programming language that lets you work more quickly and integrate your systems more effectively.
You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs.""")

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O')) #Ele joga inicialmente a frase para letra maisuculas e logo apos conta quantas vezes tem a letra O

print(len(frase)) #Vai contar os espaços alocados na memoria
print(len(frase.strip())) #Retira os espaços nas contas deles

print(frase.replace('Python', 'Android')) #Não altera a lista original, apenas altera se colocado frase = frase.replace, ele muda apenas a propia instancia

print('Curso' in frase) #Se possui ou não
print(frase.find('Curso')) #Onde está alocado e se não possuir retornara -1

print(frase.lower().find('video')) #isso irá dar certo pois eu tranformei video me minusculo e coloquei prar procurar video em minusculo

print(frase.split()) #Divide a setença com base nos espaços

divido = frase.split()
print(divido[0]) #Mostrá o primeiro item da lista

print(divido[2] [3]) #No segundo item da lista mostre a terceira letra
