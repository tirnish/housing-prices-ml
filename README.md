# House Prices - Regression

Проект по прогнозированию стоимости жилых домов на основе данных соревнования [Housing Prices Competition for Kaggle Learn Users](https://www.kaggle.com/competitions/home-data-for-ml-course).

## Цель проекта

Предсказать цену продажи (`SalePrice`) для каждого объекта из тестовой выборки.

Основная цель проекта - отработать полный pipeline решения задачи регрессии на табличных данных с большим количеством числовых и категориальных признаков.

## Данные

Исходный датасет содержит следующие файлы:

* `train.csv` - тренировочная выборка, содержащая признаки объектов и целевую переменную `SalePrice`;
* `test.csv` - тестовая выборка без целевой переменной;
* `data_description.txt` - описание признаков;
* `sample_submission.csv` - пример формата submission.

Целевая переменная:

`SalePrice` - цена продажи дома.

## Метрика

В соревновании используется RMSE между логарифмами предсказанной и фактической цены:

`RMSE(log1p(y_pred), log1p(y_true))`

Логарифмическое преобразование снижает влияние объектов с экстремально высокой стоимостью.

## Инструменты

* Python 3.11
* pandas
* NumPy
* scikit-learn
* XGBoost
* Jupyter Notebook
* Git

Зависимости проекта зафиксированы в `requirements.txt`.

Для изоляции зависимостей используется виртуальное окружение `.venv`.

## Структура проекта

```text
housing-prices-ml/
│
├── data/
│   ├── raw/             # исходные данные
│   └── result/          # итоговый файл для Kaggle
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_baseline.ipynb
│   └── 03_modeling.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

Описание notebooks:

* `01_eda.ipynb` - исследование структуры данных, пропусков, типов признаков и их связи с целевой переменной;
* `02_baseline.ipynb` - построение baseline-модели и оценка её качества с использованием кросс-валидации;
* `03_modeling.ipynb` - эксперименты с preprocessing, моделями и подбором гиперпараметров.

## Подход

В качестве baseline используется `DecisionTreeRegressor`.

Деревья решений позволяют построить простой baseline с минимальными требованиями к масштабированию числовых признаков и подготовке данных.

Для preprocessing используются:

* заполнение пропущенных значений;
* обработка отсутствующих категорий;
* кодирование категориальных признаков с помощью `OneHotEncoder`;
* `Pipeline` и `ColumnTransformer` для объединения этапов preprocessing и обучения модели.

Качество моделей оценивается с помощью кросс-валидации.

Для улучшения baseline рассматриваются:

* Decision Tree;
* Random Forest;
* Gradient Boosting;
* XGBoost.

Подбор гиперпараметров выполняется с помощью `RandomizedSearchCV`.

## Результаты

Baseline:

`Decision Tree - CV RMSE: 0.20 ± 0.02`

Наилучший результат на публичном leaderboard Kaggle показала модель `GradientBoostingRegressor`.

Результат:

`GradientBoostingRegressor - CV RMSE: 0.13 ± 0.01`

## Итог

В проекте реализован полный pipeline решения задачи табличной регрессии:

**EDA → preprocessing → baseline → cross-validation → подбор гиперпараметров → обучение финальной модели → Kaggle submission**