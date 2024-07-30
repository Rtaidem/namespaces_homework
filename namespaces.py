def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    print(inner_function())

print(test_function())

print(inner_function) # Невозможно вызвать функцию, так как она находится внутри функции test_function
