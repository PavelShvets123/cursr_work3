import functions

file = 'operations.json'

file_json = functions.json_file(file)

# Задаем переменную для создания списка выполненый операций
executed = "EXECUTED"

executed_list = functions.sort_data(executed, file_json)

sorted_list = functions.sort_by_date(executed_list)

# Выводим последнии 5 операции
five_latest_operations = sorted_list[:5]

# Перебираем данные по ключам
for transaction in five_latest_operations:
    date = transaction.get("date")
    description = transaction.get("description")
    from_data = transaction.get("from")
    where = transaction.get("to")
    amount = transaction.get("operationAmount").get("amount")
    currency = transaction.get("operationAmount").get("currency").get("name")

    date = functions.convert_date(date)
# Проверка отправителя средств
    if not from_data:
        name_from = ""
        hidden_from_number = 'отправитель не указан'
    elif "Счет" in from_data:
        name_from = "Счет"
        hidden_from_number = functions.account_number(from_data[-20:])
    else:
        name_from = from_data[:-17]
        hidden_from_number = functions.bankcard_number(from_data[-16:])

    to_data = functions.account_number(where[-20:])

    print(f'''{date} {description}
{name_from}{hidden_from_number} -> Счет {to_data}
{amount} {currency}\n''')
