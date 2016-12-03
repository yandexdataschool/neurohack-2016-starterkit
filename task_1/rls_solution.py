import numpy as np
import sys
from collections import deque

if sys.version_info.major == 2:
    input = raw_input

OFFSET = 3000
SKIP_SIZE = 28
TARGET_CHANNEL = 15
N_CHANNELS = 21

experiment_id = input()


class DelayedRLSPredictor:
    def __init__(self, n_channels, M=3, lambda_=0.999, delta=100, delay=0, mu=0.3):
        self._M = M
        self._lambda = lambda_
        self._delay = delay
        self._mu = mu
        size = M * n_channels
        self._w = np.zeros((size,))
        self._P = delta * np.eye(size)
        self.regressors = deque(maxlen=M + delay + 1)

    def predict(self, sample):
        self.regressors.append(sample)
        regressors = np.array(self.regressors)
        if regressors.shape[0] > self._delay + self._M:
            # predicted var x(t)
            predicted = regressors[-1, TARGET_CHANNEL]

            # predictor var [x(t - M), x(t - M + 1), ..., x(t - delay)]
            predictor = regressors[- self._M - self._delay - 1: - self._delay - 1].flatten()  #

            # update helpers
            pi = np.dot(predictor, self._P)
            k = pi / (self._lambda + np.dot(pi, predictor))
            self._P = 1 / self._lambda * (self._P - np.dot(k[:, None], pi[None, :]))

            # update weights
            dw = (predicted - np.dot(self._w, predictor)) * k
            self._w = self._w + self._mu * dw

            # return prediction x(t + delay)
            return np.dot(self._w, regressors[- self._M:].flatten())

        # if lenght of regressor less than M + delay + 1 return 0
        return 0


rls = DelayedRLSPredictor(n_channels=N_CHANNELS, M=3, lambda_=0.9999, delta=0.01, delay=SKIP_SIZE, mu=1)

for i in range(OFFSET):
    cur_data = list(map(float, input().split()))
    prediction = rls.predict(cur_data)

print(prediction)
sys.stdout.flush()

while True:
    cur_data = list(map(float, input().split()))
    prediction = rls.predict(cur_data)
    print(prediction)
    sys.stdout.flush()


