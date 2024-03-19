import time

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
    return 1 + min(min_edit_distance_helper(str1, str2, m, n - 1),  # Inserción
                  min_edit_distance_helper(str1, str2, m - 1, n),  # Eliminación
                  min_edit_distance_helper(str1, str2, m - 1, n - 1))  # Sustitución

  return min_edit_distance_helper(str1, str2, len(str1), len(str2))

# Lista de 30 pares de palabras
word_pairs = [
  ("kitten", "sitting"),
  ("sunday", "saturday"),
  ("algorithm", "alligator"),
  ("levenshtein", "levenstein"),
  ("dynamic", "programming"),
  ("recursion", "repetition"),
  ("insertion", "deletion"),
  ("substitution", "transposition"),
  ("palindrome", "anagram"),
  ("edit", "distance"),
  ("string", "similarity"),
  ("comparison", "measurement"),
  ("computation", "calculation"),
  ("efficiency", "performance"),
  ("accuracy", "precision"),
  ("speed", "velocity"),
  ("time", "duration"),
  ("space", "memory"),
  ("complexity", "difficulty"),
  ("cost", "expense"),
  ("benefit", "advantage"),
  ("drawback", "disadvantage"),
  ("optimization", "improvement"),
  ("heuristic", "rule of thumb"),
  ("approximation", "estimation"),
  ("solution", "answer"),
  ("problem", "challenge"),
  ("task", "assignment"),
  ("goal", "objective"),
  ("purpose", "intent"),
]

# Medición del tiempo para cada par de palabras
for word1, word2 in word_pairs:
  start_time = time.time()
  distance = min_edit_distance_dc(word1, word2)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Distancia de edición ({word1}, {word2}): {distance}")
  print(f"Tiempo transcurrido: {elapsed_time}")
