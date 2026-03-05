# TODO make if with pip install -e .

# [DONE] Раннее тестирование позволяет сэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не отсутсвие

# [DONE] Тесты не должны дублировать логику тестируемого кода
# и не делать предположений о внутреннем устройстве кода

# [DONE] Тесты не должны использовать ВСЕ наборы входных параметров
# [DONE] Тесты должны покрывать "кластеры" входных параметров
# [DONE] Тестовые функции должны тестировать логические блоки

# Тесты должны обнаруживать новые ошибки, использование
# одних и тех же типов может препятсвовать этому 
# (pescicide paradox)

# Тесты покрывают как успешные, так и ошибочные кейсы

from math_demo import (add, add_with_bug, calclate_tax_bugged, calclate_tax)

def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test ADDITION PASSED")

def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не их отсутствие
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    print("Test ADDITION PASSED")

    # finally we found data that make test reliable
    # assert add_with_bug(7, 6) == 13 # will fail here

def test_addition_duplicat():
    assert add(6, 7) == 6 + 7
    print("Test DUPLICATE ADDITION PASSED")

def test_addition_overkill():
    for i in range(0, 2 ** 32):
        for j in range(0, 2 ** 32):
            assert add(i, j) == i + j # violation of duplication
            assert add(-i, j) == -i + j
            assert add(-i, -j) == -i - j
            assert add(i, -j) == i - j

def test_addition_clussters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    print("Test CLUSTERS PASSED")

def test_addition_commutative():
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("Test COMMUTATIVE PASSED")

def test_tax_calclator_pesticide():
    assert calclate_tax_bugged(1000) == 150
    assert calclate_tax_bugged(100) == 15
    assert calclate_tax_bugged(10) == 1.5
    assert calclate_tax_bugged(1) == 0.15
    assert calclate_tax_bugged(234) == 35.1
    print("Test TAX CALCULATOR PASSED")
    # float may give us test cases
    # not available when using int
    # assert calclate_tax_bugged(2.34) == 0.35 # 0.351

def test_tax_calculartor():
    assert calclate_tax(1000) == 150
    assert calclate_tax(100) == 15
    assert calclate_tax(10) == 1.5
    assert calclate_tax(1) == 0.15
    assert calclate_tax(234) == 35.1
    assert calclate_tax(2.34) == 0.35 # 0.351
    print("Test UNBUGGED TAX CALCULATOR PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicat()
    # test_addition_overkill() # can try it on your risk
    test_addition_clussters()
    test_addition_commutative()
    test_tax_calclator_pesticide()
    test_tax_calculartor()