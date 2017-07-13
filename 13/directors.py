import csv
from collections import defaultdict, namedtuple
from decimal import Decimal,getcontext,ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_FLOOR, Context

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
getcontext().prec = 3

def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    with open(MOVIE_DATA, 'r', newline='', encoding='utf8') as file:

        # Create a list from the data in the CSV file
        reader = csv.DictReader(file, delimiter=',')
        csv_data = list([row['director_name'], row['movie_title'].strip(' ').strip(u'\xa0')
            , row['title_year'], row['imdb_score']] for row in reader)

        # Create a set of director names (set = unique names)
        director_names = {name[0] for name in csv_data}
        # Create an empty dictionary to hold the movie data
        director_dict = {}

        # Add each director to the dict along with their movie data
        for name in sorted(director_names):
            director_dict[name] = \
                [Movie(title=data[1], year=data[2] ,score=data[3]) for data in csv_data if data[0] == name]

        # Return the completed dict object
        return director_dict

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''

    for director in directors:
        if len(directors[director]) > MIN_MOVIES:
            yield (
                    director
                    # Average (score divided by number of movies)
                   ,  Decimal(sum(Decimal(movie[2]) for movie in directors[director])) /
                     Decimal(len(list(movie[2] for movie in directors[director])))
                    , Decimal(sum(Decimal(movie[2]) for movie in directors[director]))

                    )


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''

    # Calculate the mean - Sum of all movie ratings divided by the number of movies
    # Round to 1 decimal place
    return round(
                (sum(Decimal(movie[2]) for movie in movies)) / (len(list(movie[2] for movie in movies)))
            , 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    #directors = get_average_scores(directors)
    #print_results(directors)

    movies_sergio = directors['Sergio Leone']
    print('Sergio Leone' in directors)
    print(_calc_mean(movies_sergio))

    movies_nolan = directors['Christopher Nolan']
    print(_calc_mean(movies_nolan))


    for d in directors:
        #print(f'{d} - {len(directors[d])} - {directors[d]}')
        pass
        #print(d)

if __name__ == '__main__':
    main()
