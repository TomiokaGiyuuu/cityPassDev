import json

from django.http import JsonResponse
from geopy.distance import geodesic


from django.shortcuts import render

# Create your views here.
def sort_locations_view(request):
    if request.method == 'POST':
        data = request.POST.get('locations')
        locations = json.loads(data)
        current_location = json.loads(request.POST.get('current_location'))
        sorted_locations = sort_locations(locations, current_location)
        return JsonResponse({'sorted_locations': sorted_locations})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def sort_locations(locations, current_location, sorted_locations=None):
    if sorted_locations is None:
        sorted_locations = []

    if not locations:
        return sorted_locations

    # Calculate distances from the current location to all other locations
    distances = [geodesic((current_location["lat"], current_location["lng"]),
                          (loc["lat"], loc["lng"])).meters for loc in locations]

    # Find the index of the closest location
    min_dist_idx = distances.index(min(distances))
    print("minumin dist location index is: ", min_dist_idx)

    print("Locations_original", locations)

    # Add the closest location to the sorted list
    sorted_locations.append(locations.pop(min_dist_idx))
    print("Sorted:", sorted_locations)
    print(sorted_locations[-1])

    # Recursive call with the closest location as the new current location
    print("---------------------------")
    return sort_locations(locations, sorted_locations[-1], sorted_locations)



