#!/usr/local/bin/python3
#coding: utf-8

"""
Convert old indexes to new ones, if they exist.
"""

import csv
import pymongo

from typing import Dict

#############
# Functions #
#############

def fen_without_move(fen: str) -> str:
    """
    Remove the parts of the fen relative to moves (for 50-move rule and nb of moves of the game)
    """
    # fen ex: rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1
    return " ".join(fen.split()[:-2])

def get_new_id_by_fen() -> Dict[str, str]:
    new_id_by_fen: Dict[str, str] = {}
    #Fields for the new db: PuzzleId,FEN,Moves,Rating,RatingDeviation,Popularity,NbPlays,Themes,GameUrl
    with open('lichess_db_puzzle.csv', newline='') as csvfile:
        puzzles = csv.reader(csvfile, delimiter=',', quotechar='|')
        for puzzle in puzzles:
            new_id_by_fen[fen_without_move(puzzle[1])] = puzzle[0]
    return new_id_by_fen

def get_old_puzzle_coll() -> "pymongo.collection":
    client = pymongo.MongoClient()
    db = client.old_puzzle
    return db.puzzle

def main():
    with open('index_conversion.csv', 'w', newline='') as csvfile:
        fieldnames = ['old_index', 'new_index']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        new_index_dic = get_new_id_by_fen()
        coll = get_old_puzzle_coll()
        for i in range(1, 125273):
            old_puzzle = coll.find_one({"_id": i})
            if old_puzzle is None: #removed from the db
                continue
            fen = old_puzzle.get("fen")
            if fen is None: #corrupted puzzle
                print(old_puzzle)
                continue       
            if (new_index := new_index_dic.get(fen_without_move(fen))) is not None:
                writer.writerow({'old_index': i, 'new_index': new_index})

########
# Main #
########

if __name__ == "__main__":
    print('#'*80)
    main()



