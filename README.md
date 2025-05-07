# general-phylomoji: a phylogenetic tree of emoji

Scripts to produce a phylogeny of life forms depicted by emoji.

This project was inspired by https://github.com/ghuertaramos/PlantPhylomoji.

## How To Use

Install the requirements

```shell
pip3 install -r requirements.txt
```

Download emoji sets

```shell
./download_sets.sh
```

Generate phylogenetic trees

```shell
python3 src/make_svg_tree.py
```

## Emoji Details

I decided not to include some ambiguous or species-wise redundant emoji:
* 🌱, could be virtually any dicot plant
* 🌿, sometimes interpreted as fern
* 🍀, same species as ☘, but some interpret it as Marsilea quadrifolia
* 🐂, arguably same species as 🐄
* 🐏, same species as 🐑
* 🐔, same species as 🐓
* 🐩, same species as 🐕
* 🐛, in some depictions a caterpillar, in others various other arthropods, not necessarily insects
* 🥬, ambiguous, either cabbage or lettuce
* 🌴, less ambiguously depicted as 🥥
* 🍏, same species as 🍎
* 🌸, hard to distinguish from 🍒

Face emoji like 🐭 or 🐮 are not included if they have a full-body counterpart.

Some included emoji might be not obvious:
* 🦠 -- bacteria
* 🐦 -- songbirds
* 🧽 -- sponges
* 🚬 -- tobacco
* 🍺 -- hops
* ☕ -- coffee
* 🧉 -- yerba mate
* 🍵 -- tea (Camellia sinensis)
* 🍫 -- cocoa
* 🌼 -- daisy (although depictions in various sets may be different)
* 🫜 -- turnip
