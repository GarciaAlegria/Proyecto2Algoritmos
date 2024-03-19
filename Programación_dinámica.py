import time

def min_edit_distance_dp(str1, str2):
  m = len(str1)
  n = len(str2)

  # Creamos una tabla para almacenar los resultados de los subproblemas
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  # Llenamos la tabla de abajo hacia arriba
  for i in range(m + 1):
    for j in range(n + 1):
      # Si una de las cadenas es vacía, la distancia de edición es la longitud de la otra cadena
      if i == 0:
        dp[i][j] = j
      elif j == 0:
        dp[i][j] = i
      # Si los caracteres en la posición actual son iguales, no hay operación necesaria
      elif str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        # Si los caracteres son diferentes, consideramos las operaciones de inserción, eliminación y sustitución
        dp[i][j] = 1 + min(dp[i][j - 1],  # Inserción
                             dp[i - 1][j],  # Eliminación
                             dp[i - 1][j - 1])  # Sustitución

  return dp[m][n]

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
  distance = min_edit_distance_dp(word1, word2)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Distancia de edición ({word1}, {word2}): {distance}")
  print(f"Tiempo transcurrido: {elapsed_time}")
