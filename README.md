# Nu Metro Movie Tracker
 
A Python scraper that pulls the current "Now Booking" and "Coming Soon" movie
listings from [numetro.co.za](https://numetro.co.za), and saves them to CSV
files for easy viewing.

## What it does
 
**Now Booking** — fetched directly from Nu Metro's internal JSON API
  (`/api/?movies=true&cinema=`), which returns structured data with no HTML
  parsing required.
**Coming Soon** — this page has no equivalent API endpoint, so it's scraped
  from the server-rendered HTML instead, using BeautifulSoup to pull out each
  movie's title, genre, runtime, age rating, and release date.
Both lists are tagged with the standard regular ticket price (R79), since
  Nu Metro doesn't attach pricing to individual movies pricing is flat
  across all films.