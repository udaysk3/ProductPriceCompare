from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse,FileResponse
import requests




#Global Data
amazon_data = None
flipkart_data = None


# Create your views here.
def home(req):
    return render(req,'home.html')
    # return HttpResponse("Welcome Home")

import requests
from django.http import JsonResponse

def searchByKeyword(req):
    keyword = req.GET.get("keyword")
    # api_data1 = {'status': 'OK', 'request_id': '2e589806-307a-4210-926b-77a4ace629f6', 'data': {'total_products': 9001, 'country': 'IN', 'products': [{'asin': 'B0BWJS72C1', 'product_title': 'MSI Titan GT77 HX, Intel 13th Gen. i9-13980HX, 44CM FHD 144Hz Mini LED, HDR 1000 Gaming Laptop (64GB/4TB NVMe SSD/Windows 11 Home/Nvidia GeForce RTX4090, 16GB GDDR6/Core Black/3.3Kg), 13VI-092IN', 'product_price': '₹5,74,990', 'product_original_price': '₹6,71,990', 'currency': 'INR', 'product_star_rating': '2.7', 'product_num_ratings': 10, 'product_url': 'https://www.amazon.in/dp/B0BWJS72C1', 'product_photo': 'https://m.media-amazon.com/images/I/71yWBoj2kuL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹5,74,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0C8P8G3WJ', 'product_title': 'Acer Aspire Lite 11th Gen Intel Core i3 Premium Metal Laptop (8GB RAM/512GB SSD/Windows 11 Home) AL15-51, 39.62cm (15.6&quot;) Full HD Display, Metal Body, Steel Gray, 1.59 Kg', 'product_price': '₹31,990', 'product_original_price': '₹44,990', 'currency': 'INR', 'product_star_rating': '3.8', 'product_num_ratings': 81, 'product_url': 'https://www.amazon.in/dp/B0C8P8G3WJ', 'product_photo': 'https://m.media-amazon.com/images/I/617rprfdhRL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹31,990', 'is_best_seller': True, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0C1GM4C6V', 'product_title': 'ASUS [SmartChoice] Vivobook 15, Intel Celeron N4020, 15.6&quot; (39.62 cms) HD, Thin and Light Laptop (8GB/512GB SSD/Integrated Graphics/Windows 11/Office 2021/Fingerprint/Silver/1.8 kg), X515MA-BR024WS', 'product_price': '₹29,990', 'product_original_price': '₹38,990', 'currency': 'INR', 'product_star_rating': '3.9', 'product_num_ratings': 1055, 'product_url': 'https://www.amazon.in/dp/B0C1GM4C6V', 'product_photo': 'https://m.media-amazon.com/images/I/71dAYFhRTcL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹29,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0C6F686WR', 'product_title': 'MSI GF63 Thin, Intel Core i7-11800H, 40CM FHD 144Hz Gaming Laptop (16GB/512GB NVMe SSD/Windows 11 Home/Nvidia GeForce GTX 1650, GDDR6 4GB/Black/1.8Kg), 11SC-1462IN', 'product_price': '₹58,990', 'product_original_price': '₹92,990', 'currency': 'INR', 'product_star_rating': '4.3', 'product_num_ratings': 84, 'product_url': 'https://www.amazon.in/dp/B0C6F686WR', 'product_photo': 'https://m.media-amazon.com/images/I/71BCum1YVzL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹58,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0C93QX5QM', 'product_title': 'Acer Aspire Lite 11th Gen Intel Core i5-1155G7 Thin and Light Laptop (16GB RAM/512GB SSD/Intel Iris Xe Graphics, Win 11 Home) AL15-51, 39.62cm (15.6&quot;) Full HD Display, Metal Body, Steel Gray, 1.59 Kg', 'product_price': '₹41,990', 'product_original_price': '₹61,990', 'currency': 'INR', 'product_star_rating': '3.4', 'product_num_ratings': 45, 'product_url': 'https://www.amazon.in/dp/B0C93QX5QM', 'product_photo': 'https://m.media-amazon.com/images/I/71czGb00k5L._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹41,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0C3CLH1PV', 'product_title': 'HP Laptop 15s, Intel Celeron N4500, 15.6 inch(39.6cm) HD Laptop (8GB RAM,512GB SSD,Intel UHD Graphics,Dual Speakers,Numeric Keypad,Alexa,Win 11,MSO 21,Natural Silver,1.69 Kgs) 15s-fq3071TU', 'product_price': '₹28,990', 'product_original_price': '₹33,935', 'currency': 'INR', 'product_star_rating': '3.2', 'product_num_ratings': 39, 'product_url': 'https://www.amazon.in/dp/B0C3CLH1PV', 'product_photo': 'https://m.media-amazon.com/images/I/811aBK9bUFL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹28,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0C15CDKTN', 'product_title': 'Dell 14 Laptop, Intel Core i5-1135G7 Processor/ 16GB / 512GB SSD / 14.0&quot; (35.54cm) FHD with Comfort View/Windows 11 + MSO&#x27;21/15 Month McAfee/Spill-Resistant Keyboard/Carbon Black Color/ 1.48kg', 'product_price': '₹51,990', 'product_original_price': '₹72,490', 'currency': 'INR', 'product_star_rating': '3.9', 'product_num_ratings': 27, 'product_url': 'https://www.amazon.in/dp/B0C15CDKTN', 'product_photo': 'https://m.media-amazon.com/images/I/51hEf-tkHrL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹51,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0CDG6TM66', 'product_title': 'HP Victus Gaming Laptop AMD Ryzen™ 7 7840HS, 40.9 cm (16.1inch) FHD (1920 x 1080), 144 Hz (16GB, 1TB) NVIDIA® GeForce RTX 3050 6GB Graphics, Win 11, B&amp;O 16-s0094AX', 'product_price': '₹84,990', 'product_original_price': '₹99,527', 'currency': 'INR', 'product_star_rating': '4.3', 'product_num_ratings': 329, 'product_url': 'https://www.amazon.in/dp/B0CDG6TM66', 'product_photo': 'https://m.media-amazon.com/images/I/71YIPsnuJvL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹84,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0B46CJ21J', 'product_title': 'Dell 14 Laptop, Intel Core 11th Gen i3-1115G4/ 8GB/ 512GB /14.0&quot;(35.56cm) FHD Display with Comfort View/Windows 11 + MSO&#x27;21/15 Month McAfee/Spill-Resistant Keyboard/Carbon Black Color/1.48kg', 'product_price': '₹35,990', 'product_original_price': '₹49,215', 'currency': 'INR', 'product_star_rating': '4', 'product_num_ratings': 195, 'product_url': 'https://www.amazon.in/dp/B0B46CJ21J', 'product_photo': 'https://m.media-amazon.com/images/I/51cW1H73uVL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹35,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0BZS88YPT', 'product_title': 'HP Laptop 14s, 12th Gen Intel Core i3-1215U, 14-inch (35.6 cm), FHD, 8GB DDR4, 512GB SSD, Intel UHD Graphics, Thin &amp; Light, Dual Speakers (Win 11, MSO 2021, Silver, 1.46 kg), dy5008TU', 'product_price': '₹40,490', 'product_original_price': '₹51,265.85', 'currency': 'INR', 'product_star_rating': '4', 'product_num_ratings': 1234, 'product_url': 'https://www.amazon.in/dp/B0BZS88YPT', 'product_photo': 'https://m.media-amazon.com/images/I/71XySD6YwEL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹40,490', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0CCRSRM4Q', 'product_title': 'HP 255 G8 Laptop with AMD Athlon Silver 3050U APU/ 4GB Ram/ 256GB SSD/Windows 11/AMD Radeon Vega 8 Mobile Graphics/39.6 cm HD (1366 x 768), SVA, Anti-Glare WLED/Black/1 Year Onsite Warranty', 'product_price': '₹22,790', 'product_original_price': '₹99,999', 'currency': 'INR', 'product_star_rating': '3.8', 'product_num_ratings': 5, 'product_url': 'https://www.amazon.in/dp/B0CCRSRM4Q', 'product_photo': 'https://m.media-amazon.com/images/I/81GtQFQq-LL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹22,790', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B08316YSKH', 'product_title': 'Chuwi HeroBook Pro 14.1&#x27;&#x27; Laptop, 8GB RAM 256GB SSD, Windows 11 Laptop, 1TB SSD Expand, Intel Celeron N4020(up to 2.8GHz), FHD IPS Display, Ultra Slim, Mini-HDMI, USB3.0, Webcam,TF Card', 'product_price': '₹19,990', 'product_original_price': '₹34,990', 'currency': 'INR', 'product_star_rating': '3.9', 'product_num_ratings': 1951, 'product_url': 'https://www.amazon.in/dp/B08316YSKH', 'product_photo': 'https://m.media-amazon.com/images/I/61Bko7nc14L._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹19,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0CCDRPGD8', 'product_title': 'JioBook 11 (2023) NB1112MM(BLU) (Mediatek 8788 Octa-core 2 GHz/ARM Mali G72 MP3 @800 MHz/29.5cms 60 Hz/Thin and Light Laptop/ 4 GB LPDDR4/ 64 GB eMMC/JioOS 4G LTE, Dual Band Wi-Fi/Blue/ 990 GMS)', 'product_price': '₹16,499', 'product_original_price': '₹25,000', 'currency': 'INR', 'product_star_rating': '3.1', 'product_num_ratings': 76, 'product_url': 'https://www.amazon.in/dp/B0CCDRPGD8', 'product_photo': 'https://m.media-amazon.com/images/I/51cNQIk3q9L._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹16,499', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B0C91TDJ68', 'product_title': 'Dell Inspiron 3525 Laptop, AMD Ryzen R3-5300U/8GB/512GB SSD/15.6&quot; (39.62CMs) FHD WVA AG Narrow Border 120Hz 250 nits/Windows 11+MSO&#x27;21/15 Month McAfee/Carbon Black/1.68KGs', 'product_price': '₹33,990', 'product_original_price': '₹45,133', 'currency': 'INR', 'product_star_rating': '4', 'product_num_ratings': 7, 'product_url': 'https://www.amazon.in/dp/B0C91TDJ68', 'product_photo': 'https://m.media-amazon.com/images/I/51-OoAkxQqL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹33,990', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}]}}
    api_data1 = amazon_api(keyword) 
    api_data2 = flipkart_api(keyword) 
    # print(api_data1)
    combined_data = combineData(api_data1, api_data2)
    # return JsonResponse(combined_data, safe=False)
    return render(req,'index.html' , combined_data)

