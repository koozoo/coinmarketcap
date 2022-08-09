import openpyxl


def create_table(data):

    new_book = openpyxl.Workbook()
    new_sheet = new_book.active

    new_sheet.insert_rows(0)
    new_sheet['A1'].value = 'Название монеты'
    new_sheet['B1'].value = 'Символ'

    n_count = 2
    for item in data['data']:

        name = item['name']
        symbol = item['symbol']

        new_sheet[f'A{n_count}'] = name
        new_sheet[f'B{n_count}'] = symbol

        n_count += 1

    new_book.save(f'currency.xlsx')
    new_book.close()
