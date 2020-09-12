import requests
import json
import chess
import chess.svg
from datetime import datetime

USERNAME = 'agrnet'

if __name__ == '__main__':
    year = datetime.now().year
    month = datetime.now().month
    resp = requests.get('https://api.chess.com/pub/player/%s/games/%d/%02d' % (USERNAME, year, month))

    fen = ''
    for obj in json.loads(resp.text)['games']:
        if USERNAME == obj['white']['username']:
            if obj['white']['result'] == 'win':
                fen = obj['fen']
                break

        elif USERNAME == obj['black']['username']:
            if obj['black']['result'] == 'win':
                fen = obj['fen']
                break

    board = chess.Board(fen)
    img = chess.svg.board(board)
    with open('wgame.svg', 'w') as outfile:
        outfile.write(img)
