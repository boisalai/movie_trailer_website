# Movie Trailer Website
> Alain Boisvert, Québec, Canada, 2017-07-30.<br>
> Updated 2017-07-31: See section [Check code for PEP8 requirements](#pep8) below.

## Summary

Here is my first project for the "Full Stack Web Developer Nanodegree".

This repository contains a Python code to store a list of movies from my favorite film director and writer (Denis Villeneuve), including box art imagery and a movie trailer URL. This data is served as a web page allowing visitors to review their movies and watch the trailers.

## How did I develop this code?

This application contains three python files.
- `media.py`: This class provides a way to store movie related information.
- `entertainment_center.py`: This code creates five movies instances of Denis Villeneuve, and execute `fresh_tomatoes.open_movies_page()` to display a movie website with these movies.
- `fresh_tomatoes.py`:	This Python module generate a website that displays these movies. This module comes from [here](https://github.com/udacity/ud036_StarterCode/blob/master/fresh_tomatoes.py).

## What did I learn?

I already knew Java and javascript. In this work, I learned the syntax of Python, where is the documentation, IDLE (Python's Integrated Development Environnement), how to submit a project in GitHub, etc. 

This project is relatively easy since all the instructions found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/fe2ad0cf-06b0-4541-87ab-0b6d59e21ef1/modules/3a35570a-8e9d-4088-96d0-3dbe22d1fcb6/lessons/3561209451239847/concepts/36057486950923).

Nevertheless, it took all my Sunday, but I'm happy with the result.

Among others, I applied the following syntax rules:
- Use 4 spaces per indentation level.
- Limit all lines to a maximum of 79 characters.
- Line break before a binary operator.
- Imports should usually be on separate lines.

<a name="pep8"></a>
## Check code for PEP8 requirements (update 2017-07-31 after review)

I used the online PEP8 checker. I simply paste my code into this [website](http://pep8online.com/), see the results, fix my code until the PEP8 check finds no errors.

Here, log file from online PEP8 checker.
- [media.py](https://github.com/boisalai/movie_trailer_website/blob/master/PEP8/result_20170731_224930.txt)
- [entertainment_center.py](https://github.com/boisalai/movie_trailer_website/blob/master/PEP8/result_20170731_225329.txt)

However, I am not comfortable with the rule "line break before binary operator". Although I have corrected the problem indicated by PEP8 checker, I am rather of the same opinion with what is written here: [Should a line break before or after a binary operator?](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator) and [W503 enforces breaking after binary operators but PEP-8 appears to disagree](https://github.com/PyCQA/pycodestyle/issues/513).

Reviewer, what do you think about that? :confused:





## Quickstart

To run the application, you need to download the project and run `entertainment_center.py`.

Here's what you should see on your screen.

![Screenshot 1](https://raw.githubusercontent.com/boisalai/movie_trailer_website/master/images/screen.png "Screenshot 1")

## Who is Denis Villeneuve?

Denis Villeneuve is a Canadian film director and writer. He is a four-time recipient of the Canadian Screen Award (formerly Genie Award) for Best Direction, for Maelström in 2001, Polytechnique in 2010, Incendies in 2011, and Enemy in 2013. See [Wikipedia](https://en.wikipedia.org/wiki/Denis_Villeneuve).

## License

The contents of this repository are covered under the [MIT License](LICENSE).

