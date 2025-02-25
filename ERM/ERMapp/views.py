from django.shortcuts import *
from django.http import *
from .models import *

# Create your views here.


def home(request): # Home Display
    return render(request, 'ERMapp/demo.html')


def homefunc(request): # For Customer Order
    code = request.POST.get('code')
    itemCode = request.POST.getlist('itemCode[]')
    print(f"Received code: {code}, itemCode: {itemCode}")
    customers = Customer.objects.all()
    items = Item.objects.all()
    if code:
        for x in customers:
            if x.customerCode == int(code):
                context = {'values': Customer.objects.filter(customerCode=code).values()}
                return render(request, 'ERMapp/demo.html', context)
    else:
        return HttpResponse("Empty")
    return HttpResponse("Doesn't Exist")


def formvalue(request): # For Items
    if request.method == 'POST':
        date_arr = []
        customerCode = request.POST.get('customerCode')
        customerName = request.POST.get('customerName')
        customerOrderNumber = request.POST.get('customerOrderNumber')
        customerOrderDate = request.POST.get('customerOrderDate')
        itemCode = request.POST.getlist('itemCode[]')
        itemName = request.POST.getlist('itemName[]')
        quantity = request.POST.getlist('quantity[]')
        stock = request.POST.getlist('stock[]')
        unitPrice = request.POST.getlist('unitPrice[]')
        total = request.POST.getlist('total[]')

        # For Input Data From Item
        if all(field and any(value.strip() for value in field) for field in
               [customerCode, customerName, customerOrderNumber, customerOrderDate, itemCode, itemName, quantity, stock, unitPrice, total]):
            # Order entry
            for x in range(len(itemCode)):
                account = Order(customerCode=customerCode, customerName=customerName, customerOrderNumber=customerOrderNumber, customerOrderDate=customerOrderDate, itemCode=itemCode[x], itemName=itemName[x], quantity=quantity[x], unitPrice=unitPrice[x], stock=stock[x], total=total[x])
                account.save()
            return HttpResponse("Registration Successful!")
        elif itemCode != 0 or itemCode != "":
            items = Item.objects.all()
            for x in itemCode:
                for y in items:
                    if int(x) and int(x) == y.itemCode:
                        date_arr.extend(Item.objects.filter(itemCode=int(x)))
            context = {'itemValues': date_arr}
            return render(request, 'ERMapp/demo.html', context)
        else:
            return HttpResponse("Something went Wrong !")
    else:
        return HttpResponse("Invalid request method.")


# def formvalue(request):
#     if request.method == 'POST':
#         date_arr = []
#         itemCode = request.POST.getlist('itemCode[]')
#         itemName = request.POST.getlist('itemName[]')
#         quantity = request.POST.getlist('quantity[]')
#         stock = request.POST.getlist('stock[]')
#         unitPrice = request.POST.getlist('unitPrice[]')
#         total = request.POST.getlist('total[]')
#
#         # Check if any required fields are empty
#         if not (itemCode and itemName and quantity and stock and unitPrice and total):
#             items = Item.objects.all()
#             for x in itemCode:
#                 for y in items:
#                     if x.isdigit() and int(x) == y.itemCode:  # Ensure itemCode is numeric
#                         date_arr.extend(Item.objects.filter(itemCode=int(x)).values())
#             context = {'itemValues': date_arr}
#             return render(request, 'ERMapp/demo.html', context)
#
#         elif itemCode != 0 and itemName != 0 and quantity and stock and unitPrice and total:
#             # Order entry
#             for x in range(len(itemCode)):
#                 try:
#                     account = Order(
#                         itemCode=itemCode[x],
#                         itemName=itemName[x],
#                         quantity=int(quantity[x]) if quantity[x].strip() else 0,  # Convert empty string to 0
#                         unitPrice=float(unitPrice[x]) if unitPrice[x].strip() else 0.0,  # Convert to float
#                         stock=int(stock[x]) if stock[x].strip() else 0,  # Convert to int
#                         total=float(total[x]) if total[x].strip() else 0.0  # Convert to float
#                     )
#                     account.save()
#                 except ValueError:
#                     return HttpResponse("Invalid number format in form fields.")
#
#             return HttpResponse("Registration Successful!")
#
#         else:
#             return HttpResponse("Something went wrong!")
#
#     else:
#         return HttpResponse("Invalid request method.")
