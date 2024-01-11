from typing import Literal
import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

@pytest.mark.parametrize( 'text, result', [ 
    ('skypro', 'Skypro'), # латиница
    ('скайпро', 'Скайпро'), # кириллица
    ('SKYPRO', 'Skypro'), # все заглавные
    ('123', '123'), # числа
    ('skypro super', 'Skypro super'), #два слова
    ('skypro-super', 'Skypro-super'), #слово через дефис
    ('№;№@:?*', '№;№@:?*'), #спецсимволы
    ('h', 'H'), # одна буква
    ('', ''), # пустая строка
    (' ', ' '), # пробелы
    ] )
def test_capitilize_positive(text, result):
    cstringUtils = StringUtils()
    res = cstringUtils.capitilize(text)
    assert res == result

#негативный тест с None
def test_capitilize_negative_None():
    cstringUtils = StringUtils()
    with pytest.raises(AssertionError):
        cstringUtils.capitilize(None)
    
     
@pytest.mark.parametrize( 'text, result', [ 
    (' skypro', 'skypro'), # пробел в начале
    (' 111', '111'), # пробел перед цифрами
    (' skypro skypro', 'skypro skypro'), # пробел перед двуями словами
    ('     sky', 'sky'), # несколько пробелов
    (' скайпро', 'скайпро'), #пробел перед кириллицей
    ('скайпро', 'скайпро'), # нет пробела
    ('', ''), # пустая строка
    ('     ', ''), # строка из пробелов
    ] )
def test_trim_positive(text, result):
    cstringUtils = StringUtils()
    res = cstringUtils.trim(text)
    assert res == result

@pytest.mark.parametrize( 'text, delimeter, result', [ 
    ("a,b,c,d", ",", ["a", "b", "c", "d"]), # буквы и запятая
    ("a,b,3,4", ",", ["a", "b", "3", "4"]), # буквы, цифры и запятая
    ("a.b.c.d", ".", ["a", "b", "c", "d"]), # буквы и точка
    ("1.2.3.4", ".", ["1", "2", "3", "4"]), # цифры и точка
    ("a:b:c:d", ":", ["a", "b", "c", "d"]), # буквы и двоеточие
    ("1:2:3:4", ":", ["1", "2", "3", "4"]), # цифры и двоеточие
    ("1,2,3,4", ",", ["1", "2", "3", "4"]), # цифры и запятая
    ("#:$:%:&", ":", ["#", "$", "%", "&"]), # спецсимволы и двоеточие
    ("ц;ф;м;к;д", ";", ["ц", "ф", "м", "к", "д"]), # кириллица и точка с запятой
    ("", ";", []), # пустой список
    ("   ", ";", []), # список с пробелами
    ] )
def test_to_list_positive(text, delimeter, result):
    cstringUtils = StringUtils()
    res = cstringUtils.to_list(text, delimeter)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [ 
    ("SkyPro", "S", True), # буква есть
    ("SkyPro", "U", False), # буквы нет
    ("1234", "3", True), # цифра есть
    ("12345", "8", False), # цифры нет
    ("Sky Pro", " ", True), # пробел есть
    ("Sky-Pro", "-", True), # спецсимвол есть
    ("", "-", False), # пустая строка
    ("  ", " ", True), # строка из пробелов
    ] )
def test_contains_positive(string, symbol, result):
    cstringUtils = StringUtils()
    res = cstringUtils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [ 
    ("SkyPro", "k", "SyPro"), # один символ удаляем
    ("SkyPro", "Pro", "Sky"), # несколько символов удаляем
    ("SkyPro", "SkyPro", ""), # все символы удаляем
    ("SkyPro", "T", "SkyPro"), # символов нет таких
    ("SkyPro ", " ", "SkyPro"), # удаляем пробел
    ("SkyPro", "", "SkyPro"), # ничего не удаляем
    ("", "", ""), # пустые строки
    (" ", " ", ""), # удаляем пробел
    ("", "y", ""), # удаляем символ, которого нет, из пустой строки
    ] )
def test_delete_symbol_positive(string, symbol, result):
    cstringUtils = StringUtils()
    res = cstringUtils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [ 
    ("SkyPro", "S", True), # строка начинается с заданного символа
    ("SkyPro", "P", False), # строка не начинается с заданного символа
    ("12345", "1", True), # строка из чисел начинается с заданного символа
    (" adada", " ", True), # строка начинается с пробела
    ("SkyPro ", "u", False), # строка не имеет данного символа
    ("      ", " ", True), # строка из пробелов
    ("", "", True), # пустая строка
    ] )
def test_starts_with_positive(string, symbol, result):
    cstringUtils = StringUtils()
    res = cstringUtils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [ 
    ("SkyPro", "o", True), # строка заканчивается на заданный символ
    ("SkyPro", "y", False), # строка не заканчивается на заданный символ
    ("12345", "5", True), # строка из чисел заканчивается на заданный символ
    ("adada ", " ", True), # строка заканчивается на пробел
    ("SkyPro", "u", False), # строка не имеет данного символа
    ("      ", " ", True), # строка из пробелов
    ("", "", True), # пустая строка
    ] )
def test_end_with_positive(string, symbol, result):
    cstringUtils = StringUtils()
    res = cstringUtils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, result', [ 
    ("", True), # строка пустая
    ("  ", True), # строка с пробелами
    ("12345", False), # строка из чисел
    ("adada", False), # строка из букв
    ("##$%^&*", False), # строка из спецсимволов
    ] )
def test_is_empty_positive(string, result):
    cstringUtils = StringUtils()
    res = cstringUtils.is_empty(string)
    assert res == result

@pytest.mark.parametrize( 'list, joiner, result', [ 
    ([1,2,3,4], ",", "1,2,3,4"), # цифры и запятая
    (["Sky","Pro"], ",", "Sky,Pro"), # буквы и запятая
    (["a","b","3","4"], ",", "a,b,3,4"), # буквы, цифры и запятая
    (["a","b","c","d"], ".", "a.b.c.d"), # буквы и точка
    ([1,2,3,4], ".", "1.2.3.4"), # цифры и точка
    (["a","b","c","d"], ":", "a:b:c:d"), # буквы и двоеточие
    ([1,2,3,4], ":", "1:2:3:4"), # цифры и двоеточие
    (["#","$","%","&"], "-", "#-$-%-&"), # цифры и тире
    (["ц","ф","м","к","д"], ";", "ц;ф;м;к;д"), # кириллица и точка с запятой
    ([], ",", ""), # пустой список
    ] )
def test_list_to_string(list, joiner, result):
    cstringUtils = StringUtils()
    res = cstringUtils.list_to_string(list, joiner)
    assert res == result