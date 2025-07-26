from datetime import datetime
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LlmAgent
from google.adk.tools import google_search
from .holiday import get_holidays_list
from .mandi import fetch_mandi_data

def holiday_tool():
    """
    Returns holidays for the current month using Google Calendar API.
    """
    return get_holidays_list()


def mandi_tool(state: str = "Uttar Pradesh"):
    """
    Returns mandi price data for a given state.
    """
    # return fetch_mandi_data(state)
    return """Papaya (Papaya): ₹2750 - ₹2880 (Modal: ₹2810) | Market: Badayoun, District: Badaun
Tomato (Deshi): ₹2830 - ₹3000 (Modal: ₹2895) | Market: Badayoun, District: Badaun
Wheat (Dara): ₹2450 - ₹2490 (Modal: ₹2470) | Market: Dataganj, District: Badaun
Apple (Delicious): ₹12850 - ₹13200 (Modal: ₹13000) | Market: Wazirganj, District: Badaun
Cabbage (Cabbage): ₹1350 - ₹1425 (Modal: ₹1400) | Market: Wazirganj, District: Badaun
Green Chilli (Green Chilly): ₹4025 - ₹4100 (Modal: ₹4060) | Market: Wazirganj, District: Badaun
Onion (Red): ₹1425 - ₹1475 (Modal: ₹1440) | Market: Wazirganj, District: Badaun
Onion (Red): ₹1300 - ₹1340 (Modal: ₹1315) | Market: Wazirganj, District: Badaun
Papaya (Papaya): ₹2750 - ₹2825 (Modal: ₹2800) | Market: Wazirganj, District: Badaun
Wheat (Dara): ₹2490 - ₹2540 (Modal: ₹2500) | Market: Wazirganj, District: Badaun
Wheat (Dara): ₹2400 - ₹2450 (Modal: ₹2425) | Market: Wazirganj, District: Badaun
Onion (Red): ₹1470 - ₹1580 (Modal: ₹1540) | Market: Tulsipur, District: Balrampur
Tomato (Deshi): ₹3075 - ₹3170 (Modal: ₹3120) | Market: Tulsipur, District: Balrampur
Bottle gourd (Bottle Gourd): ₹600 - ₹800 (Modal: ₹700) | Market: Anwala, District: Bareilly
Green Chilli (Green Chilly): ₹3000 - ₹3500 (Modal: ₹3200) | Market: Anwala, District: Bareilly
Banana (Other): ₹2800 - ₹2900 (Modal: ₹2850) | Market: Bareilly, District: Bareilly
Mustard (Sarson(Black)): ₹6000 - ₹6050 (Modal: ₹6025) | Market: Bareilly, District: Bareilly
Onion (Red): ₹1300 - ₹1350 (Modal: ₹1325) | Market: Bareilly, District: Bareilly
Tomato (Local): ₹2600 - ₹2650 (Modal: ₹2625) | Market: Bareilly, District: Bareilly
Onion (Red): ₹1200 - ₹1600 (Modal: ₹1400) | Market: Anoop Shahar, District: Bulandshahar
Ridgeguard(Tori) (Other): ₹800 - ₹1200 (Modal: ₹1000) | Market: Anoop Shahar, District: Bulandshahar
Garlic (Desi): ₹5100 - ₹5300 (Modal: ₹5200) | Market: Gulavati, District: Bulandshahar
Potato (Desi): ₹900 - ₹1100 (Modal: ₹1000) | Market: Gulavati, District: Bulandshahar
Pumpkin (Other): ₹750 - ₹850 (Modal: ₹800) | Market: Gulavati, District: Bulandshahar
Brinjal (Round/Long): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Sikarpur, District: Bulandshahar
Paddy(Dhan)(Basmati) (1121): ₹2800 - ₹3000 (Modal: ₹2900) | Market: Sikarpur, District: Bulandshahar
Sponge gourd (Sponge gourd): ₹1400 - ₹1600 (Modal: ₹1500) | Market: Sikarpur, District: Bulandshahar
Garlic (Average): ₹16000 - ₹17400 (Modal: ₹16800) | Market: Siyana, District: Bulandshahar
Brinjal (Round/Long): ₹1200 - ₹1400 (Modal: ₹1250) | Market: Awagarh, District: Etah
Maize (Yellow): ₹1750 - ₹1850 (Modal: ₹1800) | Market: Shikohabad, District: Firozabad
Potato (Desi): ₹700 - ₹800 (Modal: ₹750) | Market: Shadabad, District: Hathras
Ginger(Green) (Green Ginger): ₹3620 - ₹3820 (Modal: ₹3720) | Market: Mugrabaadshahpur, District: Jaunpur
Gur(Jaggery) (Red): ₹4565 - ₹4765 (Modal: ₹4665) | Market: Mugrabaadshahpur, District: Jaunpur
Onion (Red): ₹1310 - ₹1510 (Modal: ₹1410) | Market: Mugrabaadshahpur, District: Jaunpur
Pumpkin (Pumpkin): ₹1425 - ₹1625 (Modal: ₹1525) | Market: Mugrabaadshahpur, District: Jaunpur
Bottle gourd (Bottle Gourd): ₹1630 - ₹1670 (Modal: ₹1650) | Market: Maigalganj, District: Khiri (Lakhimpur)
Onion (Red): ₹2400 - ₹2500 (Modal: ₹2460) | Market: Maigalganj, District: Khiri (Lakhimpur)
Potato (Red): ₹1500 - ₹2000 (Modal: ₹1800) | Market: Anandnagar, District: Maharajganj
Rice (III): ₹2800 - ₹3200 (Modal: ₹3000) | Market: Anandnagar, District: Maharajganj
Wheat (Dara): ₹2425 - ₹2450 (Modal: ₹2450) | Market: Anandnagar, District: Maharajganj
Bitter gourd (Bitter Gourd): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Gadaura, District: Maharajganj
Ginger(Green) (Green Ginger): ₹1100 - ₹1300 (Modal: ₹1200) | Market: Gadaura, District: Maharajganj
Jack Fruit (Other): ₹2000 - ₹2200 (Modal: ₹2100) | Market: Gadaura, District: Maharajganj
Sponge gourd (Other): ₹1100 - ₹1300 (Modal: ₹1200) | Market: Gadaura, District: Maharajganj
Apple (Delicious): ₹9400 - ₹9600 (Modal: ₹9500) | Market: Nautnava, District: Maharajganj
Onion (Red): ₹900 - ₹1000 (Modal: ₹950) | Market: Nautnava, District: Maharajganj
Green Chilli (Green Chilly): ₹4900 - ₹5000 (Modal: ₹4950) | Market: Doharighat, District: Mau(Maunathbhanjan)
Rice (1009 Kar): ₹3900 - ₹4000 (Modal: ₹3960) | Market: Doharighat, District: Mau(Maunathbhanjan)
Apple (Delicious): ₹8100 - ₹8300 (Modal: ₹8200) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Banana (Medium): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Cucumbar(Kheera) (Cucumbar): ₹1000 - ₹1300 (Modal: ₹1100) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Green Chilli (Green Chilly): ₹1800 - ₹2000 (Modal: ₹1900) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Banana - Green (Banana - Green): ₹1100 - ₹1200 (Modal: ₹1150) | Market: Sardhana, District: Meerut
Onion (Red): ₹1500 - ₹1600 (Modal: ₹1550) | Market: Sardhana, District: Meerut
Cauliflower (Cauliflower): ₹1600 - ₹1800 (Modal: ₹1700) | Market: Ahirora, District: Mirzapur
Cowpea(Veg) (Cowpea (Veg)): ₹2000 - ₹2200 (Modal: ₹2100) | Market: Ahirora, District: Mirzapur
Green Chilli (Green Chilly): ₹3900 - ₹4000 (Modal: ₹4000) | Market: Ahirora, District: Mirzapur
Little gourd (Kundru) (Little gourd (Kundru)): ₹1600 - ₹1800 (Modal: ₹1700) | Market: Ahirora, District: Mirzapur     
Pointed gourd (Parval) (Pointed gourd (Parval)): ₹4000 - ₹4200 (Modal: ₹4100) | Market: Ahirora, District: Mirzapur   
Bottle gourd (Bottle Gourd): ₹1300 - ₹1370 (Modal: ₹1335) | Market: Puranpur, District: Pillibhit
Green Chilli (Green Chilly): ₹4050 - ₹4135 (Modal: ₹4095) | Market: Puranpur, District: Pillibhit
Papaya (Papaya): ₹2790 - ₹2870 (Modal: ₹2830) | Market: Puranpur, District: Pillibhit
Potato (Potato): ₹1115 - ₹1195 (Modal: ₹1150) | Market: Puranpur, District: Pillibhit
Tomato (Local): ₹2850 - ₹2940 (Modal: ₹2895) | Market: Puranpur, District: Pillibhit
Tomato (Local): ₹2750 - ₹2835 (Modal: ₹2790) | Market: Puranpur, District: Pillibhit
Wheat (Dara): ₹2515 - ₹2600 (Modal: ₹2555) | Market: Puranpur, District: Pillibhit
Wheat (Dara): ₹2415 - ₹2495 (Modal: ₹2450) | Market: Puranpur, District: Pillibhit
Arhar Dal(Tur Dal) (Arhar Dal(Tur)): ₹9975 - ₹10100 (Modal: ₹10000) | Market: Bachranwa, District: Raebarelli
Bottle gourd (Bottle Gourd): ₹1450 - ₹1550 (Modal: ₹1500) | Market: Bachranwa, District: Raebarelli
Gur(Jaggery) (Red): ₹4375 - ₹4415 (Modal: ₹4400) | Market: Bachranwa, District: Raebarelli
Onion (Red): ₹1350 - ₹1400 (Modal: ₹1365) | Market: Bachranwa, District: Raebarelli
Paddy(Dhan)(Common) (Common): ₹2320 - ₹2500 (Modal: ₹2400) | Market: Lalganj, District: Raebarelli
Onion (Red): ₹1350 - ₹1400 (Modal: ₹1380) | Market: Raibareilly, District: Raebarelli
Spinach (Spinach): ₹1550 - ₹1650 (Modal: ₹1600) | Market: Raibareilly, District: Raebarelli
Sponge gourd (Sponge gourd): ₹1550 - ₹1650 (Modal: ₹1600) | Market: Raibareilly, District: Raebarelli
Colacasia (Colacasia): ₹1400 - ₹1600 (Modal: ₹1500) | Market: Chutmalpur, District: Saharanpur
Potato (Potato): ₹1300 - ₹1500 (Modal: ₹1400) | Market: Chutmalpur, District: Saharanpur
Raddish (Raddish): ₹1750 - ₹1950 (Modal: ₹1850) | Market: Chutmalpur, District: Saharanpur
Bottle gourd (Bottle Gourd): ₹600 - ₹700 (Modal: ₹650) | Market: Sambhal, District: Sambhal
Cauliflower (Cauliflower): ₹1000 - ₹1300 (Modal: ₹1250) | Market: Sambhal, District: Sambhal
Onion (Red): ₹1250 - ₹1400 (Modal: ₹1300) | Market: Khalilabad, District: Sant Kabir Nagar
Maize (Yellow): ₹1930 - ₹1960 (Modal: ₹1950) | Market: Tilhar, District: Shahjahanpur
Onion (Red): ₹1390 - ₹1470 (Modal: ₹1430) | Market: Tilhar, District: Shahjahanpur
Tomato (Deshi): ₹2840 - ₹2940 (Modal: ₹2890) | Market: Tilhar, District: Shahjahanpur
Mango (Dusheri): ₹1500 - ₹1600 (Modal: ₹1550) | Market: Kairana, District: Shamli
Pomegranate (Pomogranate): ₹7540 - ₹7560 (Modal: ₹7550) | Market: Naugarh, District: Siddharth Nagar
Potato (Local): ₹800 - ₹840 (Modal: ₹820) | Market: Hargaon (Laharpur), District: Sitapur
Potato (Desi): ₹1225 - ₹1300 (Modal: ₹1260) | Market: Purwa, District: Unnao
Tomato (Hybrid): ₹2825 - ₹2950 (Modal: ₹2875) | Market: Unnao, District: Unnao
Apple (Delicious): ₹13200 - ₹13500 (Modal: ₹13350) | Market: Fatehpur Sikri, District: Agra
Banana (Banana - Ripe): ₹2500 - ₹2700 (Modal: ₹2570) | Market: Fatehpur Sikri, District: Agra
Cauliflower (Cauliflower): ₹3450 - ₹3650 (Modal: ₹3540) | Market: Fatehpur Sikri, District: Agra
Ginger(Green) (Green Ginger): ₹3050 - ₹3250 (Modal: ₹3145) | Market: Fatehpur Sikri, District: Agra
Gur(Jaggery) (Red): ₹4380 - ₹4500 (Modal: ₹4450) | Market: Fatehpur Sikri, District: Agra
Potato (Local): ₹1000 - ₹1250 (Modal: ₹1100) | Market: Fatehpur Sikri, District: Agra
Sponge gourd (Sponge gourd): ₹1000 - ₹1100 (Modal: ₹1050) | Market: Atrauli, District: Aligarh
Bajra(Pearl Millet/Cumbu) (Hybrid): ₹1750 - ₹2100 (Modal: ₹1850) | Market: Khair, District: Aligarh
Ginger(Green) (Green Ginger): ₹3200 - ₹3800 (Modal: ₹3500) | Market: Khair, District: Aligarh
Green Chilli (Green Chilly): ₹4500 - ₹5000 (Modal: ₹4800) | Market: Khair, District: Aligarh
Onion (Red): ₹1200 - ₹1600 (Modal: ₹1400) | Market: Khair, District: Aligarh
Tomato (Hybrid): ₹2800 - ₹3500 (Modal: ₹3000) | Market: Khair, District: Aligarh
Brinjal (Brinjal): ₹1880 - ₹1925 (Modal: ₹1900) | Market: Sultanpur, District: Amethi
Cucumbar(Kheera) (Cucumbar): ₹2170 - ₹2225 (Modal: ₹2200) | Market: Sultanpur, District: Amethi
Ginger(Green) (Green Ginger): ₹3730 - ₹3780 (Modal: ₹3750) | Market: Sultanpur, District: Amethi
Green Chilli (Green Chilly): ₹4450 - ₹4525 (Modal: ₹4500) | Market: Sultanpur, District: Amethi
Mousambi(Sweet Lime) (Mousambi): ₹3380 - ₹3425 (Modal: ₹3400) | Market: Sultanpur, District: Amethi
Onion (Red): ₹1435 - ₹1460 (Modal: ₹1445) | Market: Sultanpur, District: Amethi
Pomegranate (Pomogranate): ₹7480 - ₹7535 (Modal: ₹7500) | Market: Sultanpur, District: Amethi
Apple (Delicious): ₹9200 - ₹10000 (Modal: ₹9500) | Market: Hasanpur, District: Amroha
Bottle gourd (Bottle Gourd): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Capsicum (Capsicum): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Pumpkin (Pumpkin): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Wood (Eucalyptus): ₹580 - ₹600 (Modal: ₹590) | Market: Babrala, District: Badaun
Banana - Green (Banana - Green): ₹1770 - ₹1900 (Modal: ₹1815) | Market: Badayoun, District: Badaun
Garlic (Garlic): ₹6400 - ₹6530 (Modal: ₹6465) | Market: Badayoun, District: Badaun
Gur(Jaggery) (Red): ₹4250 - ₹4360 (Modal: ₹4295) | Market: Badayoun, District: Badaun
Lemon (Lemon): ₹4850 - ₹5100 (Modal: ₹5010) | Market: Badayoun, District: Badaun
Paddy(Dhan)(Common) (Sarvati): ₹2070 - ₹2180 (Modal: ₹2100) | Market: Badayoun, District: Badaun
Potato (Desi): ₹1180 - ₹1300 (Modal: ₹1230) | Market: Badayoun, District: Badaun
Maize (Hybrid): ₹1900 - ₹1970 (Modal: ₹1950) | Market: Dataganj, District: Badaun
Bhindi(Ladies Finger) (Bhindi): ₹1800 - ₹1850 (Modal: ₹1825) | Market: Wazirganj, District: Badaun
Brinjal (Round/Long): ₹1625 - ₹1675 (Modal: ₹1660) | Market: Wazirganj, District: Badaun
Jack Fruit (Jack Fruit): ₹1700 - ₹1750 (Modal: ₹1730) | Market: Wazirganj, District: Badaun
Brinjal (Round/Long): ₹1780 - ₹1870 (Modal: ₹1820) | Market: Tulsipur, District: Balrampur
Onion (Red): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Anwala, District: Bareilly
Ridgeguard(Tori) (Ridgeguard(Tori)): ₹1000 - ₹1500 (Modal: ₹1200) | Market: Anwala, District: Bareilly
Tomato (Deshi): ₹3000 - ₹3500 (Modal: ₹3200) | Market: Anwala, District: Bareilly
Apple (Apple): ₹12950 - ₹13000 (Modal: ₹12975) | Market: Bareilly, District: Bareilly
Cauliflower (Cauliflower): ₹2750 - ₹2800 (Modal: ₹2760) | Market: Bareilly, District: Bareilly
Garlic (Average): ₹6500 - ₹6550 (Modal: ₹6525) | Market: Bareilly, District: Bareilly
Ginger(Green) (Green Ginger): ₹4025 - ₹4075 (Modal: ₹4060) | Market: Bareilly, District: Bareilly
Lentil (Masur)(Whole) (Masoor Gola): ₹6700 - ₹6750 (Modal: ₹6725) | Market: Bareilly, District: Bareilly
Mousambi(Sweet Lime) (Mousambi): ₹3550 - ₹3600 (Modal: ₹3575) | Market: Bareilly, District: Bareilly
Onion (Red): ₹1400 - ₹1450 (Modal: ₹1425) | Market: Bareilly, District: Bareilly
Papaya (Papaya): ₹2775 - ₹2850 (Modal: ₹2800) | Market: Bareilly, District: Bareilly
Pomegranate (Pomogranate): ₹7425 - ₹7500 (Modal: ₹7475) | Market: Bareilly, District: Bareilly
Pumpkin (Pumpkin): ₹1200 - ₹1225 (Modal: ₹1210) | Market: Bareilly, District: Bareilly
Tomato (Local): ₹2775 - ₹2850 (Modal: ₹2800) | Market: Bareilly, District: Bareilly
Potato (Desi): ₹1100 - ₹1300 (Modal: ₹1200) | Market: Chaandpur, District: Bijnor
Bottle gourd (Bottle Gourd): ₹600 - ₹1000 (Modal: ₹800) | Market: Anoop Shahar, District: Bulandshahar
Pumpkin (Pumpkin): ₹600 - ₹1000 (Modal: ₹800) | Market: Anoop Shahar, District: Bulandshahar
Tomato (Deshi): ₹4100 - ₹4500 (Modal: ₹4300) | Market: Anoop Shahar, District: Bulandshahar
Bottle gourd (Bottle Gourd): ₹1300 - ₹1400 (Modal: ₹1350) | Market: Sikarpur, District: Bulandshahar
Garlic (Garlic): ₹7000 - ₹7200 (Modal: ₹7100) | Market: Sikarpur, District: Bulandshahar
Ginger(Green) (Green Ginger): ₹4800 - ₹5000 (Modal: ₹4900) | Market: Sikarpur, District: Bulandshahar
Potato (Potato): ₹850 - ₹1100 (Modal: ₹1000) | Market: Sikarpur, District: Bulandshahar
Apple (Red  Gold): ₹6200 - ₹6400 (Modal: ₹6300) | Market: Siyana, District: Bulandshahar
Mango (Dusheri): ₹1600 - ₹1700 (Modal: ₹1650) | Market: Siyana, District: Bulandshahar
Onion (Red): ₹1400 - ₹1500 (Modal: ₹1450) | Market: Siyana, District: Bulandshahar
Bottle gourd (Bottle Gourd): ₹1000 - ₹1250 (Modal: ₹1100) | Market: Awagarh, District: Etah
Cabbage (Cabbage): ₹1000 - ₹1250 (Modal: ₹1100) | Market: Awagarh, District: Etah
Maize (Yellow): ₹2000 - ₹2050 (Modal: ₹2025) | Market: Jasvantnagar, District: Etawah
Potato (Potato): ₹1100 - ₹1300 (Modal: ₹1200) | Market: Jasvantnagar, District: Etawah
Onion (Red): ₹1200 - ₹1300 (Modal: ₹1250) | Market: Shadabad, District: Hathras
Bhindi(Ladies Finger) (Bhindi): ₹1780 - ₹1980 (Modal: ₹1880) | Market: Mugrabaadshahpur, District: Jaunpur
Lentil (Masur)(Whole) (Kala Masoor New): ₹6745 - ₹6945 (Modal: ₹6845) | Market: Mugrabaadshahpur, District: Jaunpur   
Mustard (Sarson(Black)): ₹6700 - ₹6900 (Modal: ₹6800) | Market: Mugrabaadshahpur, District: Jaunpur
Tomato (Deshi): ₹2985 - ₹3185 (Modal: ₹3085) | Market: Mugrabaadshahpur, District: Jaunpur
Potato (Desi): ₹750 - ₹850 (Modal: ₹800) | Market: Rura, District: Kanpur Dehat
Onion (Red): ₹1260 - ₹1450 (Modal: ₹1355) | Market: Manjhanpur, District: Kaushambi
Cabbage (Cabbage): ₹1400 - ₹1470 (Modal: ₹1450) | Market: Maigalganj, District: Khiri (Lakhimpur)
Pumpkin (Pumpkin): ₹2400 - ₹2470 (Modal: ₹2460) | Market: Maigalganj, District: Khiri (Lakhimpur)
Apple (Delicious): ₹7500 - ₹8500 (Modal: ₹8000) | Market: Anandnagar, District: Maharajganj
Banana - Green (Banana - Green): ₹1600 - ₹1800 (Modal: ₹1700) | Market: Anandnagar, District: Maharajganj
Papaya (Papaya): ₹2000 - ₹2400 (Modal: ₹2200) | Market: Anandnagar, District: Maharajganj
Tomato (Deshi): ₹2500 - ₹3000 (Modal: ₹2800) | Market: Anandnagar, District: Maharajganj
Pumpkin (Other): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Gadaura, District: Maharajganj
Tomato (Hybrid): ₹2400 - ₹2600 (Modal: ₹2500) | Market: Gadaura, District: Maharajganj
Ginger(Green) (Green Ginger): ₹2100 - ₹2300 (Modal: ₹2200) | Market: Nautnava, District: Maharajganj
Green Chilli (Green Chilly): ₹1500 - ₹1800 (Modal: ₹1600) | Market: Nautnava, District: Maharajganj
Mango (Dusheri): ₹1100 - ₹1500 (Modal: ₹1200) | Market: Nautnava, District: Maharajganj
Pumpkin (Pumpkin): ₹500 - ₹600 (Modal: ₹550) | Market: Nautnava, District: Maharajganj
Lemon (Lemon): ₹3700 - ₹3800 (Modal: ₹3755) | Market: Doharighat, District: Mau(Maunathbhanjan)
Bitter gourd (Bitter Gourd): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Cauliflower (Cauliflower): ₹1200 - ₹1300 (Modal: ₹1250) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Tomato (Hybrid): ₹1400 - ₹1700 (Modal: ₹1500) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Bhindi(Ladies Finger) (Bhindi): ₹1000 - ₹1500 (Modal: ₹1500) | Market: Ahirora, District: Mirzapur
Potato (Badshah): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Ahirora, District: Mirzapur
Raddish (Raddish): ₹1400 - ₹1500 (Modal: ₹1500) | Market: Ahirora, District: Mirzapur
Apple (Delicious): ₹12910 - ₹12990 (Modal: ₹12950) | Market: Puranpur, District: Pillibhit
Bhindi(Ladies Finger) (Bhindi): ₹1810 - ₹1890 (Modal: ₹1850) | Market: Puranpur, District: Pillibhit
Potato (Desi): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Sirsa, District: Prayagraj
Rice (Common): ₹3100 - ₹3200 (Modal: ₹3150) | Market: Lalganj, District: Raebarelli
Tomato (Hybrid): ₹2300 - ₹2500 (Modal: ₹2400) | Market: Lalganj, District: Raebarelli
Ginger(Green) (Green Ginger): ₹3800 - ₹3900 (Modal: ₹3850) | Market: Raibareilly, District: Raebarelli
Papaya (Papaya): ₹2700 - ₹2750 (Modal: ₹2725) | Market: Raibareilly, District: Raebarelli
Wheat (Dara): ₹2460 - ₹2480 (Modal: ₹2470) | Market: Raibareilly, District: Raebarelli
Ridgeguard(Tori) (Ridgeguard(Tori)): ₹800 - ₹1000 (Modal: ₹900) | Market: Chutmalpur, District: Saharanpur
Tomato (Deshi): ₹1900 - ₹2100 (Modal: ₹2000) | Market: Chutmalpur, District: Saharanpur
Maize (Yellow): ₹1600 - ₹2000 (Modal: ₹1800) | Market: Bhehjoi, District: Sambhal
Apple (Delicious): ₹8500 - ₹9500 (Modal: ₹9000) | Market: Sambhal, District: Sambhal
Potato (Desi): ₹600 - ₹1350 (Modal: ₹1000) | Market: Sambhal, District: Sambhal
Wheat (Dara): ₹2450 - ₹2470 (Modal: ₹2460) | Market: Tilhar, District: Shahjahanpur
Bottle gourd (Bottle Gourd): ₹800 - ₹900 (Modal: ₹850) | Market: Kairana, District: Shamli
Cucumbar(Kheera) (Cucumbar): ₹1500 - ₹1600 (Modal: ₹1550) | Market: Kairana, District: Shamli
Green Chilli (Green Chilly): ₹2500 - ₹2600 (Modal: ₹2550) | Market: Kairana, District: Shamli
Onion (Red): ₹1200 - ₹1300 (Modal: ₹1250) | Market: Kairana, District: Shamli
Tomato (Hybrid): ₹2900 - ₹3000 (Modal: ₹2950) | Market: Kairana, District: Shamli
Bengal Gram(Gram)(Whole) (Desi (Whole)): ₹6620 - ₹6650 (Modal: ₹6630) | Market: Naugarh, District: Siddharth Nagar    
Bottle gourd (Bottle Gourd): ₹1440 - ₹1460 (Modal: ₹1450) | Market: Naugarh, District: Siddharth Nagar
Green Chilli (Green Chilly): ₹4240 - ₹4260 (Modal: ₹4250) | Market: Naugarh, District: Siddharth Nagar
Onion (Red): ₹1385 - ₹1395 (Modal: ₹1390) | Market: Naugarh, District: Siddharth Nagar
Pointed gourd (Parval) (Pointed gourd (Parval)): ₹2620 - ₹2660 (Modal: ₹2650) | Market: Naugarh, District: Siddharth Nagar
Rice (III): ₹3240 - ₹3260 (Modal: ₹3250) | Market: Naugarh, District: Siddharth Nagar
Wheat (Dara): ₹2515 - ₹2560 (Modal: ₹2530) | Market: Naugarh, District: Siddharth Nagar
Firewood (Other): ₹300 - ₹340 (Modal: ₹320) | Market: Hargaon (Laharpur), District: Sitapur
Pumpkin (Pumpkin): ₹800 - ₹820 (Modal: ₹810) | Market: Hargaon (Laharpur), District: Sitapur
Bottle gourd (Bottle Gourd): ₹1150 - ₹1400 (Modal: ₹1250) | Market: Fatehpur Sikri, District: Agra
Brinjal (Round): ₹1600 - ₹1750 (Modal: ₹1670) | Market: Fatehpur Sikri, District: Agra
Onion (Red): ₹1300 - ₹1450 (Modal: ₹1370) | Market: Fatehpur Sikri, District: Agra
Potato (Desi): ₹1000 - ₹1120 (Modal: ₹1080) | Market: Aligarh, District: Aligarh
Apple (Delicious): ₹12650 - ₹12725 (Modal: ₹12700) | Market: Sultanpur, District: Amethi
Black Gram Dal (Urd Dal) (Black Gram Dal): ₹9960 - ₹9995 (Modal: ₹9980) | Market: Sultanpur, District: Amethi
Lemon (Lemon): ₹4780 - ₹4850 (Modal: ₹4800) | Market: Sultanpur, District: Amethi
Potato (Desi): ₹1000 - ₹1025 (Modal: ₹1015) | Market: Sultanpur, District: Amethi
Bhindi(Ladies Finger) (Bhindi): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Cucumbar(Kheera) (Cucumbar): ₹1810 - ₹2000 (Modal: ₹1850) | Market: Hasanpur, District: Amroha
Guava (Guava): ₹2100 - ₹3000 (Modal: ₹2520) | Market: Hasanpur, District: Amroha
Raddish (Other): ₹900 - ₹1000 (Modal: ₹950) | Market: Hasanpur, District: Amroha
Maize (Deshi Red): ₹1970 - ₹1990 (Modal: ₹1980) | Market: Babrala, District: Badaun
Bottle gourd (Bottle Gourd): ₹1330 - ₹1430 (Modal: ₹1395) | Market: Badayoun, District: Badaun
Cucumbar(Kheera) (Cucumbar): ₹1980 - ₹2100 (Modal: ₹2030) | Market: Badayoun, District: Badaun
Ginger(Green) (Green Ginger): ₹4150 - ₹4300 (Modal: ₹4215) | Market: Badayoun, District: Badaun
Potato (Desi): ₹1100 - ₹1180 (Modal: ₹1150) | Market: Badayoun, District: Badaun
Potato (Other): ₹700 - ₹700 (Modal: ₹700) | Market: Visoli, District: Badaun
Bottle gourd (Bottle Gourd): ₹1325 - ₹1375 (Modal: ₹1350) | Market: Wazirganj, District: Badaun
Colacasia (Colacasia): ₹2425 - ₹2475 (Modal: ₹2475) | Market: Wazirganj, District: Badaun
Potato (Desi): ₹1175 - ₹1250 (Modal: ₹1210) | Market: Wazirganj, District: Badaun
Ridgeguard(Tori) (Ridgeguard(Tori)): ₹1650 - ₹1725 (Modal: ₹1675) | Market: Wazirganj, District: Badaun
Brinjal (Brinjal): ₹800 - ₹1000 (Modal: ₹900) | Market: Anwala, District: Bareilly
Pumpkin (Pumpkin): ₹800 - ₹1200 (Modal: ₹1000) | Market: Anwala, District: Bareilly
Bottle gourd (Bottle Gourd): ₹1300 - ₹1350 (Modal: ₹1325) | Market: Bareilly, District: Bareilly
Brinjal (Round/Long): ₹1600 - ₹1650 (Modal: ₹1635) | Market: Bareilly, District: Bareilly
Lentil (Masur)(Whole) (Masoor Gola): ₹6800 - ₹6850 (Modal: ₹6825) | Market: Bareilly, District: Bareilly
Onion (Red): ₹900 - ₹1100 (Modal: ₹1000) | Market: Chaandpur, District: Bijnor
Colacasia (Other): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Gulavati, District: Bulandshahar
Onion (Red): ₹1500 - ₹1700 (Modal: ₹1600) | Market: Gulavati, District: Bulandshahar
Sponge gourd (Other): ₹1300 - ₹1500 (Modal: ₹1400) | Market: Gulavati, District: Bulandshahar
Onion (Red): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Sikarpur, District: Bulandshahar
Tomato (Deshi): ₹2300 - ₹2500 (Modal: ₹2400) | Market: Sikarpur, District: Bulandshahar
Wheat (Dara): ₹2500 - ₹2535 (Modal: ₹2520) | Market: Sikarpur, District: Bulandshahar
Bottle gourd (Bottle Gourd): ₹950 - ₹1060 (Modal: ₹1000) | Market: Siyana, District: Bulandshahar
Cauliflower (Cauliflower): ₹1000 - ₹1100 (Modal: ₹1050) | Market: Siyana, District: Bulandshahar
Cucumbar(Kheera) (Cucumbar): ₹800 - ₹900 (Modal: ₹850) | Market: Siyana, District: Bulandshahar
Pumpkin (Pumpkin): ₹900 - ₹1000 (Modal: ₹950) | Market: Siyana, District: Bulandshahar
Tomato (Local): ₹2800 - ₹2900 (Modal: ₹2850) | Market: Siyana, District: Bulandshahar
Onion (Red): ₹1425 - ₹1445 (Modal: ₹1430) | Market: Devariya, District: Deoria
Maize (Hybrid): ₹1950 - ₹1965 (Modal: ₹1960) | Market: Aliganj, District: Etah
Mustard (Sarson(Black)): ₹6000 - ₹6100 (Modal: ₹6010) | Market: Aliganj, District: Etah
Wheat (Dara): ₹2450 - ₹2465 (Modal: ₹2455) | Market: Aliganj, District: Etah
Banana - Green (Banana - Green): ₹1400 - ₹1600 (Modal: ₹1500) | Market: Awagarh, District: Etah
Cauliflower (Cauliflower): ₹1800 - ₹2100 (Modal: ₹1900) | Market: Awagarh, District: Etah
Onion (Red): ₹1000 - ₹1150 (Modal: ₹1100) | Market: Shikohabad, District: Firozabad
Rice (III): ₹2900 - ₹3000 (Modal: ₹2950) | Market: Yusufpur, District: Ghazipur
Tomato (Deshi): ₹2500 - ₹2600 (Modal: ₹2550) | Market: Shadabad, District: Hathras
Wheat (Dara): ₹2480 - ₹2500 (Modal: ₹2485) | Market: Ait, District: Jalaun (Orai)
Apple (Delicious): ₹13100 - ₹13300 (Modal: ₹13200) | Market: Mugrabaadshahpur, District: Jaunpur
Green Chilli (Green Chilly): ₹4835 - ₹5035 (Modal: ₹4935) | Market: Mugrabaadshahpur, District: Jaunpur
Raddish (Raddish): ₹2285 - ₹2485 (Modal: ₹2385) | Market: Mugrabaadshahpur, District: Jaunpur
Rice (Common): ₹3315 - ₹3515 (Modal: ₹3415) | Market: Mugrabaadshahpur, District: Jaunpur
Potato (Desi): ₹700 - ₹1000 (Modal: ₹900) | Market: Bharwari, District: Kaushambi
Wheat (Dara): ₹2450 - ₹2550 (Modal: ₹2500) | Market: Bharwari, District: Kaushambi
Potato (Desi): ₹1125 - ₹1280 (Modal: ₹1200) | Market: Manjhanpur, District: Kaushambi
Tomato (Deshi): ₹2840 - ₹3075 (Modal: ₹2955) | Market: Manjhanpur, District: Kaushambi
Apple (Kasmir/Shimla - II): ₹7800 - ₹7860 (Modal: ₹7830) | Market: Maigalganj, District: Khiri (Lakhimpur)
Potato (Desi): ₹1640 - ₹1700 (Modal: ₹1670) | Market: Maigalganj, District: Khiri (Lakhimpur)
Wheat (Dara): ₹2400 - ₹2500 (Modal: ₹2440) | Market: Maigalganj, District: Khiri (Lakhimpur)
Green Chilli (Green Chilly): ₹2800 - ₹3200 (Modal: ₹3000) | Market: Anandnagar, District: Maharajganj
Bottle gourd (Bottle Gourd): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Gadaura, District: Maharajganj
Garlic (Garlic): ₹3200 - ₹3400 (Modal: ₹3300) | Market: Gadaura, District: Maharajganj
Green Chilli (Green Chilly): ₹2000 - ₹2200 (Modal: ₹2100) | Market: Gadaura, District: Maharajganj
Onion (Red): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Gadaura, District: Maharajganj
Brinjal (Round/Long): ₹1400 - ₹1600 (Modal: ₹1500) | Market: Nautnava, District: Maharajganj
Potato (Desi): ₹800 - ₹900 (Modal: ₹850) | Market: Nautnava, District: Maharajganj
Rice (III): ₹2800 - ₹3150 (Modal: ₹2960) | Market: Nautnava, District: Maharajganj
Onion (Red): ₹1285 - ₹1485 (Modal: ₹1385) | Market: Ghiraur, District: Mainpuri
Cauliflower (Other): ₹1400 - ₹1500 (Modal: ₹1460) | Market: Doharighat, District: Mau(Maunathbhanjan)
Potato (Potato): ₹1700 - ₹1800 (Modal: ₹1745) | Market: Doharighat, District: Mau(Maunathbhanjan)
Bhindi(Ladies Finger) (Bhindi): ₹900 - ₹1000 (Modal: ₹950) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Bottle gourd (Bottle Gourd): ₹1000 - ₹1100 (Modal: ₹1050) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Green Chilli (Green Chilly): ₹1400 - ₹1600 (Modal: ₹1500) | Market: Sardhana, District: Meerut
Bottle gourd (Bottle Gourd): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Ahirora, District: Mirzapur
Cabbage (Cabbage): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Ahirora, District: Mirzapur
Cucumbar(Kheera) (Cucumbar): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Ahirora, District: Mirzapur
Colacasia (Colacasia): ₹2535 - ₹2610 (Modal: ₹2575) | Market: Puranpur, District: Pillibhit
Mousambi(Sweet Lime) (Mousambi): ₹3510 - ₹3590 (Modal: ₹3550) | Market: Puranpur, District: Pillibhit
Onion (Red): ₹1390 - ₹1465 (Modal: ₹1425) | Market: Puranpur, District: Pillibhit
Potato (Potato): ₹1215 - ₹1300 (Modal: ₹1255) | Market: Puranpur, District: Pillibhit
Pumpkin (Pumpkin): ₹1230 - ₹1310 (Modal: ₹1270) | Market: Puranpur, District: Pillibhit
Bengal Gram Dal (Chana Dal) (Bengal Gram Dal): ₹7500 - ₹7515 (Modal: ₹7510) | Market: Bachranwa, District: Raebarelli 
Jack Fruit (Jack Fruit): ₹1400 - ₹1475 (Modal: ₹1450) | Market: Bachranwa, District: Raebarelli
Potato (Desi): ₹1225 - ₹1250 (Modal: ₹1245) | Market: Bachranwa, District: Raebarelli
Wheat (Dara): ₹2475 - ₹2515 (Modal: ₹2500) | Market: Bachranwa, District: Raebarelli
Onion (Red): ₹1150 - ₹1250 (Modal: ₹1200) | Market: Lalganj, District: Raebarelli
Potato (Desi): ₹900 - ₹1000 (Modal: ₹950) | Market: Lalganj, District: Raebarelli
Wheat (Dara): ₹2450 - ₹2575 (Modal: ₹2500) | Market: Lalganj, District: Raebarelli
Barley (Jau) (Dara): ₹2320 - ₹2330 (Modal: ₹2325) | Market: Raibareilly, District: Raebarelli
Bhindi(Ladies Finger) (Bhindi): ₹1500 - ₹1550 (Modal: ₹1510) | Market: Raibareilly, District: Raebarelli
Bottle gourd (Bottle Gourd): ₹1500 - ₹1550 (Modal: ₹1530) | Market: Raibareilly, District: Raebarelli
Colacasia (Colacasia): ₹2175 - ₹2225 (Modal: ₹2200) | Market: Raibareilly, District: Raebarelli
Garlic (Garlic): ₹6200 - ₹6400 (Modal: ₹6300) | Market: Raibareilly, District: Raebarelli
Jack Fruit (Jack Fruit): ₹1375 - ₹1425 (Modal: ₹1400) | Market: Raibareilly, District: Raebarelli
Mustard Oil (Mustard Oil): ₹14750 - ₹14850 (Modal: ₹14800) | Market: Raibareilly, District: Raebarelli
Paddy(Dhan)(Common) (Common): ₹2255 - ₹2310 (Modal: ₹2300) | Market: Raibareilly, District: Raebarelli
Potato (Desi): ₹1170 - ₹1220 (Modal: ₹1200) | Market: Raibareilly, District: Raebarelli
Rice (Common): ₹3135 - ₹3150 (Modal: ₹3140) | Market: Raibareilly, District: Raebarelli
Brinjal (Brinjal): ₹800 - ₹900 (Modal: ₹850) | Market: Chutmalpur, District: Saharanpur
Cabbage (Cabbage): ₹400 - ₹600 (Modal: ₹500) | Market: Chutmalpur, District: Saharanpur
Wood (Eucalyptus): ₹500 - ₹510 (Modal: ₹505) | Market: Bhehjoi, District: Sambhal
Brinjal (Round/Long): ₹700 - ₹800 (Modal: ₹750) | Market: Sambhal, District: Sambhal
Tomato (Deshi): ₹1000 - ₹1400 (Modal: ₹1200) | Market: Sambhal, District: Sambhal
Bottle gourd (Bottle Gourd): ₹1100 - ₹1200 (Modal: ₹1150) | Market: Khalilabad, District: Sant Kabir Nagar
Cauliflower (Cauliflower): ₹1900 - ₹2050 (Modal: ₹1975) | Market: Khalilabad, District: Sant Kabir Nagar
Maize (Yellow): ₹1970 - ₹2000 (Modal: ₹2000) | Market: Tilhar, District: Shahjahanpur
Wheat (Dara): ₹2480 - ₹2520 (Modal: ₹2500) | Market: Tilhar, District: Shahjahanpur
Potato (Desi): ₹1240 - ₹1260 (Modal: ₹1250) | Market: Naugarh, District: Siddharth Nagar
Tomato (Deshi): ₹2840 - ₹2860 (Modal: ₹2850) | Market: Naugarh, District: Siddharth Nagar
Onion (Nasik): ₹1000 - ₹1100 (Modal: ₹1050) | Market: Hargaon (Laharpur), District: Sitapur
Wood (Other): ₹500 - ₹600 (Modal: ₹550) | Market: Hargaon (Laharpur), District: Sitapur
Onion (Red): ₹1300 - ₹1380 (Modal: ₹1340) | Market: Unnao, District: Unnao
Green Chilli (Green Chilly): ₹4800 - ₹5000 (Modal: ₹4900) | Market: Fatehpur Sikri, District: Agra
Lemon (Lemon): ₹3300 - ₹3450 (Modal: ₹3370) | Market: Fatehpur Sikri, District: Agra
Mango (Dusheri): ₹4150 - ₹4400 (Modal: ₹4240) | Market: Fatehpur Sikri, District: Agra
Brinjal (Brinjal): ₹1200 - ₹1300 (Modal: ₹1250) | Market: Atrauli, District: Aligarh
Maize (Hybrid): ₹1900 - ₹2000 (Modal: ₹1950) | Market: Atrauli, District: Aligarh
Pumpkin (Pumpkin): ₹700 - ₹800 (Modal: ₹750) | Market: Atrauli, District: Aligarh
Bitter gourd (Bitter Gourd): ₹2500 - ₹3000 (Modal: ₹2800) | Market: Khair, District: Aligarh
Paddy(Dhan)(Basmati) (Basmati 1509): ₹2650 - ₹2950 (Modal: ₹2800) | Market: Khair, District: Aligarh
Wheat (Dara): ₹2475 - ₹2543 (Modal: ₹2500) | Market: Khair, District: Aligarh
Arhar Dal(Tur Dal) (Arhar Dal(Tur)): ₹10280 - ₹10335 (Modal: ₹10300) | Market: Sultanpur, District: Amethi
Capsicum (Capsicum): ₹4280 - ₹4380 (Modal: ₹4300) | Market: Sultanpur, District: Amethi
Onion (Red): ₹1250 - ₹1300 (Modal: ₹1270) | Market: Sultanpur, District: Amethi
Tomato (Deshi): ₹3050 - ₹3095 (Modal: ₹3080) | Market: Sultanpur, District: Amethi
Cauliflower (Local): ₹2100 - ₹3000 (Modal: ₹2520) | Market: Hasanpur, District: Amroha
Ginger(Green) (Green Ginger): ₹3210 - ₹4000 (Modal: ₹3520) | Market: Hasanpur, District: Amroha
Mousambi(Sweet Lime) (Mousambi): ₹2100 - ₹3000 (Modal: ₹2500) | Market: Hasanpur, District: Amroha
Potato (Potato): ₹810 - ₹1000 (Modal: ₹850) | Market: Hasanpur, District: Amroha
Cabbage (Cabbage): ₹1340 - ₹1480 (Modal: ₹1400) | Market: Badayoun, District: Badaun
Green Chilli (Green Chilly): ₹4050 - ₹4200 (Modal: ₹4120) | Market: Badayoun, District: Badaun
Onion (Nasik): ₹1380 - ₹1500 (Modal: ₹1425) | Market: Badayoun, District: Badaun
Tomato (Deshi): ₹2650 - ₹2830 (Modal: ₹2720) | Market: Badayoun, District: Badaun
Wheat (Dara): ₹2450 - ₹2560 (Modal: ₹2500) | Market: Badayoun, District: Badaun
Potato (Desi): ₹1100 - ₹1125 (Modal: ₹1110) | Market: Wazirganj, District: Badaun
Pumpkin (Pumpkin): ₹1350 - ₹1375 (Modal: ₹1360) | Market: Wazirganj, District: Badaun
Tomato (Deshi): ₹2850 - ₹2900 (Modal: ₹2875) | Market: Wazirganj, District: Badaun
Tomato (Deshi): ₹2750 - ₹2800 (Modal: ₹2775) | Market: Wazirganj, District: Badaun
Pumpkin (Pumpkin): ₹1450 - ₹1550 (Modal: ₹1500) | Market: Tulsipur, District: Balrampur
Cucumbar(Kheera) (Cucumbar): ₹3000 - ₹3500 (Modal: ₹3200) | Market: Anwala, District: Bareilly
Potato (Potato): ₹1000 - ₹1050 (Modal: ₹1025) | Market: Bareilly, District: Bareilly
Tomato (Hybrid): ₹1500 - ₹1700 (Modal: ₹1600) | Market: Chaandpur, District: Bijnor
Brinjal (Round/Long): ₹800 - ₹1200 (Modal: ₹1000) | Market: Anoop Shahar, District: Bulandshahar
Cucumbar(Kheera) (Cucumbar): ₹1600 - ₹2000 (Modal: ₹1800) | Market: Anoop Shahar, District: Bulandshahar
Green Chilli (Green Chilly): ₹4200 - ₹4600 (Modal: ₹4400) | Market: Anoop Shahar, District: Bulandshahar
Potato (F.A.Q.): ₹800 - ₹1200 (Modal: ₹1000) | Market: Anoop Shahar, District: Bulandshahar
Bhindi(Ladies Finger) (Other): ₹2100 - ₹2300 (Modal: ₹2200) | Market: Gulavati, District: Bulandshahar
Brinjal (Other): ₹700 - ₹900 (Modal: ₹800) | Market: Gulavati, District: Bulandshahar
Cucumbar(Kheera) (Cucumbar): ₹1300 - ₹1500 (Modal: ₹1400) | Market: Gulavati, District: Bulandshahar
Green Chilli (Green Chilly): ₹1500 - ₹1700 (Modal: ₹1600) | Market: Gulavati, District: Bulandshahar
Lemon (Other): ₹8100 - ₹8300 (Modal: ₹8200) | Market: Gulavati, District: Bulandshahar
Bitter gourd (Bitter Gourd): ₹2400 - ₹2500 (Modal: ₹2450) | Market: Sikarpur, District: Bulandshahar
Cabbage (Cabbage): ₹2900 - ₹3000 (Modal: ₹2950) | Market: Sikarpur, District: Bulandshahar
Cauliflower (Cauliflower): ₹2900 - ₹3000 (Modal: ₹2950) | Market: Sikarpur, District: Bulandshahar
Lemon (Lemon): ₹4600 - ₹4800 (Modal: ₹4700) | Market: Sikarpur, District: Bulandshahar
Raddish (Raddish): ₹2200 - ₹2400 (Modal: ₹2300) | Market: Sikarpur, District: Bulandshahar
Paddy(Dhan)(Basmati) (Basmati 1509): ₹3100 - ₹3200 (Modal: ₹3150) | Market: Siyana, District: Bulandshahar
Potato (Desi): ₹950 - ₹1100 (Modal: ₹1060) | Market: Siyana, District: Bulandshahar
Wheat (Dara): ₹2500 - ₹2520 (Modal: ₹2510) | Market: Siyana, District: Bulandshahar
Potato (Potato): ₹1220 - ₹1240 (Modal: ₹1230) | Market: Devariya, District: Deoria
Bajra(Pearl Millet/Cumbu) (Deshi): ₹2100 - ₹2115 (Modal: ₹2105) | Market: Aliganj, District: Etah
Onion (Red): ₹1470 - ₹1570 (Modal: ₹1520) | Market: Jasvantnagar, District: Etawah
Tomato (Hybrid): ₹3370 - ₹3470 (Modal: ₹3420) | Market: Jasvantnagar, District: Etawah
Green Chilli (Green Chilly): ₹1200 - ₹1300 (Modal: ₹1250) | Market: Jamanian, District: Ghazipur
Bajra(Pearl Millet/Cumbu) (Deshi): ₹2140 - ₹2375 (Modal: ₹2260) | Market: Sikandraraau, District: Hathras
Maize (Yellow): ₹1750 - ₹1820 (Modal: ₹1800) | Market: Sikandraraau, District: Hathras
Wheat (Dara): ₹2460 - ₹2490 (Modal: ₹2485) | Market: Sikandraraau, District: Hathras
Bengal Gram(Gram)(Whole) (Desi (Whole)): ₹6540 - ₹6740 (Modal: ₹6640) | Market: Mugrabaadshahpur, District: Jaunpur
Bitter gourd (Bitter Gourd): ₹2485 - ₹2685 (Modal: ₹2585) | Market: Mugrabaadshahpur, District: Jaunpur
Bottle gourd (Bottle Gourd): ₹1555 - ₹1755 (Modal: ₹1655) | Market: Mugrabaadshahpur, District: Jaunpur
Brinjal (Brinjal): ₹1680 - ₹1880 (Modal: ₹1780) | Market: Mugrabaadshahpur, District: Jaunpur
Cucumbar(Kheera) (Cucumbar): ₹2170 - ₹2370 (Modal: ₹2270) | Market: Mugrabaadshahpur, District: Jaunpur
Garlic (Average): ₹6350 - ₹6550 (Modal: ₹6450) | Market: Mugrabaadshahpur, District: Jaunpur
Potato (Badshah): ₹1110 - ₹1310 (Modal: ₹1210) | Market: Mugrabaadshahpur, District: Jaunpur
Wheat (Dara): ₹2435 - ₹2635 (Modal: ₹2535) | Market: Mugrabaadshahpur, District: Jaunpur
Brinjal (Other): ₹1740 - ₹1800 (Modal: ₹1769) | Market: Maigalganj, District: Khiri (Lakhimpur)
Garlic (Garlic): ₹2500 - ₹2590 (Modal: ₹2560) | Market: Maigalganj, District: Khiri (Lakhimpur)
Gur(Jaggery) (Pathari): ₹3400 - ₹3470 (Modal: ₹3450) | Market: Maigalganj, District: Khiri (Lakhimpur)
Lemon (Lemon): ₹4000 - ₹4070 (Modal: ₹4030) | Market: Maigalganj, District: Khiri (Lakhimpur)
Mango (Dusheri): ₹1600 - ₹1700 (Modal: ₹1650) | Market: Maigalganj, District: Khiri (Lakhimpur)
Gur(Jaggery) (Red): ₹4000 - ₹4500 (Modal: ₹4200) | Market: Anandnagar, District: Maharajganj
Onion (Red): ₹1200 - ₹1600 (Modal: ₹1400) | Market: Anandnagar, District: Maharajganj
Potato (Red): ₹1100 - ₹1300 (Modal: ₹1200) | Market: Gadaura, District: Maharajganj
Garlic (Average): ₹2300 - ₹2500 (Modal: ₹2400) | Market: Nautnava, District: Maharajganj
Mousambi(Sweet Lime) (Mousambi): ₹2500 - ₹2800 (Modal: ₹2650) | Market: Nautnava, District: Maharajganj
Masur Dal (Kala Masoor New): ₹9000 - ₹9100 (Modal: ₹9070) | Market: Doharighat, District: Mau(Maunathbhanjan)
Brinjal (Brinjal): ₹900 - ₹1100 (Modal: ₹1000) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Onion (Red): ₹1500 - ₹1600 (Modal: ₹1550) | Market: Sardhana, District: Meerut
Banana (Banana - Ripe): ₹4000 - ₹4500 (Modal: ₹4500) | Market: Ahirora, District: Mirzapur
Onion (Red): ₹700 - ₹900 (Modal: ₹800) | Market: Ahirora, District: Mirzapur
Sponge gourd (Sponge gourd): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Ahirora, District: Mirzapur
Banana (Banana - Ripe): ₹2810 - ₹2890 (Modal: ₹2850) | Market: Puranpur, District: Pillibhit
Brinjal (Brinjal): ₹1610 - ₹1685 (Modal: ₹1650) | Market: Puranpur, District: Pillibhit
Lemon (Lemon): ₹5030 - ₹5100 (Modal: ₹5070) | Market: Puranpur, District: Pillibhit
Onion (Red): ₹1100 - ₹1300 (Modal: ₹1200) | Market: Sirsa, District: Prayagraj
Paddy(Dhan)(Common) (Common): ₹2275 - ₹2315 (Modal: ₹2300) | Market: Bachranwa, District: Raebarelli
Rice (Common): ₹3135 - ₹3165 (Modal: ₹3150) | Market: Bachranwa, District: Raebarelli
Tomato (Hybrid): ₹2800 - ₹2900 (Modal: ₹2850) | Market: Bachranwa, District: Raebarelli
Apple (Kasmir/Shimla - II): ₹12400 - ₹12550 (Modal: ₹12500) | Market: Raibareilly, District: Raebarelli
Arhar Dal(Tur Dal) (Arhar Dal(Tur)): ₹9900 - ₹9950 (Modal: ₹9930) | Market: Raibareilly, District: Raebarelli
Bitter gourd (Bitter Gourd): ₹2200 - ₹2250 (Modal: ₹2210) | Market: Raibareilly, District: Raebarelli
Black Gram (Urd Beans)(Whole) (Black Gram (Whole)): ₹8750 - ₹8780 (Modal: ₹8760) | Market: Raibareilly, District: Raebarelli
Cucumbar(Kheera) (Cucumbar): ₹1950 - ₹2050 (Modal: ₹2000) | Market: Raibareilly, District: Raebarelli
Lemon (Lemon): ₹4400 - ₹4520 (Modal: ₹4500) | Market: Raibareilly, District: Raebarelli
Mousambi(Sweet Lime) (Mousambi): ₹3200 - ₹3300 (Modal: ₹3250) | Market: Raibareilly, District: Raebarelli
Pomegranate (Pomogranate): ₹7200 - ₹7350 (Modal: ₹7300) | Market: Raibareilly, District: Raebarelli
Pumpkin (Pumpkin): ₹1475 - ₹1525 (Modal: ₹1500) | Market: Raibareilly, District: Raebarelli
Tomato (Hybrid): ₹2750 - ₹2850 (Modal: ₹2800) | Market: Raibareilly, District: Raebarelli
Banana (Banana - Ripe): ₹2000 - ₹2400 (Modal: ₹2200) | Market: Vilaspur, District: Rampur
Bhindi(Ladies Finger) (Bhindi): ₹800 - ₹1000 (Modal: ₹900) | Market: Chutmalpur, District: Saharanpur
Bitter gourd (Bitter Gourd): ₹800 - ₹900 (Modal: ₹850) | Market: Chutmalpur, District: Saharanpur
Bottle gourd (Bottle Gourd): ₹800 - ₹1000 (Modal: ₹900) | Market: Chutmalpur, District: Saharanpur
Cucumbar(Kheera) (Cucumbar): ₹1400 - ₹1600 (Modal: ₹1500) | Market: Chutmalpur, District: Saharanpur
Jack Fruit (Jack Fruit): ₹750 - ₹950 (Modal: ₹850) | Market: Chutmalpur, District: Saharanpur
Lemon (Lemon): ₹2350 - ₹2550 (Modal: ₹2450) | Market: Chutmalpur, District: Saharanpur
Pumpkin (Pumpkin): ₹750 - ₹950 (Modal: ₹850) | Market: Chutmalpur, District: Saharanpur
Wheat (Dara): ₹2500 - ₹2510 (Modal: ₹2505) | Market: Bhehjoi, District: Sambhal
Onion (Red): ₹1200 - ₹1650 (Modal: ₹1400) | Market: Sambhal, District: Sambhal
Brinjal (Brinjal): ₹700 - ₹800 (Modal: ₹750) | Market: Khalilabad, District: Sant Kabir Nagar
Potato (Desi): ₹1800 - ₹2000 (Modal: ₹1900) | Market: Khalilabad, District: Sant Kabir Nagar
Onion (Red): ₹1350 - ₹1380 (Modal: ₹1370) | Market: Tilhar, District: Shahjahanpur
Potato (Desi): ₹1150 - ₹1180 (Modal: ₹1170) | Market: Tilhar, District: Shahjahanpur
Bhindi(Ladies Finger) (Bhindi): ₹1300 - ₹1400 (Modal: ₹1350) | Market: Kairana, District: Shamli
Potato (Desi): ₹1000 - ₹1100 (Modal: ₹1050) | Market: Kairana, District: Shamli
Banana - Green (Banana - Green): ₹1810 - ₹1860 (Modal: ₹1820) | Market: Naugarh, District: Siddharth Nagar
Brinjal (Round/Long): ₹1810 - ₹1830 (Modal: ₹1820) | Market: Naugarh, District: Siddharth Nagar
Gur(Jaggery) (Red): ₹4210 - ₹4280 (Modal: ₹4250) | Market: Naugarh, District: Siddharth Nagar
Mousambi(Sweet Lime) (Mousambi): ₹3520 - ₹3560 (Modal: ₹3530) | Market: Naugarh, District: Siddharth Nagar
Peas(Dry) (Peas(Dry)): ₹4240 - ₹4260 (Modal: ₹4250) | Market: Naugarh, District: Siddharth Nagar
Banana (Desi(Bontha)): ₹1100 - ₹1200 (Modal: ₹1150) | Market: Hargaon (Laharpur), District: Sitapur
Gur(Jaggery) (Yellow): ₹3000 - ₹3200 (Modal: ₹3100) | Market: Hargaon (Laharpur), District: Sitapur
Wheat (Dara): ₹2450 - ₹2460 (Modal: ₹2455) | Market: Hargaon (Laharpur), District: Sitapur
Tomato (Hybrid): ₹3240 - ₹3360 (Modal: ₹3350) | Market: Aligarh, District: Aligarh
Bottle gourd (Bottle Gourd): ₹1100 - ₹1200 (Modal: ₹1150) | Market: Atrauli, District: Aligarh
Colacasia (Colacasia): ₹2100 - ₹2200 (Modal: ₹2150) | Market: Atrauli, District: Aligarh
Cucumbar(Kheera) (Cucumbar): ₹1000 - ₹1100 (Modal: ₹1050) | Market: Atrauli, District: Aligarh
Potato (Desi): ₹900 - ₹1000 (Modal: ₹950) | Market: Atrauli, District: Aligarh
Wheat (Dara): ₹2400 - ₹2500 (Modal: ₹2450) | Market: Atrauli, District: Aligarh
Bottle gourd (Bottle Gourd): ₹1000 - ₹1400 (Modal: ₹1200) | Market: Khair, District: Aligarh
Brinjal (Round/Long): ₹1400 - ₹2000 (Modal: ₹1800) | Market: Khair, District: Aligarh
Cauliflower (Cauliflower): ₹4500 - ₹5500 (Modal: ₹5000) | Market: Khair, District: Aligarh
Cucumbar(Kheera) (Cucumbar): ₹1200 - ₹2000 (Modal: ₹1800) | Market: Khair, District: Aligarh
Garlic (Garlic): ₹4500 - ₹6000 (Modal: ₹5500) | Market: Khair, District: Aligarh
Maize (Hybrid/Local): ₹1700 - ₹1950 (Modal: ₹1850) | Market: Khair, District: Aligarh
Potato (Desi): ₹800 - ₹1000 (Modal: ₹900) | Market: Khair, District: Aligarh
Banana - Green (Banana - Green): ₹1785 - ₹1825 (Modal: ₹1800) | Market: Sultanpur, District: Amethi
Bhindi(Ladies Finger) (Bhindi): ₹1880 - ₹1925 (Modal: ₹1900) | Market: Sultanpur, District: Amethi
Bitter gourd (Bitter Gourd): ₹2070 - ₹2180 (Modal: ₹2100) | Market: Sultanpur, District: Amethi
Bottle gourd (Bottle Gourd): ₹1480 - ₹1525 (Modal: ₹1500) | Market: Sultanpur, District: Amethi
Pointed gourd (Parval) (Pointed gourd (Parval)): ₹2580 - ₹2635 (Modal: ₹2600) | Market: Sultanpur, District: Amethi   
Rice (Common): ₹3260 - ₹3300 (Modal: ₹3280) | Market: Sultanpur, District: Amethi
Tomato (Deshi): ₹2850 - ₹2895 (Modal: ₹2870) | Market: Sultanpur, District: Amethi
Banana (Other): ₹2100 - ₹3000 (Modal: ₹2520) | Market: Hasanpur, District: Amroha
Cabbage (Cabbage): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Green Chilli (Green Chilly): ₹1810 - ₹2000 (Modal: ₹1850) | Market: Hasanpur, District: Amroha
Mango (Badami): ₹1810 - ₹2000 (Modal: ₹1850) | Market: Hasanpur, District: Amroha
Papaya (Papaya): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Ridgeguard(Tori) (Other): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Spinach (Other): ₹1410 - ₹1500 (Modal: ₹1450) | Market: Hasanpur, District: Amroha
Tomato (Deshi): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Hasanpur, District: Amroha
Bhindi(Ladies Finger) (Bhindi): ₹1780 - ₹1910 (Modal: ₹1830) | Market: Badayoun, District: Badaun
Bitter gourd (Bitter Gourd): ₹2090 - ₹2210 (Modal: ₹2130) | Market: Badayoun, District: Badaun
Brinjal (Brinjal): ₹1650 - ₹1790 (Modal: ₹1710) | Market: Badayoun, District: Badaun
Onion (Nasik): ₹1300 - ₹1380 (Modal: ₹1350) | Market: Badayoun, District: Badaun
Pumpkin (Pumpkin): ₹1370 - ₹1500 (Modal: ₹1420) | Market: Badayoun, District: Badaun
Raddish (Raddish): ₹2100 - ₹2230 (Modal: ₹2165) | Market: Badayoun, District: Badaun
Rice (III): ₹3360 - ₹3450 (Modal: ₹3395) | Market: Badayoun, District: Badaun
Ridgeguard(Tori) (Ridgeguard(Tori)): ₹1750 - ₹1890 (Modal: ₹1810) | Market: Badayoun, District: Badaun
Maize (Other): ₹2000 - ₹2225 (Modal: ₹2225) | Market: Visoli, District: Badaun
Cucumbar(Kheera) (Cucumbar): ₹2000 - ₹2025 (Modal: ₹2025) | Market: Wazirganj, District: Badaun
Lemon (Lemon): ₹5000 - ₹5075 (Modal: ₹5025) | Market: Wazirganj, District: Badaun
Mango (Dusheri): ₹3000 - ₹3100 (Modal: ₹3060) | Market: Wazirganj, District: Badaun
Rice (III): ₹3375 - ₹3425 (Modal: ₹3400) | Market: Wazirganj, District: Badaun
Apple (Kasmir/Shimla - II): ₹13250 - ₹13750 (Modal: ₹13500) | Market: Tulsipur, District: Balrampur
Bottle gourd (Bottle Gourd): ₹2530 - ₹2620 (Modal: ₹2580) | Market: Tulsipur, District: Balrampur
Green Chilli (Green Chilly): ₹5780 - ₹5880 (Modal: ₹5830) | Market: Tulsipur, District: Balrampur
Potato (Desi): ₹1050 - ₹1150 (Modal: ₹1100) | Market: Tulsipur, District: Balrampur
Potato (Desi): ₹800 - ₹1000 (Modal: ₹900) | Market: Anwala, District: Bareilly
Cucumbar(Kheera) (Cucumbar): ₹1850 - ₹1925 (Modal: ₹1890) | Market: Bareilly, District: Bareilly
Green Chilli (Other): ₹4025 - ₹4100 (Modal: ₹4065) | Market: Bareilly, District: Bareilly
Gur(Jaggery) (Red): ₹4025 - ₹4075 (Modal: ₹4060) | Market: Bareilly, District: Bareilly
Mustard (Sarson(Black)): ₹6150 - ₹6225 (Modal: ₹6200) | Market: Bareilly, District: Bareilly
Potato (Potato): ₹1125 - ₹1175 (Modal: ₹1145) | Market: Bareilly, District: Bareilly
Rice (Common): ₹3400 - ₹3450 (Modal: ₹3435) | Market: Bareilly, District: Bareilly
Wheat (Dara): ₹2500 - ₹2550 (Modal: ₹2525) | Market: Bareilly, District: Bareilly
Wheat (Dara): ₹2425 - ₹2475 (Modal: ₹2450) | Market: Bareilly, District: Bareilly
Colacasia (Colacasia): ₹1800 - ₹2200 (Modal: ₹2000) | Market: Anoop Shahar, District: Bulandshahar
Ginger(Green) (Green Ginger): ₹4800 - ₹5200 (Modal: ₹5000) | Market: Anoop Shahar, District: Bulandshahar
Raddish (Raddish): ₹600 - ₹1000 (Modal: ₹800) | Market: Anoop Shahar, District: Bulandshahar
Wheat (Dara): ₹2520 - ₹2540 (Modal: ₹2530) | Market: Anoop Shahar, District: Bulandshahar
Bitter gourd (Bitter Gourd): ₹1500 - ₹1700 (Modal: ₹1600) | Market: Gulavati, District: Bulandshahar
Bottle gourd (Bottle Gourd): ₹1000 - ₹1200 (Modal: ₹1100) | Market: Gulavati, District: Bulandshahar
Ginger(Green) (Green Ginger): ₹6100 - ₹6300 (Modal: ₹6200) | Market: Gulavati, District: Bulandshahar
Bhindi(Ladies Finger) (Bhindi): ₹1400 - ₹1500 (Modal: ₹1450) | Market: Sikarpur, District: Bulandshahar
Cucumbar(Kheera) (Cucumbar): ₹2800 - ₹3000 (Modal: ₹2900) | Market: Sikarpur, District: Bulandshahar
Green Chilli (Green Chilly): ₹3000 - ₹3200 (Modal: ₹3100) | Market: Sikarpur, District: Bulandshahar
Pumpkin (Pumpkin): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Sikarpur, District: Bulandshahar
Colacasia (Colacasia): ₹950 - ₹1050 (Modal: ₹1000) | Market: Siyana, District: Bulandshahar
Gur(Jaggery) (Yellow): ₹3100 - ₹3300 (Modal: ₹3200) | Market: Siyana, District: Bulandshahar
Maize (Yellow): ₹2235 - ₹2245 (Modal: ₹2240) | Market: Siyana, District: Bulandshahar
Mousambi(Sweet Lime) (Mousambi): ₹1900 - ₹2000 (Modal: ₹1950) | Market: Siyana, District: Bulandshahar
Papaya (Papaya): ₹1700 - ₹1800 (Modal: ₹1750) | Market: Siyana, District: Bulandshahar
Pomegranate (Pomogranate): ₹4800 - ₹5000 (Modal: ₹4900) | Market: Siyana, District: Bulandshahar
Tomato (Hybrid): ₹3010 - ₹3025 (Modal: ₹3015) | Market: Devariya, District: Deoria
Bhindi(Ladies Finger) (Bhindi): ₹1000 - ₹1250 (Modal: ₹1100) | Market: Awagarh, District: Etah
Green Gram (Moong)(Whole) (Local (Whole)): ₹6600 - ₹6900 (Modal: ₹6800) | Market: Shikohabad, District: Firozabad     
Potato (Potato): ₹700 - ₹700 (Modal: ₹700) | Market: Shikohabad, District: Firozabad
Wheat (Dara): ₹2500 - ₹2600 (Modal: ₹2550) | Market: Yusufpur, District: Ghazipur
Bengal Gram Dal (Chana Dal) (Bengal Gram (Split)): ₹7370 - ₹7570 (Modal: ₹7470) | Market: Mugrabaadshahpur, District: Jaunpur
Pomegranate (Pomogranate): ₹7385 - ₹7585 (Modal: ₹7485) | Market: Mugrabaadshahpur, District: Jaunpur
White Peas (White Peas): ₹4145 - ₹4345 (Modal: ₹4245) | Market: Mugrabaadshahpur, District: Jaunpur
Bhindi(Ladies Finger) (Other): ₹2100 - ₹2160 (Modal: ₹2130) | Market: Maigalganj, District: Khiri (Lakhimpur)
Green Chilli (Green Chilly): ₹2900 - ₹3000 (Modal: ₹2950) | Market: Maigalganj, District: Khiri (Lakhimpur)
Tomato (Local): ₹2400 - ₹2490 (Modal: ₹2440) | Market: Maigalganj, District: Khiri (Lakhimpur)
Bhindi(Ladies Finger) (Bhindi): ₹1100 - ₹1300 (Modal: ₹1200) | Market: Gadaura, District: Maharajganj
Banana - Green (Banana - Green): ₹1200 - ₹1400 (Modal: ₹1300) | Market: Nautnava, District: Maharajganj
Gur(Jaggery) (Red): ₹3000 - ₹3200 (Modal: ₹3100) | Market: Nautnava, District: Maharajganj
Tomato (Hybrid): ₹1500 - ₹1800 (Modal: ₹1600) | Market: Nautnava, District: Maharajganj
Wheat (Dara): ₹2400 - ₹2500 (Modal: ₹2450) | Market: Nautnava, District: Maharajganj
Potato (Local): ₹955 - ₹1155 (Modal: ₹1055) | Market: Ghiraur, District: Mainpuri
Tomato (Hybrid): ₹2810 - ₹3010 (Modal: ₹2910) | Market: Ghiraur, District: Mainpuri
Gur(Jaggery) (Achhu): ₹5400 - ₹5500 (Modal: ₹5460) | Market: Doharighat, District: Mau(Maunathbhanjan)
Onion (Red): ₹1900 - ₹2000 (Modal: ₹1975) | Market: Doharighat, District: Mau(Maunathbhanjan)
Tomato (Deshi): ₹1900 - ₹2000 (Modal: ₹1950) | Market: Doharighat, District: Mau(Maunathbhanjan)
Onion (Red): ₹1300 - ₹1500 (Modal: ₹1400) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Potato (Desi): ₹800 - ₹1000 (Modal: ₹950) | Market: Kopaganj, District: Mau(Maunathbhanjan)
Apple (Delicious): ₹15000 - ₹16000 (Modal: ₹15000) | Market: Ahirora, District: Mirzapur
Brinjal (Brinjal): ₹2000 - ₹2200 (Modal: ₹2100) | Market: Ahirora, District: Mirzapur
Ginger(Green) (Green Ginger): ₹3000 - ₹4500 (Modal: ₹4000) | Market: Ahirora, District: Mirzapur
Cucumbar(Kheera) (Cucumbar): ₹1850 - ₹1935 (Modal: ₹1895) | Market: Puranpur, District: Pillibhit
Onion (Red): ₹1290 - ₹1360 (Modal: ₹1320) | Market: Puranpur, District: Pillibhit
Rice (III): ₹3420 - ₹3500 (Modal: ₹3460) | Market: Puranpur, District: Pillibhit
Fish (Bata Putti): ₹3200 - ₹3400 (Modal: ₹3300) | Market: Sirsa, District: Prayagraj
Tomato (Deshi): ₹2300 - ₹2500 (Modal: ₹2400) | Market: Sirsa, District: Prayagraj
Wheat (Dara): ₹2450 - ₹2700 (Modal: ₹2600) | Market: Sirsa, District: Prayagraj
Bhindi(Ladies Finger) (Bhindi): ₹1400 - ₹1600 (Modal: ₹1500) | Market: Lalganj, District: Raebarelli
Colacasia (Colacasia): ₹1900 - ₹2100 (Modal: ₹2000) | Market: Lalganj, District: Raebarelli
Green Chilli (Green Chilly): ₹3000 - ₹3200 (Modal: ₹3100) | Market: Lalganj, District: Raebarelli
Banana (Banana - Ripe): ₹2650 - ₹2750 (Modal: ₹2700) | Market: Raibareilly, District: Raebarelli
Bengal Gram(Gram)(Whole) (Desi (Whole)): ₹6500 - ₹6525 (Modal: ₹6510) | Market: Raibareilly, District: Raebarelli     
Brinjal (Round/Long): ₹1600 - ₹1650 (Modal: ₹1640) | Market: Raibareilly, District: Raebarelli
Green Chilli (Green Chilly): ₹4450 - ₹4550 (Modal: ₹4500) | Market: Raibareilly, District: Raebarelli
Pointed gourd (Parval) (Pointed gourd (Parval)): ₹2675 - ₹2725 (Modal: ₹2700) | Market: Raibareilly, District: Raebarelli
Green Chilli (Green Chilly): ₹1750 - ₹1950 (Modal: ₹1850) | Market: Chutmalpur, District: Saharanpur
Mango (Raw-Ripe) (Mango - Raw-Ripe): ₹1850 - ₹2050 (Modal: ₹1975) | Market: Chutmalpur, District: Saharanpur
Spinach (Spinach): ₹1800 - ₹2000 (Modal: ₹1900) | Market: Chutmalpur, District: Saharanpur
Potato (Potato): ₹700 - ₹710 (Modal: ₹705) | Market: Bhehjoi, District: Sambhal
Bhindi(Ladies Finger) (Bhindi): ₹1400 - ₹1500 (Modal: ₹1450) | Market: Khalilabad, District: Sant Kabir Nagar
Green Chilli (Green Chilly): ₹2000 - ₹2200 (Modal: ₹2100) | Market: Khalilabad, District: Sant Kabir Nagar
Potato (Desi): ₹1190 - ₹1270 (Modal: ₹1230) | Market: Tilhar, District: Shahjahanpur
Tomato (Deshi): ₹2790 - ₹2830 (Modal: ₹2820) | Market: Tilhar, District: Shahjahanpur
Brinjal (Round/Long): ₹1300 - ₹1400 (Modal: ₹1350) | Market: Kairana, District: Shamli
Cabbage (Cabbage): ₹1900 - ₹2000 (Modal: ₹1950) | Market: Kairana, District: Shamli
Garlic (Garlic): ₹5800 - ₹5900 (Modal: ₹5850) | Market: Kairana, District: Shamli
Ginger(Green) (Green Ginger): ₹5900 - ₹6000 (Modal: ₹5950) | Market: Kairana, District: Shamli
Lemon (Lemon): ₹6000 - ₹6100 (Modal: ₹6050) | Market: Kairana, District: Shamli
Raddish (Raddish): ₹800 - ₹900 (Modal: ₹850) | Market: Kairana, District: Shamli
Apple (Delicious): ₹12400 - ₹12600 (Modal: ₹12500) | Market: Naugarh, District: Siddharth Nagar
Ginger(Green) (Green Ginger): ₹3820 - ₹3890 (Modal: ₹3860) | Market: Naugarh, District: Siddharth Nagar
Mango (Dusheri): ₹3200 - ₹3400 (Modal: ₹3300) | Market: Hargaon (Laharpur), District: Sitapur
Onion (Red): ₹1325 - ₹1425 (Modal: ₹1370) | Market: Purwa, District: Unnao
Tomato (Hybrid): ₹2840 - ₹2925 (Modal: ₹2880) | Market: Purwa, District: Unnao
Potato (Desi): ₹1200 - ₹1325 (Modal: ₹1250) | Market: Unnao, District: Unnao
Gur(Jaggery) (NO 2): ₹3400 - ₹3500 (Modal: ₹3500) | Market: Chittoor, District: Chittor
Banana (Bhushavali(Pacha)): ₹7500 - ₹10000 (Modal: ₹8500) | Market: Tirupati, District: Chittor
Banana (Amruthapani): ₹2300 - ₹3000 (Modal: ₹2800) | Market: Ravulapelem, District: East Godavari
Dry Chillies (1st Sort): ₹9000 - ₹12500 (Modal: ₹10400) | Market: Pidugurala(Palnadu), District: Guntur
Capsicum (Other): ₹6000 - ₹7000 (Modal: ₹6500) | Market: Chamba, District: Chamba
Green Chilli (Other): ₹7000 - ₹8000 (Modal: ₹7500) | Market: Chamba, District: Chamba
Pomegranate (Other): ₹10000 - ₹12000 (Modal: ₹11000) | Market: Chamba, District: Chamba
Banana (Other): ₹3000 - ₹3600 (Modal: ₹3300) | Market: Hamirpur, District: Hamirpur
Brinjal (Other): ₹3500 - ₹4000 (Modal: ₹3700) | Market: Hamirpur, District: Hamirpur
Lemon (Other): ₹5000 - ₹5500 (Modal: ₹5200) | Market: Hamirpur, District: Hamirpur
Onion (Other): ₹2000 - ₹2200 (Modal: ₹2100) | Market: Hamirpur, District: Hamirpur
Apple (Other): ₹8000 - ₹20000 (Modal: ₹12000) | Market: Dharamshala, District: Kangra
Banana (Other): ₹4500 - ₹5000 (Modal: ₹4750) | Market: Dharamshala, District: Kangra
Bottle gourd (Bottle Gourd): ₹4000 - ₹4500 (Modal: ₹4250) | Market: Dharamshala, District: Kangra
Cabbage (Other): ₹2500 - ₹3500 (Modal: ₹3000) | Market: Dharamshala, District: Kangra
Capsicum (Other): ₹7000 - ₹8500 (Modal: ₹7800) | Market: Dharamshala, District: Kangra
Carrot (Other): ₹2500 - ₹3000 (Modal: ₹2750) | Market: Dharamshala, District: Kangra
Coriander(Leaves) (Other): ₹18000 - ₹20000 (Modal: ₹19000) | Market: Dharamshala, District: Kangra
Cauliflower (Other): ₹4500 - ₹5500 (Modal: ₹5000) | Market: Kangra, District: Kangra
Colacasia (Colacasia): ₹2500 - ₹3000 (Modal: ₹2700) | Market: Kangra, District: Kangra
French Beans (Frasbean) (Other): ₹9000 - ₹10000 (Modal: ₹9500) | Market: Kangra, District: Kangra
Ginger(Green) (Other): ₹8000 - ₹9000 (Modal: ₹8500) | Market: Kangra, District: Kangra
Mango (Other): ₹5500 - ₹6000 (Modal: ₹5700) | Market: Kangra, District: Kangra
Mousambi(Sweet Lime) (Other): ₹5000 - ₹6000 (Modal: ₹5500) | Market: Kangra, District: Kangra
Pumpkin (Other): ₹1500 - ₹2000 (Modal: ₹1800) | Market: Kangra, District: Kangra
Spinach (Other): ₹3500 - ₹4000 (Modal: ₹3700) | Market: Kangra, District: Kangra
Bottle gourd (Bottle Gourd): ₹2600 - ₹3300 (Modal: ₹3000) | Market: Kangra(Baijnath), District: Kangra
Capsicum (Capsicum): ₹8000 - ₹8500 (Modal: ₹8300) | Market: Kangra(Baijnath), District: Kangra
Green Chilli (Green Chilly): ₹5800 - ₹6000 (Modal: ₹5900) | Market: Kangra(Baijnath), District: Kangra
Guava (Guava): ₹6500 - ₹6600 (Modal: ₹6600) | Market: Kangra(Baijnath), District: Kangra
Onion (Onion): ₹2200 - ₹2400 (Modal: ₹2300) | Market: Kangra(Baijnath), District: Kangra
Banana (Banana - Ripe): ₹4800 - ₹5200 (Modal: ₹5000) | Market: Kangra(Jaisinghpur), District: Kangra
Bitter gourd (Bitter Gourd): ₹4500 - ₹5500 (Modal: ₹5000) | Market: Kangra(Jaisinghpur), District: Kangra
Colacasia (Colacasia): ₹2500 - ₹2800 (Modal: ₹2600) | Market: Kangra(Jaisinghpur), District: Kangra
Garlic (Average): ₹10000 - ₹12500 (Modal: ₹11700) | Market: Kangra(Jaisinghpur), District: Kangra
Potato (Potato): ₹1800 - ₹2200 (Modal: ₹2000) | Market: Kangra(Jaisinghpur), District: Kangra
Raddish (Other): ₹1800 - ₹2500 (Modal: ₹2100) | Market: Kangra(Jaisinghpur), District: Kangra
Apple (American): ₹4000 - ₹12000 (Modal: ₹7000) | Market: Kangra(Nagrota Bagwan), District: Kangra
Bhindi(Ladies Finger) (Bhindi): ₹2800 - ₹4200 (Modal: ₹3300) | Market: Kangra(Nagrota Bagwan), District: Kangra       
Colacasia (Colacasia): ₹2500 - ₹3000 (Modal: ₹2700) | Market: Kangra(Nagrota Bagwan), District: Kangra
Ginger(Green) (Green Ginger): ₹8000 - ₹8500 (Modal: ₹8200) | Market: Kangra(Nagrota Bagwan), District: Kangra
Green Chilli (Green Chilly): ₹5000 - ₹5500 (Modal: ₹5200) | Market: Kangra(Nagrota Bagwan), District: Kangra
Pear(Marasebu) (Other): ₹5000 - ₹8000 (Modal: ₹6000) | Market: Kangra(Nagrota Bagwan), District: Kangra
Pineapple (Other): ₹3500 - ₹4000 (Modal: ₹3700) | Market: Kangra(Nagrota Bagwan), District: Kangra
Potato (Other): ₹1100 - ₹2000 (Modal: ₹1500) | Market: Kangra(Nagrota Bagwan), District: Kangra
Bhindi(Ladies Finger) (Other): ₹3500 - ₹4000 (Modal: ₹3700) | Market: Palampur, District: Kangra
Brinjal (Brinjal): ₹3500 - ₹4000 (Modal: ₹3700) | Market: Palampur, District: Kangra
Capsicum (Capsicum): ₹8000 - ₹8500 (Modal: ₹8200) | Market: Palampur, District: Kangra
Colacasia (Colacasia): ₹2200 - ₹2500 (Modal: ₹2300) | Market: Palampur, District: Kangra
Cucumbar(Kheera) (Other): ₹2000 - ₹3000 (Modal: ₹2500) | Market: Palampur, District: Kangra
Ginger(Green) (Other): ₹8000 - ₹9000 (Modal: ₹8500) | Market: Palampur, District: Kangra
Cabbage (Other): ₹800 - ₹1000 (Modal: ₹900) | Market: Kullu, District: Kullu
French Beans (Frasbean) (Other): ₹5000 - ₹8000 (Modal: ₹6500) | Market: Kullu, District: Kullu
Bottle gourd (Bottle Gourd): ₹1000 - ₹3000 (Modal: ₹1500) | Market: Mandi(Mandi), District: Mandi
Cauliflower (Cauliflower): ₹1000 - ₹4500 (Modal: ₹3500) | Market: Mandi(Mandi), District: Mandi
Colacasia (Colacasia): ₹1000 - ₹2500 (Modal: ₹2000) | Market: Mandi(Mandi), District: Mandi
Mango (Other): ₹8000 - ₹11000 (Modal: ₹10000) | Market: Mandi(Mandi), District: Mandi
Peas cod (Peas cod): ₹8000 - ₹12000 (Modal: ₹10000) | Market: Mandi(Mandi), District: Mandi
Raddish (Raddish): ₹1000 - ₹1500 (Modal: ₹1500) | Market: Mandi(Mandi), District: Mandi
Tomato (Tomato): ₹1600 - ₹4500 (Modal: ₹4000) | Market: Mandi(Mandi), District: Mandi
Bitter gourd (Other): ₹4000 - ₹4500 (Modal: ₹4200) | Market: Rohroo, District: Shimla
Pear(Marasebu) (Other): ₹1500 - ₹6000 (Modal: ₹3500) | Market: Rohroo, District: Shimla
Tomato (Deshi): ₹3000 - ₹4000 (Modal: ₹3500) | Market: Rohroo, District: Shimla
Water Melon (Other): ₹3800 - ₹4000 (Modal: ₹3900) | Market: Rohroo, District: Shimla
Coriander(Leaves) (Other): ₹5000 - ₹6000 (Modal: ₹5500) | Market: Nahan, District: Sirmore
Onion (Other): ₹1800 - ₹2200 (Modal: ₹2000) | Market: Nahan, District: Sirmore
Pumpkin (Other): ₹1800 - ₹2000 (Modal: ₹1900) | Market: Nahan, District: Sirmore
Capsicum (Other): ₹6000 - ₹8000 (Modal: ₹7000) | Market: Paonta Sahib, District: Sirmore
Pear(Marasebu) (Other): ₹6000 - ₹8000 (Modal: ₹7000) | Market: Paonta Sahib, District: Sirmore
Carrot (Other): ₹2000 - ₹3000 (Modal: ₹2500) | Market: Solan, District: Solan
Mashrooms (Other): ₹10000 - ₹15000 (Modal: ₹14000) | Market: Solan, District: Solan
Potato (Other): ₹700 - ₹1700 (Modal: ₹1600) | Market: Solan, District: Solan
Raddish (Other): ₹2500 - ₹3000 (Modal: ₹2800) | Market: Solan, District: Solan
Bhindi(Ladies Finger) (Other): ₹3000 - ₹3500 (Modal: ₹3300) | Market: Solan(Nalagarh), District: Solan
Cabbage (Other): ₹1400 - ₹2000 (Modal: ₹1700) | Market: Solan(Nalagarh), District: Solan
Capsicum (Other): ₹7000 - ₹8000 (Modal: ₹7500) | Market: Solan(Nalagarh), District: Solan
Green Chilli (Other): ₹4200 - ₹5000 (Modal: ₹4600) | Market: Solan(Nalagarh), District: Solan
Potato (Other): ₹1200 - ₹1600 (Modal: ₹1400) | Market: Solan(Nalagarh), District: Solan
Tomato (Deshi): ₹800 - ₹2400 (Modal: ₹2400) | Market: Waknaghat, District: Solan
Bhindi(Ladies Finger) (Bhindi): ₹800 - ₹1700 (Modal: ₹1100) | Market: Sendhwa(F&V), District: Badwani
Bottle gourd (Bottle Gourd): ₹600 - ₹1000 (Modal: ₹800) | Market: Sendhwa(F&V), District: Badwani
Brinjal (Round): ₹600 - ₹1000 (Modal: ₹800) | Market: Sendhwa(F&V), District: Badwani
Cabbage (Cabbage): ₹700 - ₹900 (Modal: ₹800) | Market: Sendhwa(F&V), District: Badwani
Onion (Red): ₹400 - ₹800 (Modal: ₹600) | Market: Sendhwa(F&V), District: Badwani
Sponge gourd (Sponge gourd): ₹800 - ₹1300 (Modal: ₹1000) | Market: Sendhwa(F&V), District: Badwani
Banana (Banana - Ripe): ₹1000 - ₹2160 (Modal: ₹1580) | Market: Ambajipeta, District: East Godavari
Banana (Chakkarakeli(White)): ₹2200 - ₹2800 (Modal: ₹2600) | Market: Ravulapelem, District: East Godavari
Banana (Desi(Bontha)): ₹1800 - ₹2500 (Modal: ₹2100) | Market: Ravulapelem, District: East Godavari
Lemon (Lemon): ₹900 - ₹2800 (Modal: ₹1500) | Market: Eluru, District: West Godavari
Cauliflower (Local): ₹4000 - ₹5000 (Modal: ₹4500) | Market: Bilaspur, District: Bilaspur
Lemon (Lemon): ₹5500 - ₹6000 (Modal: ₹5800) | Market: Bilaspur, District: Bilaspur
Bitter gourd (Other): ₹5500 - ₹6000 (Modal: ₹5750) | Market: Chamba, District: Chamba
Capsicum (Other): ₹9000 - ₹10000 (Modal: ₹9500) | Market: Hamirpur, District: Hamirpur
Cucumbar(Kheera) (Other): ₹1500 - ₹2000 (Modal: ₹1700) | Market: Hamirpur, District: Hamirpur
Ginger(Green) (Other): ₹10000 - ₹12000 (Modal: ₹11000) | Market: Hamirpur, District: Hamirpur
Green Chilli (Other): ₹5000 - ₹5500 (Modal: ₹5200) | Market: Hamirpur, District: Hamirpur
Mango (Safeda): ₹7000 - ₹7500 (Modal: ₹7200) | Market: Hamirpur, District: Hamirpur
Mango (Totapuri): ₹4500 - ₹5000 (Modal: ₹4700) | Market: Hamirpur, District: Hamirpur
Papaya (Other): ₹4500 - ₹4500 (Modal: ₹4500) | Market: Hamirpur, District: Hamirpur
Pineapple (Pine Apple): ₹4500 - ₹5000 (Modal: ₹4700) | Market: Hamirpur, District: Hamirpur
Brinjal (Other): ₹3500 - ₹4500 (Modal: ₹4000) | Market: Dharamshala, District: Kangra
French Beans (Frasbean) (Other): ₹8500 - ₹10000 (Modal: ₹9200) | Market: Dharamshala, District: Kangra
Garlic (Other): ₹10000 - ₹15000 (Modal: ₹12500) | Market: Dharamshala, District: Kangra
Pomegranate (Other): ₹14000 - ₹18000 (Modal: ₹16000) | Market: Dharamshala, District: Kangra
Potato (Other): ₹1200 - ₹2200 (Modal: ₹1700) | Market: Dharamshala, District: Kangra
Banana (Other): ₹4500 - ₹5000 (Modal: ₹4700) | Market: Kangra, District: Kangra
Bitter gourd (Other): ₹3500 - ₹5500 (Modal: ₹4500) | Market: Kangra, District: Kangra
Coriander(Leaves) (Other): ₹10000 - ₹18000 (Modal: ₹14000) | Market: Kangra, District: Kangra
Papaya (Other): ₹3500 - ₹4000 (Modal: ₹3700) | Market: Kangra, District: Kangra
Raddish (Other): ₹2000 - ₹2500 (Modal: ₹2200) | Market: Kangra, District: Kangra
Cucumbar(Kheera) (Cucumbar): ₹2500 - ₹2800 (Modal: ₹2600) | Market: Kangra(Baijnath), District: Kangra
Pumpkin (Other): ₹2000 - ₹2200 (Modal: ₹2100) | Market: Kangra(Baijnath), District: Kangra
Apple (Kullu Royal Delicious): ₹5000 - ₹13000 (Modal: ₹9000) | Market: Kangra(Jaisinghpur), District: Kangra
Bhindi(Ladies Finger) (Bhindi): ₹3800 - ₹4200 (Modal: ₹4000) | Market: Kangra(Jaisinghpur), District: Kangra
Ginger(Green) (Green Ginger): ₹8500 - ₹9500 (Modal: ₹9000) | Market: Kangra(Jaisinghpur), District: Kangra
Papaya (Other): ₹4800 - ₹5200 (Modal: ₹5000) | Market: Kangra(Jaisinghpur), District: Kangra
Pomegranate (Other): ₹11500 - ₹13500 (Modal: ₹12500) | Market: Kangra(Jaisinghpur), District: Kangra
Cucumbar(Kheera) (Cucumbar): ₹1500 - ₹2000 (Modal: ₹1700) | Market: Kangra(Nagrota Bagwan), District: Kangra
Lemon (Lemon): ₹5000 - ₹5500 (Modal: ₹5200) | Market: Kangra(Nagrota Bagwan), District: Kangra
Apple (Kullu Royal Delicious): ₹5000 - ₹12000 (Modal: ₹8500) | Market: Palampur, District: Kangra
Banana (Banana - Ripe): ₹4500 - ₹5000 (Modal: ₹4700) | Market: Palampur, District: Kangra
Cauliflower (Cauliflower): ₹4000 - ₹5000 (Modal: ₹4500) | Market: Palampur, District: Kangra
French Beans (Frasbean) (Other): ₹7000 - ₹8000 (Modal: ₹7500) | Market: Palampur, District: Kangra
Green Chilli (Green Chilly): ₹3000 - ₹4000 (Modal: ₹3500) | Market: Palampur, District: Kangra
Lemon (Other): ₹5000 - ₹5500 (Modal: ₹5200) | Market: Palampur, District: Kangra
Mango (Safeda): ₹7000 - ₹8000 (Modal: ₹7500) | Market: Palampur, District: Kangra
Papaya (Other): ₹4500 - ₹5000 (Modal: ₹4700) | Market: Palampur, District: Kangra
Pear(Marasebu) (Other): ₹4500 - ₹8000 (Modal: ₹6500) | Market: Palampur, District: Kangra
Peas Wet (Other): ₹10000 - ₹12000 (Modal: ₹11000) | Market: Palampur, District: Kangra
Pomegranate (Other): ₹11000 - ₹13000 (Modal: ₹12000) | Market: Palampur, District: Kangra
Bitter gourd (Other): ₹4000 - ₹6000 (Modal: ₹5000) | Market: Kullu, District: Kullu
Capsicum (Other): ₹5000 - ₹7000 (Modal: ₹6000) | Market: Kullu, District: Kullu
Carrot (Other): ₹3000 - ₹4000 (Modal: ₹3500) | Market: Kullu, District: Kullu
Mango (Other): ₹3500 - ₹7000 (Modal: ₹5500) | Market: Kullu, District: Kullu
Onion (Other): ₹2200 - ₹2400 (Modal: ₹2300) | Market: Kullu, District: Kullu
Pumpkin (Other): ₹2000 - ₹2500 (Modal: ₹2300) | Market: Kullu, District: Kullu
Raddish (Other): ₹1000 - ₹1500 (Modal: ₹1300) | Market: Kullu, District: Kullu
Apple (Other"""


