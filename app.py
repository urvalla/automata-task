from automata import Grid, MachineRotation, Automata, GridTextDumper
from flask import Flask, request
import json

app = Flask(__name__)

HTTP_UNPROCESSIBLE_ENTITY_STATUS_CODE = 422

@app.route('/simulation/', methods=['PUT'])
def simulation():
    steps = int(request.form.get('steps', 0))

    # validate
    if steps < 1:
        return 'Positive number of steps is expected', HTTP_UNPROCESSIBLE_ENTITY_STATUS_CODE

    # init
    machine_rotation = MachineRotation()
    grid = Grid()
    automata = Automata(grid=grid, machine_rotation=machine_rotation)

    # run simulation
    for i in range(steps):
        automata.step()

    dumper = GridTextDumper(grid)
    dump_result = dumper.dump()

    dims_x, dims_y = grid.get_dims()

    # write to file
    f = open("simulation_result_"+str(steps)+"_steps.txt", "w")
    f.write("x: [%d..%d]" % dims_x + " pos: %d" % automata.pos_x + "\n")
    f.write("y: [%d..%d]" % dims_y + " pos: %d" % automata.pos_y + "\n")
    f.write("rotation: %s" % {0: "top", 1: "right", 2: "bottom", 3: "left"}[machine_rotation.rotation] + "\n\n")
    
    f.write(dump_result)
    f.close()

    return "OK"+str(steps)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)