def searchBytitle(title):
    api_data1 = amazon_api(title)
    api_data2 = flipkart_api(title)
    
    combined_data = combineData(api_data1, api_data2)
    # return JsonResponse(combined_data, safe=False)
    return combined_data



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
        'X-RapidAPI-Key': '2a537099efmshd1a71173ebec557p1a4fd0jsn45a9f966e035',
    }
    try:    
        response = requests.get(api_url, headers=headers)
        # print(response.json())
        if response.status_code == 200:
            api_data = response.json()
            # print(api_data)
            title = api_data["product"]["title"]
            combined_data = searchBytitle(title)
            # return render(req, "compare.html", {
            #     'amazon_item' : amazon_item,
            #     'flipkart_item' : flipkart_item
            # })
        return render(req,'index.html',combined_data)
        return HttpResponse("Some error ooccured Please Try again!")

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})


def fetchByASIN(asin):
    api_url = 'https://aids.p.rapidapi.com/products/'+asin+'?api_key=c2206c49a186bdded150ff78fea282c4'
    headers = { 
        'X-RapidAPI-Host': 'aids.p.rapidapi.com',
        'X-RapidAPI-Key': '2a537099efmshd1a71173ebec557p1a4fd0jsn45a9f966e035',
    }
    try:
        response = requests.get(api_url, headers)
        # print(response.json())
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
        # print(amazon_item)
    except:
        pass
    api_data2 = flipkart_api(amazon_item["product_title"])[0]
    flipkart_item = {
            "product_title": api_data2.get("name", "  "),
            "product_price": api_data2.get("current_price", ""),
            "product_photo": api_data2.get("thumbnail", ""),
            "product_original_price": api_data2.get("original_price", ""),
            "url" : api_data2.get("link")
        }
    return [amazon_item, flipkart_item]

    


