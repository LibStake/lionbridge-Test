from openpyxl import Workbook
import data_structure

def printToExcel(savePath):
    workbook = Workbook()
    sheet = workbook.active

    sheet['A1'] = 'Page ID'
    sheet['B1'] = 'Page Title'
    sheet['C1'] = 'Template Name'
    sheet['D1'] = 'Date of Birth'
    sheet['E1'] = 'Height'
    sheet['F1'] = 'Team'

    col = 1
    row = 2

    for data in data_structure.DataSetList:
        for val in data.field.values():
            sheet.cell(row=row, column=col).value = val
            col += 1
        col = 1
        row += 1

    workbook.save(savePath)
    workbook.close()