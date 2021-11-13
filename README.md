# Anki Sentence Maker

This project is part of a selection process for a sopt of Automation Tester in the Voxy team. This project contains a set of set
Anki Sentence Maker is a personal project that has helped me increase my vocabulary in english, and it stemmed from a matter of preference in how I import my sentences on Anki.

## Requirements

* [Python 3](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/)
* Firefox [GeckoDriver]()

## Getting started

Go to the directory where requirements.txt is located and run 

```
pip install -r requirements.txt
```

After install all the packages, you need to install 

```
python3 main.py desecrate meaning
```

In case of look expressions up separated by spaces, wrap it up with quotation marks
> Example: a means to an end

```
python3 main.py desecrate "a means to and end" meaning
```

The script will try to find these words, and it is going to save into the root folder in the format below

```
sentences-25-04-2020.csv
```

And that is it. You can import in your Anki using the csv file.

## How it is going to work

* User will give a list of words
* The script will look it up in a variety of dictionaries
* The script will create a .csv file with rows in the format below

## Card format

|Sentence (Front card) |Information (Back card)|
|:-------------:|:-------------:|
|He played with the band at a recent gig.| gig /ɡɪɡ/ (a performance by musicians playing popular music or jazz in front of an audience; a similar performance by a comedian)|

> This way, we have the information about the word that we would like to learn as a short definition about it and its phonetic notation.


## Author

[Caio Pedreira](https://github.com/caiovvp)
