# news-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/0xbonson/news-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/0xbonson/news-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

The world's news of Thursday 19 November 2026 on one 1024x1024 front page: 36
stories across six continents — three leaders in Shenzhen, Israeli forces in
central Gaza, the biggest IPO in history, the war reaching the Crimea bridge —
drawn as flat vector art with a world map that pins every story to the place it
happened.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The program writes the drawn front page (`entry.png`, a 1024x1024 PNG) to
`$MAKEFUN_OUTPUT_DIR/entry.png`. It reads nothing else and needs no network.

## How it was drawn

- `tools/stories.py` — the day's stories: three leads, nine more with a small
  drawing each, and twenty-four shorter reports, each with its region, its map
  position and the place it happened.
- `tools/build_page.py` — lays the page out as SVG (masthead, leads, cards,
  the "also on" columns) and renders it with headless Chrome to `entry.png`.
- `tools/make_map.py` — draws the world map from Natural Earth country borders
  and prints the numbered pin of every story on it.

Rebuild the image with `python3 tools/make_map.py && python3 tools/build_page.py`.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=kewdhhyh&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
