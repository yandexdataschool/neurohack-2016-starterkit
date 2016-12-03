# Анализ ЭМГ

## Введение

Проводились следующие эксперименты: испытуемый писал на планшете цифры, параллельно с этим работа мышц его руки считывалась при помощи [электромиографии](https://en.wikipedia.org/wiki/Electromyography). Вам
даны записи сессий - сигналы электромиографа и координаты пера. Ваша задача - построить алгоритм, который бы предсказывал координаты пера (X, Y) по сигналам электромиографа и отправить на проверку предсказанные траектории для тестовой выборки. Набор символов в тестовой и тренировочной выборках - разный.

```python
import h5py
with h5py.File("train.h5") as train_io:
    for subject_name, subject_data in train_io.items():
        for digit, digit_data in subject_data.items():
            for trial_name, trial_data in digit_data.items():
                print(subject_name, digit, trial_name)
                print("EMG ticks %d, EMG channels %d" %
                      trial_data['emg'].shape)
                print("Coordinates ticks: %d, dimensions: %d (x, y)" %
                      trial_data['pen_coordinates'].shape)
```

```python
import h5py
with h5py.File("test.h5") as train_io:
    for subject_name, subject_data in train_io.items():
       for trial_name, trial_data in subject_data.items():
           print(subject_name, trial_name)
           print("EMG ticks %d, EMG channels %d" %
                 trial_data.shape)
```

## Метрика

Для проверки качества Вашего алгоритма вычисляется [коэффициент корреляции Пирсона](https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient) между скоростью пера и предсказанной скоростью пера по координатам X и Y, затем сумма этих коэффициентов делится на 2. Значения этих величин усредняются по всем цифрам тестового набора и результат умножается на 10^4.

```python
def score_trial(true_coordinates, predicted_coordinates, dimensions=2):
	return numpy.mean([pearsonr(
		numpy.diff(true_coordinates[:, axis]),
	    numpy.diff(predicted_coordinates[:, axis]))[0] 
		for axis in range(dimensions)])

```

## Решение

Формат файла решения:
```
subject_id,trial_id,tick_index,x,y
```

Подробнее про задачу и baseline можно почитать в [статье](http://journal.frontiersin.org/article/10.3389/fnins.2015.00389/full)
