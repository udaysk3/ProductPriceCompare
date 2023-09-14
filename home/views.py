from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse,FileResponse
import requests
# Create your views here.
def home(req):
    return render(req,'home.html')
    # return HttpResponse("Welcome Home")

import requests
from django.http import JsonResponse

def searchByKeyword(req):
    keyword = req.GET.get("keyword")
    api_data1 = amazon_api(keyword)
    api_data2 = flipkart_api(keyword)
    
    combined_data = combineData(api_data1, api_data2)
    # return JsonResponse(combined_data, safe=False)
    return render(req,'index.html' , combined_data)



import cv2
from pyzbar.pyzbar import decode

def capture():
    # Initialize the camera capture
    cap = cv2.VideoCapture(0)
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
        if cv2.waitKey(1) & 0xFF == 27:
            cap.release()
            cv2.destroyAllWindows()
            return
        
        if cv2.getWindowProperty('Barcode Scanner', cv2.WND_PROP_VISIBLE)<1:
            cap.release()
            cv2.destroyAllWindows()
            return

def searchByGTIN(req):
    gtin = capture()
    if gtin == None:
        return render(req,"home.html")
    api_url = 'https://barcodes1.p.rapidapi.com/?query='+gtin
    headers = {
        'X-RapidAPI-Host': 'barcodes1.p.rapidapi.com',
        'X-RapidAPI-Key': 'd9496b245emsh6c6a6bfc69583afp1ecafajsn20b6e27e13a7',
    }
    try:    
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            api_data = response.json()
            asin = api_data["product"]["attributes"]["asin"]
            amazon_item , flipkart_item = fetchByASIN(asin)
            return HttpResponse(amazon_item)
            # return render(req, "compare.html", {
            #     'amazon_item' : amazon_item,
            #     'flipkart_item' : flipkart_item
            # })
        return HttpResponse("Some error ooccured Please Try again!")

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})
    

def fetchByASIN(asin):
    print(asin)
    api_url = 'https://amazon-scrapper-api3.p.rapidapi.com/products/'+str(asin)+'?api_key=17fd230b65a63c27854fdb057d95524c'
    headers = { 
        'X-RapidAPI-Host': 'amazon-scrapper-api3.p.rapidapi.com',
        'X-RapidAPI-Key': 'd9496b245emsh6c6a6bfc69583afp1ecafajsn20b6e27e13a7',
    }
    response = requests.get(api_url, headers)
    if response.status_code == 200:
        api_data = response.json()
        amazon_item = {
        "product_title": api_data.get("name", ""),
        "product_price": api_data.get("pricing", ""),
        "shipping_price": api_data.get("shipping_price", ""),
        "product_photo" : api_data.get("images",[]),
        "brand": api_data.get("brand", ""),
        "range" : range(int(api_data.get("average_rating")[0])),
        'reviewCount' : api_data.get("total_reviews"),
        "weight" : api_data.get("weight"),
        'url' : 'https://amazon.in/dp/'+asin,
    }
    else:
        print(response)
    print(amazon_item)
    api_data2 = flipkart_api(amazon_item["product_title"])[0]
    flipkart_item = {
            "product_title": api_data2.get("name", "  "),
            "product_price": api_data2.get("current_price", ""),
            "product_photo": api_data2.get("thumbnail", ""),
            "product_original_price": api_data2.get("original_price", ""),
            "url" : api_data2.get("link")
        }
    return [amazon_item, flipkart_item]
    
    
print(fetchByASIN('B00S9BOLD4'))

def flipkart_api(keyword):
    api_url = 'https://flipkart-scraper-api.dvishal485.workers.dev/search/'+keyword
    try:
        response2 = requests.get(api_url)
        if response2.status_code == 200:
            api_data2 = response2.json()
            api_data2["result"] = api_data2["result"][:5]
    except:
        api_data2 = {"results" : []}
        
        
