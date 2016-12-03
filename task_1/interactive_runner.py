import sys
import subprocess
import numpy as np
import h5py
from sklearn.metrics import mean_squared_error


def interact(test_file, experiment_id, solution_file, runner, out_file):
    SKIP_SIZE = 28
    OFFSET = 3000
    TARGET_CHANNEL = 15


    with h5py.File(test_file) as data_file:
        data = np.array(data_file[experiment_id])
    
    solution = subprocess.Popen([runner, solution_file], 
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE, 
                                universal_newlines=True)
    
    solution.stdin.write(experiment_id + '\n')

    solution.stdin.write('\n'.join(' '.join(map(str, data[i])) for i in range(OFFSET)) + '\n')


    prediction = []
    with open(out_file, 'w') as prediction_file:
        solution.stdin.flush()
        stdout = solution.stdout.readline()
        prediction.append(float(stdout))
        prediction_file.write(stdout)

        for i in range(OFFSET, len(data) - SKIP_SIZE):
            solution.stdin.write(' '.join(map(str, data[i])) + '\n')
            solution.stdin.flush()
            stdout = solution.stdout.readline()
            prediction.append(float(stdout))
            prediction_file.write(stdout)

    solution.kill()

    prediction = np.array(prediction)
    target = data[OFFSET + SKIP_SIZE - 1:, TARGET_CHANNEL]
    mse_score = mean_squared_error(target, prediction)
    print('MSE score {}'.format(mse_score))


if __name__ == '__main__':
    interact(test_file=sys.argv[1], experiment_id=sys.argv[2], solution_file=sys.argv[3], runner=sys.argv[4], out_file=sys.argv[5])
