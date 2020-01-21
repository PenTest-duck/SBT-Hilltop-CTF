# Ash - Writeup

This OSINT challenge requires the solver to view image metadata, navigate in Github and use the Wayback Machine in order to reach the flag.
This challenge follows the Internet footprints of an "Asher Harrison", beginning with his image of a quote to his Twitter, Github and Pastebin accounts.

# Viewing the Metadata

The actual quote in the given image is a red herring - the real "breadcrumb" lies within the image's metadata, specifically in the description.
There are a few websites that can be used to view the metadata, including https://www.thexifer.net and http://exif.regex.info/exif.cgi.
Note that some metadata viewers won't display the description.

The description reveals a Twitter account: @AsherH0902

# Navigating In Github

The very first tweet on the Twitter account reveals a Github Pages blog, made using Jekyll, a popular Github blog framework.
Looking at the Blog and About sections won't reveal anything except some meaningless text.
Now, keeping in mind that the blog is made through Github Pages, the source repository for the blog can be found with a simple search in Github of the user AsherH0902.

Looking through the different directories and files shouldn't reveal anything interesting.
Instead, as the second hint suggests, you must switch from the master branch to the draft branch.
There, within the \_posts directory, you will find an unpublished post containing a Pastebin link.

# Using Wayback Machine to Retrieve the Flag

When you follow the Pastebin URL, you should be notified that the page had been removed.
In order to view a version of the page when it wasn't deleted, we can use the Wayback Machine at http://www.wayback.com and enter in our URL.
You should find 1 snapshot of the page on the 21st of January and viewing it reveals a Pastebin page with the flag.

Flag: HilltopCTF{d0nt_l34k_1nf0_0nl1n3}
