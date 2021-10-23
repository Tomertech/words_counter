# Words counter

An API with 2 endpoint: `word_counter.py` and `word_statistics.py`. 

* `word_counter.py` - receives a text input and counts the number of appearances for each word in the input.
* `word_statistics.py` - receives a word and returns the number of times the word appeared so far (in all previous calls) 


### How to use
First, clone the project.
Now, you can either:
1.Import `word_counter.py` and `word_statistics.py` and use it's API.
2.Use the CLI (command line interface) that is given below.


##### Using the CLI :

When using the Counter endpoint there are 3 options:

* Insert a path to a text file:
```
py main.py --service counter --source this_is_a_path/text_file.txt --type file
```

* Insert a URL to text:
```
py main.py --service counter (or c) --source this_is_a_url --type url
                            
```

* Insert a string:
```
py main.py --service counter --source this_is_a_string --type string
```

##### Using the Statistics endpoint:
* Get the number of times a word appeared so far
```
py main.py --service statistics (or s) --word this_is_the_word
```

##### Reset the counter:
```
py main.py --service reset (or r)
```

### Assumptions
* All given texts are encoded by 'utf-8' format
* Only alphabet consecutive sequences ('a'-'z' or 'A'-'Z') counts as words
* All words are considered as case insensitive
* Any non-alphabet char will be considered as a separator between chars sequences - words


#### Input Output Examples
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

### Examples
Using `word_counter` with a file
```
py main.py --service counter --source tests/captmidn.txt --type file
Got it, now processing...
Done
```

Using `word_counter` with a url
```
py main.py --service counter --source http://www.textfiles.com/100/cDc-0200.txt --type url
Got it, now processing...
Done
```

Using `word_counter` with a string
```
py main.py --service counter --source Hey Lemonade! looking forward to hearing from you :) --type string
Got it, now processing...
Done
```

Using `word_statistics`
```
py main.py --service statistics --word the
The word "the" appeared so far 713 times
```

Resetting the `word_counter`
```
py main.py --service reset
counter was reset
```

### Tests
The project's folder includes `tests.py` file that contains a unittest for the API



### Author

**Tomer Ashuach**  [GitHub](https://github.com/Tomertech) [LinkedIn](https://www.linkedin.com/in/Tomerashuach/)