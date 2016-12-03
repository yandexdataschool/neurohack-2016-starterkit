#!/bin/sh

HERE=$(dirname $0)

curl https://transfer.sh/TWT1i/train-online.h5 -o $HERE/task_1/train-online.h5
curl https://transfer.sh/QhLb8/train.h5 -o $HERE/task_2/train.h5
curl https://transfer.sh/KY6kZ/test.h5 -o $HERE/task_2/test.h5
curl https://transfer.sh/14KC71/train.h5 -o $HERE/task_3/train.h5
curl https://transfer.sh/ytgtR/test.h5 -o $HERE/task_3/test.h5
