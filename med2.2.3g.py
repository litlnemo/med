#!/Users/litlnemo/aProjects/coding/med/myenv/bin/python

import PySimpleGUI as sg
import os
import requests
from bs4 import BeautifulSoup
import webbrowser
import re

"""med.py: A script for searching the Middle English Dictionary,
   designed for use by those researching Medieval names.
   
   v. 1.0.1, 14 September 2013

   v. 1.0.2, 30 September 2013:
       - added loop, so you can search over and over again
       - custom icon
       - program now closes after you cancel search
       - pages slightly prettier.

   v. 2.0, 8 August 2024:
       - updated for Python 3
       - Pashua removed as it is no longer supported 
       - this means that for now this is command line only, sorry
       - no loop at the moment
       - cannot open pages with full open results... for now
       - last version without GUI dialog box

    v. 2.0G, 10 Aug 2024:
       - PySimpleGUI added
    
    v. 2.1, 11 Aug 2024
       - Standalone Mac app with Platypus
       - changed deprecated "soup.find(text)" to "soup.find(string)"

    v. 2.2G 12 Aug 2024
       - different searches added -- "definition and notes" and "modern English word equivalent"
       - from this point version numbers are intended to match the standalone app
"""

# Search window contents
sg.theme('SystemDefaultForReal')
layout = [  [sg.Text('Enter search word: '), sg.InputText(key='searchword')],
            [[sg.Radio('Headword & forms ', group_id=1, key='hnf', default=True), sg.Radio('Definition & notes ', key='dnn', group_id=1), sg.Radio('Modern English word equivalent', key='mdne', group_id=1)]],
            [sg.Push(), sg.Button('Submit',visible=False, bind_return_key=True)] ]

# Create the Window
window = sg.Window('MED Open Search', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    else:
        search_term = value["searchword"]

        # formatting URL based on chosen type of search
        # headword and forms search

        if value['hnf'] == True:
            url = (
                "https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary?utf8=✓&search_field=hnf&q="
                + search_term
                )
        
        # notes and definitions search

        elif value['dnn'] == True:
            url = (
                "https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary?utf8=✓&search_field=notes_and_def&q="
                + search_term
                )
            
        # modern english word equivalents search

        else:
            url = (
                "https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary?utf8=✓&search_field=oed&q="
                + search_term
                )

        # Get text of search results

        r = requests.get(url)
        page_data = r.text
        soup = BeautifulSoup(page_data, "html.parser")
        count = 0

        # Open file to write to, write HTML for top of page

        file_path = os.path.expanduser("~/Documents/medresults.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(
                "<html>"
                + "\n"
                + '<head><title>Middle English Dictionary open search results</title><base href="http://quod.lib.umich.edu" /><meta charset="UTF-8">'
                + "\n"
                + '<style>li:nth-of-type(odd) { background-color: #fdf0b4; }</style>'
                + "\n"
                + '</head>'
                + "\n"
                + '<body style="font-family: helvetica, arial, sans-serif; margin:0 auto; max-width: 700px; " >'
                + "\n"
                )
            file.write(
                '<h1 style="text-align: center;" width="100%">Middle English Dictionary open search results for the word <span style="font-style: italic">"'
                + str(search_term)
                + '"</span>:</h1>'
                + "\n"
                )
            file.write("<ol>" + "\n")

            # Find relevant links, build LIs with them

            get_urls = soup.find_all("h3", class_="index_title document-title-heading col-md-12")

            if not get_urls:
                print("Error! No results.")
                file.write("<li>" + "\n")
                file.write("Sorry, no results!" + "\n")
                file.write("</li>" + "\n")

            for h3_tag in get_urls:
                # Find the <a> tag inside the <h3>
                link_tag = h3_tag.find("a")

                # If there is no <a> tag, continue to the next h3_tag
                if not link_tag:
                    continue

                # Remove the h3 tag but keep its contents (specifically the <a> tag)
                h3_tag.unwrap()

                # Remove the span with the class "document-counter" if it exists
                span_counter = h3_tag.find("span", class_="document-counter")
                if span_counter:
                    span_counter.decompose()

                file.write('<li style="padding: 10px 0 10px 5px"><b>' + "\n")

                # Find the correct index number in the link
                index_number = re.search(r"MED\d\d\d\d\d", link_tag["href"])

                if index_number:
                    full_url = "https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary/" + index_number.group(0)
                    link_tag["href"] = full_url

                file.write(str(link_tag))
                file.write("</li></b>" + "\n")
                print("Added " + str(count + 1) + " to page")
                count += 1

            # Finish HTML and close 'er up!

            file.write(
                "</ol>"
                + "\n"
                + '<p style="font-size: small; border-top: 1px solid black; margin-top: 10px; padding-top: 15px;">Page generated by MED Open Search. Software &copy; Wendi Dunlap, 2013, 2024. The MED and all search results &copy; University of Michigan. </p></body>'
                + "\n"
                + "</html>"
                )

            html_url = "file://" + file_path
            
            webbrowser.open_new(html_url)

 