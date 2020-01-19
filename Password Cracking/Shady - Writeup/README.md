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


# References
A list of Eminem songs: https://www.songfacts.com/songs/eminem
