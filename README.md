# Words counter

An API with 2 endpoint: `word_counter.py` and `word_statistics.py`. 

* `word_counter.py` - receives a text input and counts the number of appearances for each word in the input
* `word_statistics.py` - receives a word and returns the number of times the word appeared so far (in all previous calls) 


### How to use
1.Clone the project  
2.Go to the directory where you cloned the project to and run a command line  
3.Install requirements
```
pip install -r requirements.txt
```

4.Run the API using:
```
py api.py
```
Now you can use the two endpoints: `wordscounter` and `statistics`.

##### Usage example with Postman

When using the Counter endpoint there are 3 options:

Insert a path to a text file:
```
POST http://127.0.0.1:5000/wordscounter?source=file_path/file.txt&type=string

Got it!
```

Insert a URL to text:
```
POST http://127.0.0.1:5000/wordscounter?type=url&source=http://www.textfiles.com/100/hack11a.txt                            

Got it!
```

Insert a string:
```
POST http://127.0.0.1:5000/wordscounter?type=url&source="Hey Lemonade! looking forward to hearing from you :)"

Got it!
```

##### Using the Statistics endpoint

Get the number of times a word appeared so far:
```
GET http://127.0.0.1:5000/statistics?word=lemonade

The word "lemonade" appeared so far 12 times
```

##### Reset the counter

Reset all words in counter:
```
DELETE http://127.0.0.1:5000/statistics

Counter was reset
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


### Tests
The project's folder includes `tests.py` file that contains a unittest for the component


### Author

**Tomer Ashuach**  [GitHub](https://github.com/Tomertech) [LinkedIn](https://www.linkedin.com/in/Tomerashuach/)