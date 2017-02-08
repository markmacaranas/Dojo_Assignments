Regular Expressions
Regular expressions, commonly known as regex, are a set of rules for identifying or matching strings.
Many programming languages, including Python, support use of regular expressions for matching and searching strings.

Although regex can make some specific tasks much easier, it's important to keep in mind that they’re not the right tool for every job.
Regular expression string searches can be what is known as expensive operations.
This occurs when general search terms are used, which often force string comparisons to become exponentially complex.
Even if this doesn't make too much sense now, just realize that regex use can lead to some performance issues with large data sets,
so they should be used sparingly, and optimized in cases where they are the best option.

Common uses include searching string inputs from users. Search engines and other form input, like user registration and login,
are great examples of correct uses for regular expressions.
Later on we'll see a couple of practical uses for regex, including validating a user email format in Flask, and for recognizing url patterns in our Django apps.

The strings we build for comparison in regex are known as patterns. In a regex pattern,
most characters just represent themselves, so “a” matches “a”, “b” matches “b” (but not “B”), and so forth.
Some characters, though, have special meanings; some of the most common are

 .	Matches any character except a new line.
\w 	Matches any letter or digit.
+	The pattern before it can appear 1 or more times.
 *	The pattern can appear any number of times, including none.
A full list of the special characters can be found on the Google for Education: Tutorial on
Python Regular Expressions (https://developers.google.com/edu/python/regular-expressions)
or in the Python re module documentation (https://docs.python.org/2/library/re.html)

Note that in Python regexes are usually raw strings (like r"this", with an “r” at the start);
this tells Python to treat the string exactly as you entered it, rather than applying its normal substitutions (like changing “\n” to the new-line character.)

re.search(pattern, string) is a function that scans a string for a specific regex pattern
 and returns a match object (a collection of data about the match) if it finds a match and None otherwise.
 One common use is to make this part of an if statement:

  if re.search(r"a.*a"):
   print("That string had at least two 'a's in it!")
  else:
   print("No more than one 'a' found!")
