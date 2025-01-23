"""
    Дополните приведенный ниже код так, чтобы в переменной result хранился
    словарь, в котором для каждого символа строки text будет подсчитано
    количество его вхождений.

Примечание. Выводить содержимое словаря result не нужно.
"""

text = "footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff"

result = {}
for symbol in text:
    result[symbol] = result.get(symbol, 0) + 1

print(result)
