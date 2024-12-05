def test_function():
    def iner_function():
        print('Я в области видимости функции test_function')
    return iner_function()


test_function()
# iner_function() NameError: name 'iner_function' is not defined. Did you mean: 'test_function'?