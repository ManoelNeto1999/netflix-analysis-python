import pandas as pd
import matplotlib.pyplot as plt

#convertendo o arquivos csv em tipo pandas
netflix_df = pd.read_csv(r'C:\Users\manoe\OneDrive\Documents\dataCamp\arquivosCSV\netflix_data.csv')

#filtrando apenas os tipos de conteudo que são filmes
justMovies = netflix_df['type'] == 'Movie'
netflix_subset = netflix_df[justMovies]

#filtrando apenas as colunas necessarias
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

#esse filtro foi apenas para dar uma olhada na quantidade de filmes menos que 60 min
lessThan60 = netflix_movies['duration'] < 60
short_movies = netflix_movies[lessThan60]

#aqui criamos uma lista de cores para cada genero de filmes para podes ajudar no nosso grafico
colors = []
for x in netflix_movies['genre']:
    if x == "Children":
        colors.append("red")
    elif x == "Documentaries":
        colors.append("black")
    elif x == "Stand-Up":
        colors.append("blue")
    else:
        colors.append("orange")

#Aqui criamos nosso grafico de disperssão com os dados que obtivemos a cima
fig = plt.figure(figsize=(12, 8))
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c = colors)
plt.xscale('log')
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.xticks([1920, 1940, 1960, 1980, 2000, 2020], [1970, 1980, 1990, 2000, 2010, 2020])
plt.show()

