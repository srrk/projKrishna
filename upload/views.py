import openpyxl

from django.shortcuts import render, HttpResponse

from .utils import process_xl_file

# Create your views here.

def index(request):

    if request.method == "POST":
        # Get the file.
        xl_file = request.FILES['file']
        try:
            workbook = openpyxl.load_workbook(xl_file)
            list_of_rows = process_xl_file(workbook)
            context = {'list_of_rows': list_of_rows}
            return render(request, 'upload/status.html',context)
        except:
            context = {'error': True}
            return render(request, 'upload/status.html',context)

    return render(request, 'upload/index.html')