def amazon_api(keyword):
    api_url = 'https://real-time-amazon-data.p.rapidapi.com/search?query='+keyword+'&page=1&country=IN'
    headers = { 
        'X-RapidAPI-Host': 'real-time-amazon-data.p.rapidapi.com',
        'X-RapidAPI-Key': 'c0bbe0d173mshba64da84edcbaddp14163ejsn21a7047f7e51',
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            api_data = response.json()
            # Limit the results to the top 5
            api_data["data"]["products"] = api_data["data"]["products"][:5]
            # Sort the Amazon results based on keyword match and then by average rating
            # api_data["data"]["products"] = sorted(api_data["data"]["products"], key=lambda x: (-x["product_title"].count(keyword), -float(x.get("product_star_rating", 0))))
        sample_data = {'status': 'OK', 'request_id': '9c7af152-6b4e-40d9-a9e9-37f678f66c40', 'data': {'total_products': 134, 'country': 'IN', 'products': [{'asin': 'B097BL2VSX', 'product_title': '(Refurbished) Realme 7i (Fusion Blue, 4GB RAM, 64GB Storage)', 'product_price': '₹10,999', 'product_original_price': '₹11,999', 'currency': 'INR', 'product_star_rating': '5', 'range' : range(4) ,'product_num_ratings': 10, 'product_url': 'https://www.amazon.in/dp/B097BL2VSX', 'product_photo': 'https://m.media-amazon.com/images/I/41FO5YxxFyS._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹10,999', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B08KGNQJVL', 'product_title': '(Refurbished) Realme 7 (Mist Blue, 64 GB) (6 GB RAM)', 'product_price': '₹12,799.99','range' :range(int(5)), 'product_original_price': '₹13,999', 'currency': 'INR', 'product_star_rating': '3.6', 'product_num_ratings': 95, 'product_url': 'https://www.amazon.in/dp/B08KGNQJVL', 'product_photo': 'https://m.media-amazon.com/images/I/3190PsrBwUL._AC_SX290_SY416_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹12,799.99', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B08N19GBFD', 'product_title': '(Renewed) Realme 7 Pro (Mirror Silver, 6GB RAM, 128GB Storage)', 'product_price': '₹13,999', 'product_original_price': '₹14,999', 'currency': 'INR', 'product_star_rating': '3.4', 'product_num_ratings': 78, 'product_url': 'https://www.amazon.in/dp/B08N19GBFD', 'product_photo': 'https://m.media-amazon.com/images/I/51y6ryf+gGL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹13,999', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B09778HZLB', 'product_title': '(Refurbished) Realme 7 Pro (Mirror Blue, 6GB RAM, 128GB Storage)', 'product_price': '₹12,695', 'product_original_price': None, 'currency': 'INR', 'product_star_rating': '3.4', 'product_num_ratings': 23, 'product_url': 'https://www.amazon.in/dp/B09778HZLB', 'product_photo': 'https://m.media-amazon.com/images/I/41jrb4uoo2S._AC_SX348_SY500_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹12,695', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B08MB7P913', 'product_title': '(Refurbished) Realme 7 (Mist White, 64 GB) (6 GB RAM)', 'product_price': '₹9,749', 'product_original_price': '₹16,990', 'currency': 'INR', 'product_star_rating': '3.3', 'product_num_ratings': 34, 'product_url': 'https://www.amazon.in/dp/B08MB7P913', 'product_photo': 'https://m.media-amazon.com/images/I/31h2YHQ+R9L._AC_SX296_SY426_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹9,749', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}]}}
        api_data  = sample_data
    except:
        api_data = {"data": {"products": []}}
    return api_data


def combineData(api_data1, api_data2):
    amazon_results = []
    flipkart_results = []


    for amazon_product in api_data1.get("data", {}).get("products", []):
        amazon_item = {
            "product_title": amazon_product.get("product_title", ""),
            "product_price": amazon_product.get("product_price", ""),
            "product_photo": amazon_product.get("product_photo", ""),
            "product_original_price": amazon_product.get("product_original_price", ""),
            "range" : range(int(amazon_product.get("product_star_rating")[0])),
            'reviewCount' : amazon_product.get("product_num_ratings"),
            "is_prime" : amazon_product.get("is_prime"),
            'url' : amazon_product.get("product_url")
        }
        amazon_results.append(amazon_item)

    for flipkart_product in api_data2.get("result" , {}):
        flipkart_item = {
            "product_title": flipkart_product.get("name", "  "),
            "product_price": flipkart_product.get("current_price", ""),
            "product_photo": flipkart_product.get("thumbnail", ""),
            "product_original_price": flipkart_product.get("original_price", ""),
            "url" : flipkart_product.get("link")
        }
        flipkart_results.append(flipkart_item)
    combined_results = []
    min_length = min(len(amazon_results), len(flipkart_results))

    for i in range(min_length):
        combined_item = {
            "amazon_item": amazon_results[i],
            "flipkart_item": flipkart_results[i]
        }
        combined_results.append(combined_item)

    # Return the combined results
    combined_data = {
        "combined_results": combined_results
    }
    return combined_data
