## Install & Run ##

Check `python --version` >= 3.5.2

#### Install requirements ####

`pip install -r requirements.txt`

#### Run ####
`python app.py`

#### Call ####
`curl -X PUT http://localhost:5000/simulation/ -F steps=3000`

Positive integers are accepted as `steps` argument.

Result will be stored to `./simulation_result_3000_steps.txt` (according to passed amount of steps).

Success response: `OK`

Error response: error message with non-200 result code

## Testing ##

`cd automata && python -m unittest test_automata.py test_grid.py test_grid_text_dumper.py`

## About ##

#### Assumptions ####

1. Cartesian coordinate system is used (both for task interpretation & output).
2. Grid is stored in memory as a nested hash (grid[y][x]) (simple solution for handling large grids).
3. Grid is stored to file as 0 & 1 rectangle for human-readablity. Whites are '0' and blacks are '1'.
4. Single-threaded server excludes racing for file writes.
5. Test suite covers only general results.

#### Limitations ####

1. Current HTTP-server can handle one request at a time.
2. Grid size is limited with sys.maxsize (as well as with system resources).
3. Python 3 is required (tested against 3.5.2).

#### Potential improvements ####

1. Results can be cached as they are determenistic for any amount of steps (S). Caching stratagy may include saving grid and machine position for certain steps and dynamic computation for intermediate steps.
2. Grid memory representation can be changed to 2-dimentional array (e.g. in C implementation). Actually, it could be a grid of arrays (e.g. array of poiters to arrays) with lazy allocation of reached areas.
3. Areas can also be partially loaded into memory (as simulation is always localized).
4. As computation may take time, asyncronous execution of simulation is preferable.
5. Use multithreaded HTTP-server for production environment. It should be used with thread-safety in mind. Write locks or request joints are required.
6. Other storages could be considered for both caching and storing results.
7. Prepare for deploy: host & port configuration via ENV / dockerization / healthchecks.
8. Visualization of simulation could be added.

## Task ##

Consider an infinite grid of white and black squares. The grid is initially all white and there is a machine in one cell facing right. It will move based on the following rules:

If the machine is in a white square, turn 90° clockwise and move forward 1 unit;
If the machine is in a black square, turn 90° counter-clockwise and move forward 1 unit;
At every move flip the color of the base square.
Implement an application that will receive HTTP PUT requests with a number of steps the simulation should run, always starting from the same conditions, and output the resulting grid to a file.

Please provide support documentation, including your main assumptions, limitations and potential improvements.