def flipkart_api(keyword):
    api_url = 'https://flipkart-scraper-api.dvishal485.workers.dev/search/'+keyword
    try:
        response2 = requests.get(api_url)
        if response2.status_code == 200:
            api_data2 = response2.json()
            api_data2["result"] = api_data2["result"]
    except:
        api_data2 = {"results" : []}
    # print(api_data2)
    return api_data2
        
        
def amazon_api(keyword):
    # api_url = 'https://real-time-amazon-data.p.rapidapi.com/search?query='+keyword+'&page=1&country=IN'
    api_url = 'https://real-time-amazon-data.p.rapidapi.com/search?query='+keyword+'&page=1&country=IN'
    headers = { 
        'X-RapidAPI-Host': 'real-time-amazon-data.p.rapidapi.com',
        'X-RapidAPI-Key': '2a537099efmshd1a71173ebec557p1a4fd0jsn45a9f966e035'}
    try:
        response = requests.get(api_url, headers=headers)
        # print(response.json())
        if response.status_code == 200:
            api_data = response.json()
            # api_data["data"]["products"] = api_data["data"]["products"]
            # api_data["data"]["products"] = sorted(api_data["data"]["products"], key=lambda x: (-x["product_title"].count(keyword), -float(x.get("product_star_rating", 0))))
        # sample_data = {'status': 'OK', 'request_id': '9c7af152-6b4e-40d9-a9e9-37f678f66c40', 'data': {'total_products': 134, 'country': 'IN', 'products': [{'asin': 'B097BL2VSX', 'product_title': '(Refurbished) Realme 7i (Fusion Blue, 4GB RAM, 64GB Storage)', 'product_price': '₹10,999', 'product_original_price': '₹11,999', 'currency': 'INR', 'product_star_rating': '5', 'range' : range(4) ,'product_num_ratings': 10, 'product_url': 'https://www.amazon.in/dp/B097BL2VSX', 'product_photo': 'https://m.media-amazon.com/images/I/41FO5YxxFyS._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹10,999', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B08KGNQJVL', 'product_title': '(Refurbished) Realme 7 (Mist Blue, 64 GB) (6 GB RAM)', 'product_price': '₹12,799.99','range' :range(int(5)), 'product_original_price': '₹13,999', 'currency': 'INR', 'product_star_rating': '3.6', 'product_num_ratings': 95, 'product_url': 'https://www.amazon.in/dp/B08KGNQJVL', 'product_photo': 'https://m.media-amazon.com/images/I/3190PsrBwUL._AC_SX290_SY416_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹12,799.99', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B08N19GBFD', 'product_title': '(Renewed) Realme 7 Pro (Mirror Silver, 6GB RAM, 128GB Storage)', 'product_price': '₹13,999', 'product_original_price': '₹14,999', 'currency': 'INR', 'product_star_rating': '3.4', 'product_num_ratings': 78, 'product_url': 'https://www.amazon.in/dp/B08N19GBFD', 'product_photo': 'https://m.media-amazon.com/images/I/51y6ryf+gGL._AC_SX444_SY639_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹13,999', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B09778HZLB', 'product_title': '(Refurbished) Realme 7 Pro (Mirror Blue, 6GB RAM, 128GB Storage)', 'product_price': '₹12,695', 'product_original_price': None, 'currency': 'INR', 'product_star_rating': '3.4', 'product_num_ratings': 23, 'product_url': 'https://www.amazon.in/dp/B09778HZLB', 'product_photo': 'https://m.media-amazon.com/images/I/41jrb4uoo2S._AC_SX348_SY500_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹12,695', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}, {'asin': 'B08MB7P913', 'product_title': '(Refurbished) Realme 7 (Mist White, 64 GB) (6 GB RAM)', 'product_price': '₹9,749', 'product_original_price': '₹16,990', 'currency': 'INR', 'product_star_rating': '3.3', 'product_num_ratings': 34, 'product_url': 'https://www.amazon.in/dp/B08MB7P913', 'product_photo': 'https://m.media-amazon.com/images/I/31h2YHQ+R9L._AC_SX296_SY426_QL65_.jpg', 'product_num_offers': None, 'product_minimum_offer_price': '₹9,749', 'is_best_seller': False, 'is_prime': True, 'climate_pledge_friendly': False}]}}
        # api_data  = sample_data
        else:
            api_data = {"data": {"products": []}}
    except:
        api_data = {"data": {"products": []}}
    return api_data


