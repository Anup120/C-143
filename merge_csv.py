import csv

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    header = data[0]

header.append("poster_link")
with open('final.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)

with open('movie_link.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.write(f)
                        csvwriter.writerrow(movie_item)
