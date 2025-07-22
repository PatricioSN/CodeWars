def solution(string):
    counter = 0
    lista = []
    nova_string = ""
    if (len(string)) % 2 != 0: #Verifica se o número é impar, e em caso afirmativo, adiciona "_" ao final da string.
        string += "_"

    for i in range(len(string)):
        nova_string += string[i] #Percore a lista e adiona o char da posição atual de "i".
        counter +=  1
        if counter == 2: #Quando o contador indica que 2 caracteres ja foram adicionados, insere essa nova string na lista.
            lista.append(nova_string)
            counter = 0 #Reseta os valores
            nova_string = ""

    print(lista)
    return lista





