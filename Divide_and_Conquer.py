def min_edit_distance_dc(str1, str2):
    # Función auxiliar para calcular la distancia de edición entre dos subcadenas
    def min_edit_distance_helper(str1, str2, m, n):
        # Caso base: si una de las cadenas está vacía, la distancia de edición es la longitud de la otra cadena
        if m == 0:
            return n
        if n == 0:
            return m
        
        # Si los caracteres en la posición actual son iguales, no hay operación necesaria
        if str1[m - 1] == str2[n - 1]:
            return min_edit_distance_helper(str1, str2, m - 1, n - 1)
        
        # Si los caracteres son diferentes, consideramos las operaciones de inserción, eliminación y sustitución
        return 1 + min(min_edit_distance_helper(str1, str2, m, n - 1),   # Inserción
                       min_edit_distance_helper(str1, str2, m - 1, n),   # Eliminación
                       min_edit_distance_helper(str1, str2, m - 1, n - 1)   # Sustitución
                      )
    
    return min_edit_distance_helper(str1, str2, len(str1), len(str2))

# Ejemplo de uso
str1 = "kitten"
str2 = "sitting"
print("Distancia de edición (Divide and Conquer):", min_edit_distance_dc(str1, str2))
