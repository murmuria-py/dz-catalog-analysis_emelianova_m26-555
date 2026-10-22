import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    total_rating = 0

    for movie in movies:
        total_rating += movie["rating"]

    count = len(movies)

    return round(total_rating / count, 1)

def catalog_age_stats(movies, current_year=2026):
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    oldest = max(ages)
    newest = min(ages)

    average_age = sum(ages) / len(ages)
    rounded_average = math.ceil(average_age)
    return (oldest, newest, rounded_average)

def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60

    return f"{hours}ч {mins}м"

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ :
            return "старые"

def demo_1():
    print("Фильмы не в жанре comedy:")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

def demo_2():
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print("Найден шедевр:", movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено") # Проверено с rating > 9.5

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    words = title.split(" ")
    result = []
    for word in words:
        capitalized = word[0].upper() + word[1:]
        result.append(capitalized)
    return " ".join(result)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f'{duration}, жанры: {genres}'
    )

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda m: m["rating"],
        reverse=True
    )
    titles  = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda m: m["rating"],
        reverse=True
    )
    result = []
    for movie in sorted_movies[:n]:
        result.append((movie["title"], movie["rating"]))
    return result

def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography

avg = average_rating(movies)
above_avg = {
    movie["title"]:movie["rating"]
    for movie in movies
    if movie["rating"] > avg
}

def all_genres(movies):
    result = set()
    for movie in movies:
        result = result | movie["genres"]
    return result

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    for movie in movies_a:
        genres_a = genres_a | movie["genres"]
    genres_b = set()
    for movie in movies_b:
        genres_b = genres_b | movie["genres"]
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def demo_3():
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

def demo_4():
    total_minutes = sum(
        m["duration_min"]
        for m in movies
        if m["rating"] > 7
    )
    print(total_minutes)

def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")

    oldest, newest, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")

    print("\nТоп-3 фильма:")
    top3 = sorted(
        movies,
        key=lambda m: m["rating"],
        reverse=True
    )[:3]
    for movie in top3:
        print("  " + format_report_line(movie))

    print("\nФильмов по жанрам:")
    counts = count_by_genre(movies)
    for genre, count in sorted(
        counts.items(),
        key=lambda pair: (-pair[1], pair[0]),
    ):
        print(f"  {genre} — {count}")

    genres_str = ", ".join(sorted(all_genres(movies)))
    print(f"\nВсе жанры каталога: {genres_str}")



def main():
    print("Hello from dz-catalog-analysis-emelianova-m26-555!")
    build_report(movies)

if __name__ == "__main__":
    main()