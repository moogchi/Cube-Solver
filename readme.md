Django Rubik's Cube Solver क्यूब
This is a web-based Rubik's Cube solver built with Django and three.js. It allows users to input the state of a scrambled 3x3 cube through various methods and provides an animated, step-by-step 3D visualization of the solution.

✨ Features
Interactive 3D Cube: A fully interactive 3D model of the Rubik's Cube rendered using three.js.

Multiple Input Methods:

Manual Input: Click on the stickers in the 3D model to paint the colors of your scrambled cube.

Camera Input: Use your device's camera to capture each face of the cube for automatic color detection.

Text Input: Enter the colors for a face using a simple 9-character string (e.g., Y G O O G R W G B).

Backend Solver: Utilizes the powerful Kociemba's two-phase algorithm via the kociemba-py library to find an efficient solution.

Animated Solution: Watch the solution being performed on the 3D model with step-by-step playback controls (Next, Previous, Auto-Play, Speed).

⚙️ How It Works
The application is split into two main parts: the frontend for user interaction and visualization, and the Django backend for processing and solving.

1. Frontend: Capturing the Cube State (index.html)
The initial page allows you to define the cube's state. The core challenge is translating the visual colors on the 3D model into a structured data format.

Sticker Representation: The 3D cube is composed of 26 "cubies," each with one to three visible "stickers." Every sticker is a three.js mesh with associated user data, including its color and the face it belongs to (e.g., 'U' for Up, 'F' for Front).

Creating the Payload: When you click the "Solve Cube" button, the extractCubeState() JavaScript function runs.

It groups all sticker objects by the face they belong to (U, R, F, D, L, B).

Crucially, for each face, it calls the sortFace() function. This function sorts the 9 stickers of a face into a consistent, predictable order (top-left to bottom-right, relative to a standard cube orientation).

This process generates a JavaScript object that maps each face to an array of its 9 color names.

JavaScript

// Example payload sent to the backend
{
  "U": ["white", "green", "white", "blue", "white", ...],
  "R": ["red", "yellow", "red", "green", "red", ...],
  "F": [...],
  "D": [...],
  "L": [...],
  "B": [...]
}
This JSON object is sent to the Django backend via a POST request.

2. Backend: Solving with Kociemba (solver.py)
The Django backend receives the JSON payload and prepares it for the kociemba library.

The Kociemba "Definition String": Kociemba's algorithm doesn't accept a JSON object. It requires a very specific 54-character "definition string." This string represents all 54 stickers of the cube in a fixed order: Up, Right, Front, Down, Left, Back.

Conversion Process: The state_to_solver_format() function acts as a bridge:

It iterates through the faces in the exact order Kociemba expects: ['U', 'R', 'F', 'D', 'L', 'B'].

For each face, it takes the array of 9 color names (which the frontend already sorted).

It uses a dictionary (color_to_face_map) to convert each color name (e.g., "white") into the character for the face that color belongs on when solved (e.g., 'U').

It concatenates these characters into the final 54-character definition string.

For example, the array ["white", "green", "red", ...] for the Up face becomes the string "UFR...".

Solving: This definition string is passed to kociemba.solve(), which returns the solution as a space-separated string of moves (e.g., U F' R2 B').

3. Frontend: Animating the Solution (solution.html)
The backend redirects the user to the solution page, passing the initial state and the solution moves.

Recreating the Scrambled State: The page first builds the cube in its initial scrambled state using the data provided by the backend.

Animating Moves: The animateMove() function uses tween.js to create smooth animations. For each move (e.g., R'):

It identifies all the cubies belonging to the 'R' (Right) face.

These cubies are temporarily attached to a pivot object.

The pivot is rotated -90 degrees around the X-axis.

After the animation, the cubies are reattached to the main scene, their world positions and rotations now updated.

🚀 Getting Started
To run this project locally, follow these steps.

Prerequisites
Python 3.x

Django

kociemba-py library

Installation
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Set up a virtual environment (recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the Python dependencies:
Create a requirements.txt file with the following content:

Django>=3.2
kociemba
Then install them:

Bash

pip install -r requirements.txt
Run the Django development server:

Bash

python manage.py runserver
Open the application:
Navigate to http://127.0.0.1:8000/ in your web browser.

🛠️ Technologies Used
Backend: Python, Django

Solver: kociemba-py

Frontend: HTML5, CSS3, JavaScript

3D Rendering: three.js

Animation: tween.js






