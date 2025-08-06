# solver.py

import kociemba

def state_to_solver_format(cube_state):
    """
    Converts the cube state from the frontend dictionary
    into a single string format that the kociemba library expects.
    """
    # Map color names to face letters according to the user's orientation
    color_to_face_map = {
        'white': 'U',   # Up
        'green': 'F',   # Front
        'red': 'R',     # Right
        'orange': 'L',  # Left
        'blue': 'B',    # Back
        'yellow': 'D',  # Down
    }

    solver_string = ""
    face_order = ['U', 'R', 'F', 'D', 'L', 'B']
    for face_char in face_order:
        face_colors = cube_state[face_char]
        for color_name in face_colors:
            solver_string += color_to_face_map.get(color_name.lower(), '?')
    return solver_string

def solve_cube(solver_string):
    """
    This function uses the Kociemba library to solve the cube.
    It replaces your original mock_solver function.
    """
    try:
        solution = kociemba.solve(solver_string)
        # The library returns the solution as a single string, e.g., "U F' R2 B'"
        return solution
    except ValueError as e:
        # Kociemba raises a ValueError for invalid cube states
        print(f"Error solving cube: {e}")
        return "Invalid cube state. Please check your colors."