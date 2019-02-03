# The Wire

**The·Wire**  */ˈTheˌWire/*

*Noun:*  
A one-hour HBO drama set and produced in Baltimore Maryland.

*Synonyms:*	
Breaking Bad, Game of Thrones.

![Characters](assets/montage.jpg "Characters")

## Description

A personal project of mine. I want to take the story of the wire and map it onto a 'Graph Database'

I'll be updating this repo as I go so the README will change.

I'm starting off small and working my way out.

### Characters

As stated above I am starting off small. So initiallty I am taking information from the entry of [wikipedia](https://en.wikipedia.org/wiki/The_Wire). I found a table of [primary characters](https://en.wikipedia.org/wiki/List_of_The_Wire_characters). A quick copy and paste onto [Google SpreadSheets](https://www.google.com/sheets/about/) with a bit of manual manipulation and hey preso. My first [data sheet](https://github.com/swmcc/the-wire/commit/a72d6c5229bebf8fa8f0590b99d60de57ddec1a4). All I need to do is to injest the information. So without further ado... lets open my first [GitHub Issue](https://github.com/swmcc/the-wire/issues/1)


## Links



## Development Info

> Ensure that you have [pipenv](https://pipenv.readthedocs.io/) installed.

##### Start server
```sh
export FLASK_ENV=development
python manage.py run
```
##### Display characters to json
```sh
python services/characters/project/characters.py data/characters.csv
```




