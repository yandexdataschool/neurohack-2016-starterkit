# Декодирование состояния испытуемого по ЭЭГ

## Введение

В ходе записи ЭЭГ испытуемый поочередно представлял три состояния: _движение левой рукой_ (`0`), _движение правой рукой_ (`1`) или _находиться в покое_ (`2`). Это целевые состояния, которые нужно научиться распознавать на
основе паттернов ЭЭГ. Необходимо сопоставлять один из трех классов
каждому отсчёту тестовой записи ЭЭГ.

Вам даны размеченные записи сессий ЭЭГ для нескольких испытуемых -
`train.h5`.

```python
import h5py
with h5py.File("train.h5") as train_io:
    for subject_name, subject_data in train_io.items():
        print("Subject %s EEG has %d ticks and %d channels" % (
              subject_name, subject_data["labels"].shape[1],
              subject_data["data"].shape[0]))
        # Please note that in the EEG recording the 0 axis is 
        # channel number, and 1 axis is the tick
```

Кроме этого Вам даны неразмеченные отрезки ЭЭГ с теми же испытуемыми, каждому в каждом отрезке необходимо сопоставить один из трёх классов.

```python
import h5py
with h5py.File("test.h5") as test_io:
    for subject_name, subject_data in test_io.items():
        for chunk_name, chunk_data in subject_data.items():
            print("Chunk %s has %d ticks and %d channels" % (
                  chunk_name, chunk_data.shape[1],
                  chunk_data.shape[0]))
```

Частота оцифровки данных 250 Гц. Названия каналов: `['T5', 'T3', 'F7', 'F3', 'C3', 'P3', 'Fp1', 'Fpz', 'A1', 'O1', 'Cz', 'Oz', 'Fz', 'Pz', 'O2', 'A2', 'Fp2', 'P4', 'C4', 'F4', 'F8', 'T4', 'T6', 'AUX']`.

## Решение

Вам необходимо сформировать файл с предсказаниями в следующем формате:
```
subject_id, chunk_id, tick, class_0_score, class_1_score, class_2_score
```

Пример корректного файла с ответами: `baseline_submission.csv`

## Метрика

Для оценки качества решения будет использоваться усредненная метрика [ROC_AUC](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html) по всем классам (один-против-всех) умноженная на 10^4.

## Дополнительная информация

Названия каналов мнемонически соответствуют расположению электродов на голове испытуемого:
  - электроды слева содержат нечетные номера, электроды справа - нечетные
  - Fp: frontal pole
  - F: frontal
  - C: central
  - T: temporal
  - P: parietal
  - O: occipital

Подробности: http://robertoostenveld.nl/electrode/. 
Координаты расположения электродов для этой задачи находятся в файле `electrode_locations_besa_unit_sphere.mat`.

Каналы `A1`, `A2`, `AUX` не использовались.

Отобразить расположение электродов на голове испытуемого можно:
```python
import scipy.io
import matplotlib.pylab as plt

from mpl_toolkits.mplot3d import Axes3D
%matplotlib notebook

l = scipy.io.loadmat('electrode_locations_besa_unit_sphere.mat')

fig = plt.figure(figsize=(8,6))
ax = fig.gca(projection='3d')
ax.scatter3D(l['x_coord'], l['y_coord'], l['z_coord'])
```
