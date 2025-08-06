from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
import json
from .solver import solve_cube, state_to_solver_format

def index(request):
    """
    Renders the cube configuration page.
    """
    return render(request, 'cube_solver/index.html')

def solve_cube_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cube_state_dict = data.get('state')
            
            if not cube_state_dict:
                return JsonResponse({'status': 'error', 'error': 'No cube state provided.'})

            solver_string = state_to_solver_format(cube_state_dict)
            solution_string = solve_cube(solver_string)

            if "Invalid cube state" in solution_string:
                return JsonResponse({
                    'status': 'error', 
                    'error': solution_string,
                    'definition_string': solver_string
                })
            
            request.session['initial_cube_state'] = cube_state_dict
            request.session['solution_str'] = solution_string
            request.session['definition_string'] = solver_string 
            
            request.session.save()
            
            return JsonResponse({'status': 'success', 'redirect_url': reverse('cube_solver:solution_steps')})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)})

    return JsonResponse({'status': 'error', 'error': 'Invalid request method.'})

def solution_steps(request):
    solution_str = request.session.get('solution_str', 'No solution found.')
    initial_state_dict = request.session.get('initial_cube_state', {})
    definition_string = request.session.get('definition_string', 'Definition string not found.')
    
    solution = solution_str.split()
    initial_state_json = json.dumps(initial_state_dict)
    
    context = {
        'solution_str': solution_str,
        'solution': solution,
        'initial_state_json': initial_state_json,
        'definition_string': definition_string,
    }
    
    return render(request, 'cube_solver/solve_page.html', context)