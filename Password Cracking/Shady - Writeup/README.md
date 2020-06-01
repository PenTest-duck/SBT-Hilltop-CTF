# Shady - Writeup

This password cracking challenge requires custom wordlist generation by manually scraping a website for song titles and performing simple word manipulation by appending three numbers.

*This challenge also had 2 references to Eminem: the name of this challenge comes from Eminem's alter-ego Slim Shady and the username of the "Eminem super-fan" is 'stan', which is the title of Eminem's 2000 song, and means an overly obsessed fan.*

The 2 files in the challenge prompt refers to /etc/passswd and /etc/shadow and it can be inferred that the password is related to the rapper Eminem, most likely the title of one of his songs.

# Initial Wordlist Generation

In order to generate the initial wordlist, the solver must find a list of songs released by Eminem, most likely in a website.
The most ideal website should have little or no text between each title, such as https://www.songfacts.com/songs/eminem where only the year of release separate each title.

Once a website is chosen, the solver should look into the HTML source for the section which contains the titles.
In Chrome, the solver can right click on a song title, click Inspect, find the parent class which contains a list of all the song titles and right click > Copy > Copy element.
Once the list has been copied, paste it into a file in order to 'clean up' the wordlist and remove all unnecessary text.

In our case, the pasted list in web_scrape.txt is all in a single line.
For ease of viewing, we should add some newline characters by using the *tr* command.

`cat web_scrape.txt | tr '>' '\n' | tr '<' ' '`

This replaces all the closing element tags with newline characters and virtually removes the opening tags.

To remove all unnecessary text and whitespace in, and at the end of lines, a series of *grep*, *cut* and *sed* can be used.

`cat web_scrape.txt | tr '>' '\n' | tr '<' ' ' | grep '/a' | grep -v href | cut -d '/' -f 1 | sed 's/ //g' > wordlist.txt`

The wordlist can now be manually reviewed and tidied up by replacing &amp with & and removing apostrophes and brackets.

# Attempting to Crack the Hash

There are two major password cracking tools: John the Ripper and Hashcat. 
In our case, we will use Hashcat to use our initial wordlist to hopefully crack the given hash.
If opting to use JtR, the passwd and shadow files should be *unshadow*ed before cracking.

Firstly, from the shadow file, only the salt and the hash should be copied and pasted into a separate file (from $6$ to the next colon).
Then, we can use Hashcat in UNIX sha512crypt mode (-m 1800) using a dictionary attack (-a 0) with our initial wordlist and output the result to a file (note that you may have to use the *--force* parameter for Hashcat to start).

`hashcat -m 1800 -a 0 -o out.txt hash.txt init_wordlist.txt --force`

Once finished, you should notice that Hashcat isn't able to crack the hash.
This is because we may need to append some extra characters the user added 'for security'.

# Improving the Wordlist

The very first thing that comes to mind when a user is increasing the length of their password is adding numbers.
Adding a few digits to the end of a password is a very common way for users to bypass any password length enforcements.
We can write a Bash script that takes advantage of *crunch*, a tool used for generating wordlists.

```
#!/bin/bash

cat $1 | while read -r passwd; do
	length=$(($(echo $passwd | wc -m)+2))  # Set +n to number of chars to add - 1
	crunch $length $length -t $passwd%%% >> wordlist.txt  # Set the number of %s to n + 1
done
```

The script takes a wordlist file as an argument, appends *x* digits to each password and adds the newly generated wordlist for each password to an improved wordlist.

Adding three digits to each word and running Hashcat using the improved wordlist should crack the hash to reveal a password of TheWayIAm812.

Flag: HilltopCTF{TheWayIAm812}

# References
A list of Eminem songs: https://www.songfacts.com/songs/eminem
