import media
import fresh_tomatoes

# define movie details

inception = media.Movie(
    "Inception",
    'A thief who steals corporate secrets through use of the dream-sharing '
    'technology is given the inverse task of planting an idea into the mind '
    'of a CEO.',
    "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0",
    "2010")

the_shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    'Two imprisoned men bond over a number '
    'of years, finding solace and eventual '
    'redemption through acts of common decency.',
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
    "https://www.youtube.com/watch?v=zdWZBvd0-pg",
    "1994")

lost_in_translation = media.Movie(
    "Lost in Translation",
    'A faded movie star and a neglected young woman form an unlikely bond '
    'after crossing paths in Tokyo.',
    "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",
    "https://www.youtube.com/watch?v=6wXjObmziEk",
    "2003")

schindlers_list = media.Movie(
    "Schindler's List",
    'In Poland during World War II, Oskar Schindler gradually becomes concerned '
    'for his Jewish workforce after witnessing their persecution by the Nazis.',
    "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
    "https://www.youtube.com/watch?v=JdRGC-w9syA",
    "1993")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    'The lives of two mob hit men, a boxer, a gangster\'s wife, and a pair of '
    'diner bandits intertwine in four tales of violence and redemption.',
    "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
    "https://www.youtube.com/watch?v=ewlwcEBTvcg",
    "1994")

the_usual_suspects = media.Movie(
    "The Usual Suspects",
    'A sole survivor tells of the twisty events leading up to a horrific gun '
    'battle on a boat, which begin when five criminals meet at a seemingly '
    'random police lineup.',
    "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",
    "https://www.youtube.com/watch?v=oiXdPolca5w",
    "1995")

the_intouchables = media.Movie(
    "The Intouchables",
    'After he becomes a quadriplegic from a paragliding accident, an aristocrat '
    'hires a young man from the projects to be his caregiver.',
    "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
    "https://www.youtube.com/watch?v=34WIbmXkewU",
    "2011")

pans_labyrinth = media.Movie(
    "Pan's Labyrinth",
    'In the falangist Spain of 1944, the bookish young stepdaughter of a '
    'sadistic army officer escapes into an eerie but captivating fantasy world.',
    "https://upload.wikimedia.org/wikipedia/en/6/67/Pan%27s_Labyrinth.jpg",
    "https://www.youtube.com/watch?v=EqYiSlkvRuw",
    "2006")

up = media.Movie(
    "Up",
    'Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his '
    'home equipped with balloons, inadvertently taking a young stowaway.',
    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=ORFWdXl_zJ4",
    "2009")

movies = [inception, pans_labyrinth, the_shawshank_redemption, lost_in_translation,
          schindlers_list, pulp_fiction, the_usual_suspects, the_intouchables, up]

# generate movies html page
fresh_tomatoes.open_movies_page(movies)
