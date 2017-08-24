import openpyxl

from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect

from .utils import process_xl_file
from .models import Participant

# Create your views here.

def index(request):
    if request.method == "POST":
        # Get the file.
        xl_file = request.FILES['file']
        try:
            workbook = openpyxl.load_workbook(xl_file)
            list_of_rows = process_xl_file(workbook)
            # import pdb;pdb.set_trace()
            request.session['list_of_rows'] = list_of_rows
            context = {'list_of_rows': list_of_rows}
            return render(request, 'upload/status.html',context)
        except:
            context = {'error': True}
            return render(request, 'upload/status.html',context)

    return render(request, 'upload/index.html')

def update(request):
    '''
    update database with the parsed excel sheet values
    '''
    if 'list_of_rows' in request.session:
        list_of_rows = request.session['list_of_rows']
        Participant.objects.all().delete()
        for item in list_of_rows:
            Participant.objects.create(reg_number=item.get('reg_number'),
                    name=item.get('name'),
                    org_name=item.get('org'))
        query_results = Participant.objects.all().order_by('reg_number')
        context = {'items': query_results}
        return render(request, 'upload/confirm.html', context)
    else:
        return redirect('index')
