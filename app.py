# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)


def check_winner(board):
    """
    Check if there's a winner or if the game is a draw
    Returns: (winner, winning_cells) tuple where:
    - winner is 'X' or 'O' for winner, 'Draw' for draw, None if game is ongoing
    - winning_cells is a list of (row, col) tuples indicating the winning combination
    """
    # Check rows
    for i, row in enumerate(board):
        if len(set(row)) == 1 and row[0] != '':
            return row[0], [(i, 0), (i, 1), (i, 2)]
    
    # Check columns
    for i in range(3):
        if len(set(board[row][i] for row in range(3))) == 1 and board[0][i] != '':
            return board[0][i], [(0, i), (1, i), (2, i)]
    
    # Check main diagonal
    if len(set(board[i][i] for i in range(3))) == 1 and board[0][0] != '':
        return board[0][0], [(0, 0), (1, 1), (2, 2)]
    
    # Check secondary diagonal
    if len(set(board[i][2-i] for i in range(3))) == 1 and board[0][2] != '':
        return board[0][2], [(0, 2), (1, 1), (2, 0)]
    
    # Check for draw
    if all(cell != '' for row in board for cell in row):
        return 'Draw', []
    
    return None, []

@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = [['', '', ''] for _ in range(3)]
        session['current_player'] = 'X'
        session['winning_cells'] = []
    return render_template('game.html', 
                         board=session['board'], 
                         current_player=session['current_player'],
                         winning_cells=session['winning_cells'])

@app.route('/play/<int:row>/<int:col>')
def play(row, col):
    if session['board'][row][col] == '':
        # Make the move
        session['board'][row][col] = session['current_player']
        
        # Check for winner
        winner, winning_cells = check_winner(session['board'])
        
        if winner:
            session['winning_cells'] = winning_cells
            if winner == 'Draw':
                return render_template('game.html', 
                                     board=session['board'],
                                     winning_cells=session['winning_cells'],
                                     message="It's a draw!",
                                     show_reset=True)
            else:
                return render_template('game.html', 
                                     board=session['board'],
                                     winning_cells=session['winning_cells'],
                                     message=f"Player {winner} wins!",
                                     show_reset=True)
        
        # Switch players
        session['current_player'] = 'O' if session['current_player'] == 'X' else 'X'
        session.modified = True
    
    return render_template('game.html', 
                         board=session['board'], 
                         current_player=session['current_player'],
                         winning_cells=session.get('winning_cells', []))

@app.route('/reset')
def reset():
    session['board'] = [['', '', ''] for _ in range(3)]
    session['current_player'] = 'X'
    session['winning_cells'] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)