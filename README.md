# med.py: Middle English Dictionary search

med.py is a short and simple script for searching the Middle English Dictionary. 

I do a lot of searching the MED for research projects, usually researching medieval names, and the default "closed" search results are never what I am looking for. So it used to be that every single time I did a search I had to reload the page to load it in "open" format. It got old.

So this script was originally written to give me a default search that suits my needs a bit better. It would give me a simple list of words, and when I clicked on one, it would open the associated MED page, *already in "open" (quotations showing) format!* Maybe not of use for anyone else... but I sure used it a lot! Unfortunately, around 2018 the MED updated their website so the app broke. 

In 2024, I decided to fix it, and now you can search directly without going through the MED's search interface again! But to automatically load the pages in "open" format, you will have to use the additional userscript with a userscript manager such as Tampermonkey, because that's now controlled via javascript on the MED's side.

## Installation and usage:

* Download one of the versions of med.py. The "g" version has a GUI dialog box; the other is entirely from the command line.
* You will need these additional libraries installed in your copy of Python: requests, BeautifulSoup. If you are going to run the "g" version, add PySimpleGUI.
* When in the directory you've installed med.py into, type `python3 med.py` or `python3 med2g.py` into your terminal.
* You will either get a prompt in your terminal, or a GUI dialog box. Choose the word you are searching for. It's a "headword and alternate forms" search so you'll need to know at least one Middle English spelling of the word.
* A web page will open with a list of words that match your search. Click on the word you want to look at, and it will open the MED page for that word.
* To force the MED page to open in "show quotations" mode, download MED Open Click.user.js and follow the directions in your userscript manager to activate it.

## Things to note about med.py 2.0:
* Unless you use MED Open Click.user.js with a userscript manager, you will have to click the "Show Quotations" button on the MED pages you go to. This is less annoying than it used to be, though, because there is no page reload.
* The search is currently just a simple "headword with alternate spellings" search. I'll add some of the others eventually, maybe.
* If you want a GUI dialog box to enter your search words, grab the version with "g" on the end (e.g. 2.0g).
* It is currently coded to save the html to `~/Documents/medresults.html`. You may want to change that. 

med.py uses the BeautifulSoup libraries.

-- Wendi

## Updates

**2.0g and MED Open Click.user.js (10 August 2024):**

This version of the script uses PySimpleGUI to make a search dialogue box. You still need to start it from the command line for now. The regular 2.0 script is still current if you don't care about the dialog box. If you use this "g" version, you'll see the search loop has returned -- you can search over and over without reloading the program, until you close the dialog box. MED Open Click.user.js is a separate userscript that can be used to force MED pages to be opened in "show quotations" mode, just like the pre-2018 version of med.py! 

**2.0 (8 August 2024):**

Yikes, it's been a long time! Updated code to Python 3. Removed Pashua GUI since it is no longer supported. Removed loop, though clearly it's useful, so it may return sometime! App is now command-line only. You can't open pages in open quotations mode; blame the MED's redesign (it is a lot better, but not for med.py!).

**1.0.2 (30 September 2013):**

Added loop, so you can search over and over again without rerunning the script. Added GUI dialog box using Pashua. Made app version with Platypus, using this script. Custom icon for the app version. Program now closes after you cancel search. Pages slightly prettier.
Removed restricted surname page search after deciding it's not very useful.

**1.0.1 (14 Sep 2013):**

Added ability to restrict search to pages that contain the term "surname." N.B. -- the MED usually marks surnames in a "surnames or place names" category, but not always! It is possible to miss something with this search for that reason. But for a quick search it works pretty well.

**1.0 (13 Sep 2013):**

Functional if not pretty. Features: Boolean search with default "open" results, correct response (in console) to searches with empty results, correct response to single result searches, which are displayed differently on the OED site.









   
