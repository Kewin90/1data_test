import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Пример данных: [часы, успеваемость, стресс]
X = np.array([
    [5, 70, 40],  # студент подготовился 5 часов, успеваемость 70, стресс 40
    [3, 50, 80],  # студент подготовился 3 часа, успеваемость 50, стресс 80
    [10, 90, 20], # студент подготовился 10 часов, успеваемость 90, стресс 20
    [1, 40, 90],  # студент подготовился 1 час, успеваемость 40, стресс 90
    [8, 85, 30]   # студент подготовился 8 часов, успеваемость 85, стресс 30
])
# Целевая переменная
y = np.array([1, 0, 1, 0, 1])  # 1 сдаст - 0 не сдаст
# Разделение данных на тренировочные и тестовые выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Создание модели логистической регрессии
model = LogisticRegression()
# Обучение модели
model.fit(X_train, y_train)
# Прогнозирование на тестовых данных
y_pred = model.predict(X_test)
# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy * 100:.2f}%")
# Прогнозирование сдачи экзамена
new_student = np.array([[6, 75, 50]])  # подготовка 6 ч, успеваемость 75, стресс 50
student = model.predict(new_student)
# print(f"Прогноз сдачи экзамена: {'Сдаст' if new_student[0] == 1 else 'Не сдаст'}")
if student[0] == 1:
    print("Сдаст")
else:
    print("Не сдаст")