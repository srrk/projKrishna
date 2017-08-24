# Processing routines for views.
import openpyxl

from upload.models import Participant

def process_xl_file(workbook):
    '''
    Process the xl file and send the reply 
    as database objects without saving to 
    database
    '''
    sheet = workbook.get_sheet_by_name('DD and Cash')
    list_of_rows = []
    for row in sheet.rows:
        if type(row[0].value) is int:
            reg = row[0].value
            name = row[1].value
            org = row[2].value
            dataset = {}
            dataset["reg_number"] = reg
            dataset["name"] = name
            dataset["org"] = org
            list_of_rows.append(dataset)
        else:
            continue
    return list_of_rows
