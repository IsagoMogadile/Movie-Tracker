import pandas as pd
from scraper import get_now_showing, get_coming_soon

now_showing = get_now_showing()
coming_soon = get_coming_soon()

df_now_showing = pd.DataFrame(now_showing)
df_coming_soon = pd.DataFrame(coming_soon)

df_now_showing.to_csv("now_showing.csv", index=False)
df_coming_soon.to_csv("coming_soon.csv", index=False)

print(f"Saved {len(df_now_showing)} now showing movies to now_showing.csv")
print(f"Saved {len(df_coming_soon)} coming soon movies to coming_soon.csv")