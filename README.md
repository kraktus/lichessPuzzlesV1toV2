# Convert puzzle V1 index to puzzle V2 

The [`index_conversion.csv`](https://github.com/kraktus/lichessPuzzlesV1toV2/blob/master/index_conversion.csv) contains the list of all old puzzles that have an equivalent after the puzzle V2 update. This file will be updated along with the puzzle V2 db.

The converter is intentionally loose (just checking that both puzzles have the same starting position), since puzzle V2 generator ensure that there's only one winning move for the side to play. The moves played by the opponent may vary, but the tactical idea of the puzzle will likely stay the same.

## Stats

Currently about 12% of the old puzzles (puzzles V1 with index ≥ 61053) and 1% of the very old puzzles (puzzles "V0" with index < 61053, on lichess prior to 2015) were re-generated.

## Run it

Download the puzzle V2 database [here](https://database.lichess.org/#puzzles) and save it in the current directory (make sure the file is still named `lichess_db_puzzle.csv`).

Download the puzzle V1 [here](https://database.lichess.org/puzzlesv1/), then run `mongorestore -d old_puzzle -c puzzle puzzle.bson` in the command line. You need to have `mongodb` (>= 4.0) installed and running.

Install the python dependencies (`pip3 install -r requirements.txt`)