def combineData(api_data1, api_data2,sortby="own"):
    amazon_results = []
    flipkart_results = []
    for amazon_product in api_data1.get("data", {}).get("products", []):
        amazon_item = {
            "product_title": amazon_product.get("product_title", ""),
            # "product_price": amazon_product.get("product_price", ""),
            "product_price": amazon_product.get("product_price",""),
            "product_photo": amazon_product.get("product_photo", ""),
            "product_original_price": amazon_product.get("product_original_price", ""),
            'reviewCount' : amazon_product.get("product_num_ratings"),
            "is_prime" : amazon_product.get("is_prime"),
            'url' : amazon_product.get("product_url"),
            "in_stock" : True
        }
        # if(amazon_item["product_price"] != "" and amazon_item["product_price"] is not None):
        #    amazon_item["product_price"]  =  round(float(amazon_product.get("product_price", "").replace("$","").replace(",","")))*80
        # else:
        #    amazon_item["product_price"]  =  "Not Available"
            
        # if(amazon_product.get("product_url") is not None):
        #     amazon_item["url"] = amazon_product.get("product_url").replace(".com",".in")
        if amazon_item["product_price"] is None:
            amazon_item["in_stock"] = False
        else:
            amazon_item["in_stock"] = True
        amazon_results.append(amazon_item)
    
    for flipkart_product in api_data2.get("result" , {}):
        flipkart_item = {
            "product_title": flipkart_product.get("name", "  "),
            "product_price": flipkart_product.get("current_price", ""),
            "product_photo": flipkart_product.get("thumbnail", ""),
            "product_original_price": flipkart_product.get("original_price", ""),
            "query_url" : flipkart_product.get("query_url",""),
            "url" : flipkart_product.get("link"),
            "in_stock" : True
        }
        
        if flipkart_item["query_url"] is not None:
            response = requests.get(flipkart_item["query_url"])
            data = response.json()
            if (data.get("in_stock") is not None and data["in_stock"]==True):
                flipkart_item["in_stock"] = True
            else:
                flipkart_item["in_stock"] = False
        
    
        flipkart_results.append(flipkart_item)
    if(sortby=="asc"):
        if amazon_results is not None:
            amazon_results = sorted(amazon_results, key=lambda x: float( x["product_price"].replace("₹", "").replace(",", "")  if x["product_price"] is not None else 0))
        if flipkart_results is not None:    
            flipkart_results = sorted(flipkart_results, key=lambda x: float(x["product_price"]))
    elif sortby=="desc":
        if amazon_results is not None:
            amazon_results = sorted(amazon_results, key=lambda x: float( x["product_price"].replace("₹", "").replace(",", "")  if x["product_price"] is not None else 0),reverse=True)
        if flipkart_results is not None:
            flipkart_results = sorted(flipkart_results, key=lambda x: float(x["product_price"]),reverse=True)


    combined_results = []
    min_length = min(len(amazon_results), len(flipkart_results))

    for i in range(min_length):
        combined_item = {
            "amazon_item": amazon_results[i],
            "flipkart_item": flipkart_results[i]
        }
        combined_results.append(combined_item)
    for i in range(min_length, len(amazon_results)):
        combined_item = {
            "amazon_item" : amazon_results[i],
            "flipkart_item" : None
        }
        combined_results.append(combined_item)
    for i in range(min_length, len(flipkart_results)):
        combined_item = {
            "amazon_item" : None,
            "flipkart_item" : flipkart_results[i]
        }
        combined_results.append(combined_item)

    # Return the combined results
    combined_data = {
        "combined_results": combined_results
    }
    global amazon_data
    global flipkart_data
    amazon_data = api_data1
    flipkart_data = api_data2
    return combined_data