news_agent = LlmAgent(
    name="news_agent",
    model="gemini-2.5-flash",
    description="Provides market news and sentiment for a location or commodity.",
    instruction="You are a search specialist. Use the google_search tool to find relevant news and market reports. Return a summary of key findings.",
    tools=[google_search],
    output_key="news_data"
)

weather_agent = LlmAgent(
    name="weather_agent",
    model="gemini-2.5-flash",
    description="Provides the 10-day weather forecast for a specific location.",
    instruction=(
        "You are a weather assistant. When given a location, "
        "use the 'google_search' tool to find the 10-day weather forecast. "
        "Summarize temperature, rain chances, and extreme weather if any."
    ),
    tools=[google_search],
    output_key="weather_data"
)

analysis_agent = LlmAgent(
    name="analysis_agent",
    model="gemini-1.5-flash",
    description=(
        "Analyzes holidays and local news to anticipate upcoming demand, such as festival or wedding seasons. "
        "Also provides mandi price data for a given state."
    ),
    instruction=(
        "You are a professional market analysis assistant. "
        "When the user asks for the price of an item, use the tools to get price and holiday information. "
        "Return price information first, followed by relevant holiday/news analysis."
    ),
    tools=[holiday_tool, mandi_tool],
    output_key="final_data"

)


gatherer = ParallelAgent(
    name="InfoGatherer",
    sub_agents=[analysis_agent, news_agent, weather_agent]
)


main_final_agent = Agent(
    name="market_final_agent",
    model="gemini-2.5-pro",
    instruction=(
        "You are a combined assistant. This is the : NEWS : {news_data} Mandi : {final_data}, Weather : {weather_data}"
        "1. First, get the market prices and holiday information. "
        "2. Second, find relevant news. "
        "3. Third, get the weather forecast. "
        "Finally, combine all the information into a comprehensive response."
    ),
)
# Root agent for app
root_agent = main_final_agent