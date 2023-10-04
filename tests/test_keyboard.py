import pytest
from src.keyboard import Keyboard

def test_keyboard_creation():
    """
    Тест на корректное создание объекта класса Keyboard.
    Проверяются имя клавиатуры и заданный по умолчанию язык.
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)  # Создаем объект класса Keyboard
    assert str(kb) == "Dark Project KD87A"  # Проверяем, что имя корректно инициализировано
    assert str(kb.language) == "EN"  # Проверяем, что язык задан английский по умолчанию


def test_keyboard_change_lang():
    """
    Тест на корректное переключение языка клавиатуры.
    Проверяется работа метода change_lang, переключающего язык между RU и EN.
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)  # Создаем объект класса Keyboard
    kb.change_lang()  # Смена языка
    assert str(kb.language) == "RU"  # Проверяем, что язык изменился на русский
    kb.change_lang()  # Смена языка
    assert str(kb.language) == "EN"  # Проверяем, что язык вернулся на английский


def test_keyboard_change_lang_directly():
    """
    Тест на попытку непосредственного изменения атрибута языка.
    Класс не предполагает прямого изменения атрибута языка - только через
    метод change_lang. Поэтому при попытке прямого присвоения
    значения атрибуту "language" должно возникать исключение AttributeError.
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)  # Создаем объект класса Keyboard
    with pytest.raises(AttributeError):  # Ожидаем исключение
        kb.language = 'CH'  # Попытка непосредственного изменения атрибута "язык"
