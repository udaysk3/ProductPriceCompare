from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
import requests
# Create your views here.
def home(req):
    return render(req,'index.html')
    # return HttpResponse("Welcome Home")

def searchByKeyword(req):
    pass 

def searchByGTIN(req):
    gtin = req.GET.get('gtin')
    api_url = 'https://barcodes1.p.rapidapi.com/?query='+gtin
    headers = {
        'X-RapidAPI-Host': 'barcodes1.p.rapidapi.com',
        'X-RapidAPI-Key': 'd9496b245emsh6c6a6bfc69583afp1ecafajsn20b6e27e13a7',
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            api_data = response.json()
            context ={}
            # context['name'] = api_data['properties']['title'][0]
            # context['image'] = api_data['stores'][0]['image']
            # context['resp'] = api_data
            # context['stores'] = api_data['stores']
            # return render(req, 'index.html', context)
            return JsonResponse(api_data)
        else:
            return JsonResponse({'error': 'API request failed'}, status=response.status_code)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})


import cv2
from pyzbar.pyzbar import decode

def capture():
    # Initialize the camera capture
    cap = cv2.VideoCapture(1)
    res = ""
    while True:
        # Read a frame from the camera feed
        ret, frame = cap.read()

        # Decode barcodes in the frame
        barcodes = decode(frame)
        # Loop through detected barcodes
        for barcode in barcodes:
            # Extract barcode data
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            if(len(barcode_data)) <=13:
                cap.release()
                cv2.destroyAllWindows()
            return barcode_data

        # Display the frame
        cv2.imshow('Barcode Scanner', frame)
        # Exit when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return

def scan_barcode(req):
    gtin = capture()
    return HttpResponse(gtin)