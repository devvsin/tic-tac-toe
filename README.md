# Flask Tic Tac Toe

A modern, interactive web-based implementation of the classic Tic Tac Toe game built with Flask and enhanced with sleek animations and a glassmorphism design.

![Tic Tac Toe Game](https://raw.githubusercontent.com/devvsin/tic-tac-toe/main/Screenshot.png)

## Features

- 🎮 Classic Tic Tac Toe gameplay
- 🎨 Modern glassmorphism UI design
- ✨ Smooth animations and transitions
- 📱 Responsive layout for all devices
- 🔄 Session-based game state management
- 🎯 Real-time win/draw detection
- 🔄 Instant game reset functionality

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3
- **State Management**: Flask Sessions
- **Design**: Custom CSS with modern design principles

## Installation

1. Clone the repository
```bash
git clone https://github.com/devvsin/tic-tac-toe.git
cd flask-tic-tac-toe
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install flask
```

4. Run the application
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
flask-tic-tac-toe/
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── game.html      # Game interface
├── README.md          # Project documentation
└── requirements.txt   # Project dependencies
```

## Game Rules

1. The game is played on a 3x3 grid
2. Players alternate placing X's and O's on the board
3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) wins
4. When all 9 squares are full and no player has won, the game is a draw

## Features in Detail

### Backend
- Secure session management for game state
- Efficient win detection algorithm
- Clean route organization
- Error handling for invalid moves

### Frontend
- Intuitive user interface
- Visual feedback for player actions
- Responsive design for all screen sizes
- Smooth animations and transitions
- Modern glassmorphism design style





## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by classic Tic Tac Toe games
- Modern UI design principles
- Flask framework documentation

## Contact


Project Link: [https://github.com/devvsin/tic-tac-toe](https://github.com/devvsin/tic-tac-toe)
