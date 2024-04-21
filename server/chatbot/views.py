import json
import re
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt

from .Islam.code_2 import *

from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'chatbot/index.html')

def get_place_id_through_name(request):
    search_term = request.GET.get('search_term', '')

    if search_term:
        places = Places.objects.filter(name__icontains=search_term)
        place_ids = [place.id for place in places]
        return JsonResponse({'place_ids': place_ids})
    else:
        return JsonResponse({'error': 'No search term provided'})

def get_place_by_id(request, place_id):
    print("HEloooooooooooooooooooooooo")
    try:
        place = Places.objects.prefetch_related('schedule_mo', 'schedule_tu', 'schedule_we',
                                                              'schedule_th', 'schedule_fr', 'schedule_sa',
                                                              'schedule_su').get(pk=place_id)
        place_data = {
            'id': place.id,
            'name': get_normal_text(place.name),
            'description': get_normal_text(place.description),
            'address': get_normal_text(place.address),
            'image_url': place.image,
            'instruction': get_normal_text(place.instruction),

            'longitude': float(place.longitude),
            "latitude": float(place.latitude),

            'schedule_mo': get_schedules_json(place.schedule_mo_id),
            'schedule_tu': get_schedules_json(place.schedule_tu_id),
            'schedule_th': get_schedules_json(place.schedule_th_id),
            'schedule_we': get_schedules_json(place.schedule_we_id),
            'schedule_fr': get_schedules_json(place.schedule_fr_id),
            'schedule_sa': get_schedules_json(place.schedule_sa_id),
            'schedule_su': get_schedules_json(place.schedule_su_id),

            'category': get_normal_text(get_cat_name(place.category_id)),
        }
        print(place_data)
        # place_data = serializers.serialize('json', [place])
        return JsonResponse({'place': json.dumps(place_data)})

    except Places.DoesNotExist:
        return JsonResponse({'error': 'Place not found'}, status=404)

# def get_places_json(request):
#     places = Places.objects.all()
#     places_data = [{'name': place.name, 'description': place.description, ...} for place in places]
#     return JsonResponse({'places': json.dumps(places_data)})
#
def get_schedules_json(schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    return {
        'start_time': schedule.start_time.strftime("%H:%M:%S"),
        'end_time': schedule.end_time.strftime("%H:%M:%S"),
        'excuse': schedule.excuse
    }

def get_cat_name(category_id):
    cat = Category.objects.get(pk=category_id)
    return cat.category_name

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            print("___________________________________________")
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

def get_normal_text(encoded_text):
    # Define a pattern to match Unicode escape sequences
    pattern = r'\\[Uu]([0-9a-fA-F]{4})'

    # Replace the escape sequences with the decoded characters
    def replace(match):
        return chr(int(match.group(1), 16))

    decoded_text = re.sub(pattern, replace, encoded_text)
    print(decoded_text)
    return decoded_text

def remove_backslash(text):
    text = text.strip()
    if text.startswith('\\') and len(text) > 1:
        text = text[1:]
    return text

def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")
@csrf_exempt
def conversation(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        prompt = data.get('prompt')
        category = check_category(data.get('category', ''))

        answer = generate_response(prompt)

        # Return the answer as a JSON response
        return JsonResponse({'answer': answer})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



def check_category(category):
    cat = category.lower()
    switcher = {
        "музей": "Музей",
        "театр": "Театр",
        "монумент": "Монумент",
        "развлечения": "Развлечения",
        "мечеть": "Мечеть",
        "парк": "Парк",
        "искусство": "Искусство",
        "культурный центр": "Культурный Центр",
    }
    return switcher.get(category.lower(), "Без")

# Музей, Театр, Монумент, Развлечения, Мечеть, Парк, Искусство, Культурный Центр, Без
