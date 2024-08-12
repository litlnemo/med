![MED Open Search: Easier research in the MED!](MEDOpenSearchGraphic.png)

# med.py: Middle English Dictionary search

med.py is a short and simple script for searching the Middle English Dictionary. 

I do a lot of searching the MED for research projects, usually researching medieval names, and the default "closed" search results are never what I am looking for. So it used to be that every single time I did a search I had to reload the page to load it in "open" format. It got old.

So this script was originally written to give me a default search that suits my needs a bit better. It would give me a simple list of words, and when I clicked on one, it would open the associated MED page, *already in "open" (quotations showing) format!* Maybe not of use for anyone else... but I sure used it a lot! Unfortunately, around 2018 the MED updated their website so the app broke. 

In 2024, I decided to fix it, and now you can search directly without going through the MED's search interface again! But to automatically load the pages in "open" format, you will have to use the additional userscript with a userscript manager such as Tampermonkey, because that's now controlled via javascript on the MED's side.

## Installation and usage: standalone Mac app

If you are using a Mac, it's easiest to just use the standalone app, unless you want to edit the code. 
* [Download the app here](https://github.com/litlnemo/med/releases/tag/v2.1) and save it to your Mac.
* Launch it as you would launch any other program.
* A dialog box will appear in which you can type in the word you are searching for. Hit enter/return to submit the search. It's a "headword and alternate forms" search so you'll need to know at least one Middle English spelling of the word.
* If it's your first time using the app, it will probably ask you if it's OK to access your documents folder. This is because that is where it will save the web page it generates. Don't worry, it doesn't look at anything else in there.
* Enjoy the page of search results!
* To force the MED page to open in "show quotations" mode, find MED Open Click.user.js (it was in the .zip with the app) and follow the directions in your userscript manager to activate it.

## Installation and usage: command line version

* Download one of the versions of med.py from [https://github.com/litlnemo/med](https://github.com/litlnemo/med). The "g" version has a GUI dialog box; the other is entirely used from the command line.
* You will need these additional libraries installed in your copy of Python: requests, BeautifulSoup. If you are going to run the "g" version, add PySimpleGUI.
* When in the directory you've installed med.py into, type `python3 med.py` or `python3 med2g.py` into your terminal.
* You will either get a prompt in your terminal, or a GUI dialog box. Choose the word you are searching for. It's a "headword and alternate forms" search so you'll need to know at least one Middle English spelling of the word.
* If it's your first time using the app, it will probably ask you if it's OK to access your documents folder. This is because that is where it will save the web page it generates. Don't worry, it doesn't look at anything else in there.
* A web page will open with a list of words that match your search. Click on the word you want to look at, and it will open the MED page for that word.
* To force the MED page to open in "show quotations" mode, download MED Open Click.user.js and follow the directions in your userscript manager to activate it.

## Things to note about med.py 2.0:
* Unless you use MED Open Click.user.js with a userscript manager, you will have to click the "Show Quotations" button on the MED pages you go to. This is less annoying than it used to be, though, because there is no page reload.
* The search is currently just a simple "headword with alternate spellings" search. I'll add some of the others eventually, maybe.
* If you want a GUI dialog box to enter your search words, grab the version with "g" on the end (e.g. 2.0g), or the Mac app if you have a Mac.
* It is currently coded to save the html to `~/Documents/medresults.html`. You may want to change that if you are running the command line script. It's not yet possible to change it in the Mac app.

med.py uses the BeautifulSoup libraries.

-- Wendi

## Updates

**2.0.1 and 2.0.1g, 2.1 Mac app (11 August 2024):**

2.0.1 is just a minor fix to update a deprecated Beautiful Soup function. 2.1 is the Mac app. The script underlying it is 2.0.1g. The app was built with [Platypus](https://github.com/sveinbjornt/Platypus).

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









   
