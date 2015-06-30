# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://abs.gov.au/AUSSTATS/abs@.nsf/mf/1345.0")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)


root.cssselect("tr valign="top"")
    record={}
    record["indicator"]=td[0].text_content()
    record["pub"]=td[1].text_content()
    record["period"]=td[2].text_content()
    record["unit"]=td[3].text_content()
    record["value"]=td[4].text_content()
    record["changeyr"]=td[6].text_content()
    scraperwiki.sqlite.save(unique_keys=['indicator'], data=record)

#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
