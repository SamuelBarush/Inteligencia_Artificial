import random

def test_Train_Test():
    # Crear una instancia de la clase KNN
    knn = KNN()

    # Crear un conjunto de datos de ejemplo
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

    # Definir el porcentaje de datos para entrenamiento
    porcentaje = 0.8

    # Ejecutar la función Train_Test
    train = knn.Train_Test(data, porcentaje)

    # Verificar que el conjunto de entrenamiento tenga la longitud esperada
    assert len(train) == int(len(data) * porcentaje)

    # Verificar que cada elemento del conjunto de entrenamiento sea una tupla de dos elementos
    for item in train:
        assert isinstance(item, tuple)
        assert len(item) == 2

        # Verificar que cada elemento de la tupla sea un par de valores
        assert isinstance(item[0], int)
        assert isinstance(item[1], int)

    print("Pruebas pasadas con éxito")

# Ejecutar las pruebas
test_Train_Test()