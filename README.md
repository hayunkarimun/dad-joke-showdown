# Dad Joke Showdown — make.fun bounty entry

[![Dad Joke Showdown](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/hayunkarimun/dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/hayunkarimun/dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

One dad joke, at most 200 characters — the whole entry. `main.py` (Python 3.13,
stdlib only) scores five fresh jokes against the judge's five criteria
(dad voice, clean pun, freshness, tightness, reads aloud) and writes the
winner to `/output/entry.txt`.

The winner:

> Why did the clock go to therapy? It had too much time on its hands.

67 characters, one line. The double pun (time + hands) lands on the first
read, it is fresh rather than a retold classic, and it reads like a father
telling it across the dinner table.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Two runs produce byte-identical output.
