from django.shortcuts import render
from datetime import datetime, timedelta
import os
import pytz

tz = pytz.timezone('America/Panama')

def img_list(request):

    if request.GET.get('del'):
        file = request.GET.get('del')
        try:
            os.remove('/var/www/eq/media/screenshots/' + file)
        except:
            pass

    utc = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    pan = datetime.now()
    pan = pytz.utc.localize(pan, is_dst=None).astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')

    images = os.listdir('/var/www/eq/media/screenshots')
    images.sort(reverse=True)
    num_events = len(images)

    context = {
        'utctime': utc,
        'panamatime': pan,
        'images': images,
        'numevents': num_events,
    }
    return render(request, 'main/index.html', context)
