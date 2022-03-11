def update_dict(searched, my_dict):
    for char in my_dict.keys():
        if searched in my_dict[char]:
            # uno los sucesores de 'searched' al set de char
            # como son sets, no va a haber duplicados
            my_dict[char] = my_dict[char].union(my_dict[searched])

            
def build_word_from_dict(my_dict):
    ordered_dict = {char: set_of_chars for char, set_of_chars in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
    return ''.join(ordered_dict.keys())
    
def recoverSecret(triplets):
    my_dict = {}
    # cada letra estará en un diccionario como clave, cuyo valor sera un set con las letras que tiene delante
    # en los triplets.
    # Cada letra tendrá un puntaje, la de mayor puntaje estará mas cerca del principio en la palabra
    
    # El puntaje se calcula como la longitud del set de sucesores, que estará unido con el set de cada letra sucesora
    # Necesito trabajar con Set y no listas, para evitar repeticiones de letras.
    # Estamos suponiendo que cada letra que repite 1 sola vez en el string
    
    # Cada vez que se agrega una nueva letra al diccionario, o se actualiza un set de sucesores,
    # se actualiza el set de los ancestros.
    # De esa forma, a la hora de calcular el puntaje de cada letra, simplemente calculo la longitud de su set
    
    
    # clave : set de sucesores
    # cada clave en mi diccionario sera un set.
    for triplet in triplets:
        for i in range(3):
            if triplet[i] in my_dict.keys():
                my_dict[triplet[i]] = my_dict[triplet[i]].union(set([triplet[j] for j in range(i+1,3)]))
                # si esta en el indice 0, tiene 2 delante.
                # si esta en el indice 2, el set a unir estara vacio
            else:
                my_dict[triplet[i]] = set([triplet[j] for j in range(i+1,3)])
            # actualizo el diccionario, para que todos los que tengan como sucesor a 'triplet[i]'
            # tambien tengan como sucesor a los sucesores de 'triplet[i]'
            update_dict(triplet[i], my_dict)
            
    return build_word_from_dict(my_dict)