# fetchByASIN("B00S9BOLD4") 


def combineFilterData(min_budget , max_budget,sortby='asc'):
    amazon_results = []
    flipkart_results = []
    api_data1 = amazon_data
    api_data2 = flipkart_data
    for amazon_product in api_data1.get("data", {}).get("products", []):
        amazon_item = {
            "product_title": amazon_product.get("product_title", ""),
            "product_price": amazon_product.get("product_price", ""),
            "product_photo": amazon_product.get("product_photo", ""),
            "product_original_price": amazon_product.get("product_original_price", ""),
            'reviewCount' : amazon_product.get("product_num_ratings"),
            "is_prime" : amazon_product.get("is_prime"),
            'url' : amazon_product.get("product_url"),
            "in_stock" : True
        }
        
        if amazon_item["product_price"] is None:
            amazon_item["in_stock"] = False
        else:
            amazon_item["in_stock"] = True
        amazon_results.append(amazon_item)
        if(amazon_item['product_price'] is not None):
            if(int(amazon_item['product_price'].replace("₹", "").replace(",", "")) >= int(min_budget) and int(amazon_item['product_price'].replace("₹", "").replace(",", ""))<=int(max_budget)):
                amazon_results.append(amazon_item)
    
    for flipkart_product in api_data2.get("result" , {}):
        flipkart_item = {
            "product_title": flipkart_product.get("name", "  "),
            "product_price": flipkart_product.get("current_price", ""),
            "product_photo": flipkart_product.get("thumbnail", ""),
            "product_original_price": flipkart_product.get("original_price", ""),
            "query_url" : flipkart_product.get("query_url",""),
            "url" : flipkart_product.get("link")
        }
        if flipkart_item["query_url"] is not None:
            response = requests.get(flipkart_item["query_url"])
            data = response.json()
            if (data["in_stock"]=="true"):
                flipkart_item["in_stock"] = True
            else:
                flipkart_item["in_stock"] = False
        
        if(int(flipkart_item['product_price']) >= int(min_budget) and int(flipkart_item['product_price'])<=int(max_budget)):
             flipkart_results.append(flipkart_item)
    if(sortby=="asc"):
        if amazon_results is not None:
            amazon_results = sorted(amazon_results, key=lambda x: float( x["product_price"].replace("₹", "").replace(",", "")  if x["product_price"] is not None else 0))
        if flipkart_results is not None:    
            flipkart_results = sorted(flipkart_results, key=lambda x: float(x["product_price"]))
    elif sortby=="desc":
        if amazon_results is not None:
            amazon_results = sorted(amazon_results, key=lambda x: float( x["product_price"].replace("₹", "").replace(",", "")  if x["product_price"] is not None else 0),reverse=True)
        if flipkart_results is not None:
            flipkart_results = sorted(flipkart_results, key=lambda x: float(x["product_price"]),reverse=True)
    combined_results = []
    min_length = min(len(amazon_results), len(flipkart_results))

    for i in range(min_length):
        combined_item = {
            "amazon_item": amazon_results[i],
            "flipkart_item": flipkart_results[i]
        }
        combined_results.append(combined_item)
    for i in range(min_length, len(amazon_results)):
        combined_item = {
            "amazon_item" : amazon_results[i],
            "flipkart_item" : None
        }
        combined_results.append(combined_item)
    for i in range(min_length, len(flipkart_results)):
        combined_item = {
            "amazon_item" : None,
            "flipkart_item" : flipkart_results[i]
        }
        combined_results.append(combined_item)
    # Return the combined results
    
    combined_data = {
        "combined_results": combined_results
    }
    return combined_data

def sortByPrice(req):
    combine_data = combineData(amazon_data, flipkart_data, req.GET.get("sort_param"))
    return render(req,'index.html',combine_data)

def filterByBudget(req):
    min_budget = req.POST['min_budget']
    max_budget = req.POST['max_budget']
    combined_data = combineFilterData(min_budget, max_budget)
    return render(req,'index.html',combined_data)