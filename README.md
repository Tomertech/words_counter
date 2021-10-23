# Words counter

An API for retrieving text from URl, file or string, parsing it and counting the words.


### Getting Started

First, we need to clone the project.\
Go to the location you want to clone the project to, and do:
```
git clone https://github.com/Tomertech/words_count.git
```

### How to use

* Import `word_counter.py` and `word_statistics.py` and use its API.

* Use the UI that is given below.


##### Using the Counter endpoint:

When using the Counter endpoint there are 3 options:

* Insert a path to a text file:
```
py main.py --service "counter" --source "this_is_a_path/text_file.txt" --type "file"
```

* Insert a URL to a text file:
```
py main.py --service "counter" (or "c") --source "this_is_a_url" --type "url"
                            
```

* Insert a string:
```
py main.py --service "counter" --source "this_is_a_string" --type "string"
```

##### Using the Statistics endpoint:
* Get a word number of appearances
```
py main.py --service "statistics" (or "s") --word "this_is_the_word"
```

##### Reset the counter:
```
py main.py --service "reset" (or "r")
```

### Assumptions
* All given texts are encoded by 'utf-8' format.
* All given arguments are valid (url is a valid url that leads to text, file path is a valid file path to a text file, a string is a valid string).
* Only alphabet sequences ('a'-'z' or 'A'-'Z') counts as words.
* Any non-alphabet char will be cleaned up.
* Any non-alphabet char will be considered as a separator between chars sequences - words.

please see the examples below.

### Input Output Examples
	a string => the dictionary that the counter creates from it: {'word': number of appearances}
	
	Me ME mE     =>     {'me': 3}
	me2          =>     {'me': 1}
	m2e          =>     {'m': 1, 'e': 1}
	{[(me)]}     =>     {'me': 1}
	m&$@e        =>     {'m': 1, 'e': 1}
	@$me#%       =>     {'me': 1}
	me,me        =>     {'me': 2}
	me.me        =>     {'me': 2}
	me-me        =>     {'me': 2}
	me@#$me      =>     {'me': 2}

	Me ME mE me-me- me2 2me me,me.me, .me. -me-     =>      {'me': 12}
	m#@e $#m$$e  %^m_*e5 &7m09e2                    =>      {'m': 4, 'e': 4}
	mmee meme                                       =>      {'mmee': 1, 'meme': 1}

### Usage Examples
Using counter with a file
```
py main.py --service "counter" --source "texty.txt" --type "file"
Got it, now processing...
Done
```

Using counter with a url
```
py main.py --service "counter" --source "http://www.textfiles.com/100/cDc-0200.txt" --type "url"
Got it, now processing...
Done
```

Using counter with a string
```
py main.py --service "counter" --source "Hey Lemonade! looking forward to hearing from you :)" --type "string"
Got it, now processing...
Done
```

Using statistics
```
py main.py --service "statistics" --word "the"
The word "the" appeared so far 713 times
```

Resetting the counter
```
py main.py --service "reset"
counter was reset
```

### Tests
The project's folder includes `tests.py` file that contains a few tests for the API



### Author

* **Tomer Ashuach**  [GitHub](https://github.com/Tomertech) [LinkedIn](https://www.linkedin.com/in/Tomerashuach/)