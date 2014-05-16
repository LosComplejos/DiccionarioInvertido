Indice Invertido
====================

Conceptos ACM (mono/bi grams)

Procesa los titulos y abstracts de acm.db:

1. Se almacenan los stopwords en memoria (de nltk y de fuente externa)

2. El titulo+abstract se tokeniza, todo a minusculas y se excluyen palabras de stopwords

3. Para generar monogramas, se hace lematizacion y con FreqDist consideramos monogramas y su frecuencia

4. Para generar bigramas, NO se hace lematizacion y con FreqDist consideramos bigramas y su frecuencia (ssi frec>1)

5. Se guarda todo en el txt diccionario invertido


Base de datos:
https://www.dropbox.com/s/ymz253goevhwjqm/acm.db

Programas principales:
00-title.py, 01-abstract.py, 02-title+abstract.py
