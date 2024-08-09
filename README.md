# med.py: Middle English Dictionary search

med.py is a short and simple script for searching the Middle English Dictionary. 

I do a lot of searching for research projects, usually researching medieval names, and the default "closed" search results are never what I am looking for. So every single time I did a search I had to reload the page to load it in "open" format. It gets old.

So this script was originally written to give me a default search that suits my needs a bit better. It would give me a simple list of words, and when I clicked on one, it would open the associated MED page, *already in "open" format!* Maybe not of use for anyone else... but I sure used it a lot! Unfortunately, around 2018 the MED updated their website so the app broke. 

In 2024, I decided to fix it, but so far I cannot find any way to automatically load the pages in "open" format, because that's now controlled via javascript on the MED's side. Still, there is some useful functionality with the script -- you can search directly without going through the MED's search interface. 

## Things to note about med.py 2.0:
* You will have to click the "Show Quotations" button on the MED pages you go to. This is less annoying than it used to be, though, because there is no page reload.
* The search is currently just a simple "headword with alternate spellings" search. I'll add some of the others eventually, maybe.
* The Pashua software that gave it a GUI is no longer being maintained, so I removed it. This means that you need to run this from the command line for now.
* It is currently coded to save the html to `~/Documents/medresults.html`. You may want to change that. 

med.py uses the BeautifulSoup libraries.

-- Wendi

## Updates

2.0 (8 August 2024):
Yikes, it's been a long time! Updated code to Python 3. Removed Pashua GUI since it is no longer supported. Removed loop, though clearly it's useful, so it may return sometime! App is now command-line only. You can't open pages in open quotations mode; blame the MED's redesign (it is a lot better, but not for med.py!).

1.0.2 (30 September 2013):

Added loop, so you can search over and over again without rerunning the script. Added GUI dialog box using Pashua. Made app version with Platypus, using this script. Custom icon for the app version. Program now closes after you cancel search. Pages slightly prettier.
Removed restricted surname page search after deciding it's not very useful.

1.0.1 (14 Sep 2013):

Added ability to restrict search to pages that contain the term "surname." N.B. -- the MED usually marks surnames in a "surnames or place names" category, but not always! It is possible to miss something with this search for that reason. But for a quick search it works pretty well.

1.0 (13 Sep 2013):

Functional if not pretty. Features: Boolean search with default "open" results, correct response (in console) to searches with empty results, correct response to single result searches, which are displayed differently on the OED site.









   
