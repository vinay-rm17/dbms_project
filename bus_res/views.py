from django.shortcuts import render
import mysql.connector as sql


def booking(request):
    if request.method == "POST":
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date=request.POST.get('travel_date')
        n = sql.connect(host="localhost", user="root", password="W7301@jqir#", database="bus")
        cursor = n.cursor()
        
        query = "SELECT bus_name, bus_no,cost FROM travels WHERE source=%s AND destination=%s AND travel_date=%s"
        cursor.execute(query, (source, destination,date))
        travels = cursor.fetchall()
        
        if travels:
            travel_details = [{'name': travel[0], 'number': travel[1],'cost':travel[2]} for travel in travels]
            return render(request, 'book.html', {'travel_details': travel_details})
        else:
            return render(request, 'error.html')
    return render(request, 'dbms1.html')

def ticket_view(request):
    travel_name = request.GET.get('travelName')
    travel_number = request.GET.get('travelNumber')
    travel_cost=request.GET.get('travelCost')
    context = {
        'travel_name': travel_name,
        'travel_number': travel_number,
        'travel_cost':travel_cost,

    }
    return render(request, 'ticket.html', context)