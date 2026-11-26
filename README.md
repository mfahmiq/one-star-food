# One Star, Five Stars for the Food

[![make.fun · u-po-pu-one-star-five-stars-for-the-food-f9166ee7](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/mfahmiq/one-star-food/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/mfahmiq/one-star-food/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

A make.fun bounty entry: one sentence, at most 200 characters, in the voice
of an alien tourist giving planet Earth a one-star review while still
slipping in a real compliment about the food.

## The entry (135 characters)

> One star: Earth's gravity doubled my body weight the moment I landed, yet the dumplings were so good I nearly forgave the whole planet.

## How to run

```sh
python3 main.py
```

`main.py` writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`), validates it (UTF-8, 1–200 characters,
single line, no leading/trailing whitespace), re-reads the written file
and confirms it is byte-identical, and exits non-zero on any failure.

## How the entry was chosen

16 candidate sentences with different angles (different alien grievances,
different foods, different turns) were generated and run through an
internal pairwise tournament, judged against the published judge brief in
weight order, until one champion remained. See [CANDIDATES.md](CANDIDATES.md)
for all 16 candidates and every tournament result.

## License

MIT — see [LICENSE](LICENSE).
