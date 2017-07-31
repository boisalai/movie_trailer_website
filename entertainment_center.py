﻿import media
import fresh_tomatoes

# I have applied the following rules...
# Use 4 spaces per indentation level.
# Limit all lines to a maximum of 79 characters.
# Line break before a binary operator.
# Imports should usually be on separate lines.

incendies = media.Movie(
    "Incendies",
    "Incendies is a 2010 Canadian mystery-drama film written and directed " +
    "by Denis Villeneuve.",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/Incendies.jpg",
    "https://www.youtube.com/watch?v=0nycksytL1A")

prisoners = media.Movie(
    "Prisoners (2013 film)",
    "Prisoners is a 2013 American thriller film directed by Denis " +
    "Villeneuve from a screenplay written by Aaron Guzikowski. The film " +
    "has an ensemble cast including Hugh Jackman, Jake Gyllenhaal, " +
    "Viola Davis, Maria Bello, Terrence Howard, Melissa Leo and Paul Dano.",
    "https://upload.wikimedia.org/wikipedia/en/6/63/Prisoners2013Poster.jpg",
    "https://www.youtube.com/watch?v=KWhS0xN3C0g")

enemy = media.Movie(
    "Enemy (2013 film)",
    "Enemy is a 2013 psychological thriller film directed by Denis " +
    "Villeneuve, produced by M.S. Faura and Niv Fichman and written " +
    "by Javier Gullón, loosely adapted from José Saramago's 2002 " +
    "novel The Double.",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/Enemy_poster.jpg",
    "https://www.youtube.com/watch?v=FJuaAWrgoUY")

sicario = media.Movie(
    "Sicario (2015 film)",
    "Sicario is a 2015 American crime-drama film directed by Denis " +
    "Villeneuve, written by Taylor Sheridan, and starring Emily Blunt, " +
    "Benicio del Toro, and Josh Brolin. ",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Sicario_poster.jpg",
    "https://www.youtube.com/watch?v=G8tlEcnrGnU")

arrival = media.Movie(
    "Arrival",
    "When twelve mysterious spacecraft appear around the world, " +
    "linguistics professor Louise Banks is tasked with interpreting " +
    "the language of the apparent alien visitors.",
    "https://upload.wikimedia.org/wikipedia/en/d/df" +
    "/Arrival%2C_Movie_Poster.jpg",
    "https://www.youtube.com/watch?v=DEX_ziImldA")

movies = [incendies, prisoners, enemy, sicario, arrival]

fresh_tomatoes.open_movies_page(movies)
