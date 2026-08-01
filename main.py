#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

REGULAR_TICKET_PRICE = "R 79"


def get_now_showing():
    url = "https://numetro.co.za/api/?movies=true&cinema="
    headers = {"User-Agent": "Mozilla/5.0 (educational scraping project)"}
    response = requests.get(url, headers=headers)
    movies = response.json()

    results = []
    for m in movies:
        results.append({
            "title": m["title"],
            "genres": m["genres"],
            "running_time": m["running_time"],
            "age_restriction": m["age_restriction"],
            "price": REGULAR_TICKET_PRICE
        })
    return results


def get_coming_soon():
    url = "https://numetro.co.za/coming-soon/"
    headers = {"User-Agent": "Mozilla/5.0 (educational scraping project)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    movie_blocks = soup.select("div.movie_item")
    results = []
    for block in movie_blocks:
        title_el = block.select_one("h4.orange")
        title = title_el.get_text(strip=True) if title_el else None

        details_el = block.select_one("p.movie-details")
        details_text = details_el.get_text(" ", strip=True) if details_el else ""

        results.append({
            "title": title,
            "details": details_text,
            "price": REGULAR_TICKET_PRICE
        })
    return results


if __name__ == "__main__":
    now_showing = get_now_showing()
    coming_soon = get_coming_soon()

    pd.DataFrame(now_showing).to_csv("now_showing.csv", index=False)
    pd.DataFrame(coming_soon).to_csv("coming_soon.csv", index=False)

    print(f"Saved {len(now_showing)} now showing movies to now_showing.csv")
    print(f"Saved {len(coming_soon)} coming soon movies to coming_soon.csv")
