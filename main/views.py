from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . models import transactions

# Create your views here.

context = {
        "transactions": [
            {
                'type': "income",
                'source': "freelancing",
                'paid_to': None,
                'mode_of_payment': "Bank Transfer",
                "amount": 1000.00,
                'currency': "USD",
                'description': "Payment for web development project",
                'date': "2024-11-30",
                'time_stamp_created': "2024-12-16T10:00:00",
                'time_stamp_updated': "2024-12-16T12:00:00"   
            },
            {
                'type': "expense",
                'source': None,
                'paid_to': "Office supplies store",
                'mode_of_payment': "UPI",
                "amount": 500.00,
                'currency': "INR",
                'description': "stationery",
                'date': "2024-11-30",
                'time_stamp_created': "2024-12-16T10:00:00",
                'time_stamp_updated': "2024-12-16T12:00:00"   
            },
            
            {
                'type': "expense",
                'source': None,
                'paid_to': "Dmart",
                'mode_of_payment': "Credit card",
                "amount": 5000.00,
                'currency': "INR",
                'description': "Groceries",
                'date': "2024-11-30",
                'time_stamp_created': "2024-12-16T10:00:00",
                'time_stamp_updated': "2024-12-16T12:00:00"   
            }
        ]
    }


def index(request):
            
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def transactions_input(request):
    if request.method == "POST":
        type = request.POST.get('type')
        if type == 'income':
            source = request.POST.get('source_or_paid_to')
            paid_to = None
        else:
            source = None
            paid_to = request.POST.get('source_or_paid_to')   
        mode_of_payment = request.POST.get('mode_of_payment')
        paid_to = request.POST.get('paid_to')
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        description = request.POST.get('description')
        date = request.POST.get('date')
        
        temp_dict = {
                'type': type,
                'source': source,
                'paid_to': paid_to,
                'mode_of_payment': mode_of_payment,
                "amount": amount,
                'currency': currency,
                'description': description,
                'date': date,
                'time_stamp_created': datetime.datetime.now,
                'time_stamp_updated': datetime.datetime.now
        }
        context['transactions'].append(temp_dict)
        return render(request, 'index.html', context)
    else:
        return render(request, 'transactions_input.html')

def tr_list(request):
    tr_item = transactions.objects.all()
    return render(request, 'transactions_input.html' )


# context = {
#         "transactions": 
#             {
#                 'type': "income",
#                 'source': "freelancing",
#                 'paid_to': None,
#                 'mode_of_payment': "Bank Transfer",
#                 "amount": 1000.00,
#                 'currency': "USD",
#                 'description': "Payment for web development project",
#                 'date': "2024-11-30",
#                 'time_stamp_created': "2024-12-16T10:00:00",
#                 'time_stamp_updated': "2024-12-16T12:00:00"   
#             }
#     }

# # income/expenses
# # income_source
# # mode_of_payment
# # paid_to
# # amount
# # currency
# # description
# # date
# # Timestamp_created
# # timestamp_updated


# give me a python code on this to use in django context