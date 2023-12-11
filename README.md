# mario-rpg-remake
Actions parser for mario RPG remake


## How to use
Execute `python simplified.py <input file>` to create a 'simplified' json which you can more easily edit. This json will not deal with the key ids in the map so it's easier to add element.

Once you are done adding/changing elements, run `python rebuild.py <simplied input json file` to create an input file in the same format as the original but with your changes.