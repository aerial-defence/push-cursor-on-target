import os
import time
import CoT

ATAK_IP = os.getenv('ATAK_IP', '192.168.1.160')
ATAK_PORT = int(os.getenv('ATAK_PORT', '4242'))
ATAK_PROTO = os.getenv('ATAK_PROTO', 'UDP')

params_1 = {  # SWX parking lot
    "lat": 54.48658,
    "lon": -1.12545,
    "uid": "Test CoT 1",
    "identity": "friend",
    "dimension": "land-unit",
    "entity": "military",
    "type": "U-C",
    "remarks": "Test Message",
    "callsign": "12345",
    "course": "0",
    "speed": "0"    
#    "type": "U-C-R-H"
}

params_2 = {  # SWX parking lot
    "lat": 54.48584,
    "lon": -1.12708,
    "uid": "Test CoT 2",
    "identity": "neutral",
    "dimension": "land-unit",
    "entity": "military",
    "type": "U-C",
    "remarks": "Test Message",
    "callsign": "67890",
    "course": "0",
    "speed": "0"    
#    "type": "U-C-R-H"
}

params_3 = {  # SWX parking lot
    "lat": 54.48530,
    "lon": -1.12599,
    "uid": "Test CoT 3",
    "identity": "suspect",
    "dimension": "land-unit",
    "entity": "military",
    "type": "U-C",
    "remarks": "Test Message",
    "callsign": "09876",
    "course": "0",
    "speed": "0"    
#    "type": "U-C-R-H"
}

for i in range(0, 10):
    params_1["lat"] = params_1["lat"] + i/10000.0
    params_1["lon"] = params_1["lon"] + i/10000.0

    params_2["lat"] = params_2["lat"] + i/10000.0
    params_2["lon"] = params_2["lon"] + i/10000.0

    params_3["lat"] = params_3["lat"] + i/10000.0
    params_3["lon"] = params_3["lon"] + i/10000.0
    
    print("Params:\n" + str(params_1))
    print("Params:\n" + str(params_2))
    print("Params:\n" + str(params_3))
    
    cot = CoT.CursorOnTarget()

    cot_1_xml = cot.atoms(params_1)
    cot_2_xml = cot.atoms(params_2)
    cot_3_xml = cot.atoms(params_3)    

    print("\nXML message:")
    print(cot_1_xml)
    print(cot_2_xml)
    print(cot_3_xml)    
    
    print("\nPushing to ATAK...")
    if ATAK_PROTO == "TCP":
        sent = cot.pushTCP(ATAK_IP, ATAK_PORT, cot_1_xml)
        sent = cot.pushTCP(ATAK_IP, ATAK_PORT, cot_2_xml)
        sent = cot.pushTCP(ATAK_IP, ATAK_PORT, cot_3_xml)        
    else:
        sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_1_xml)
        sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_2_xml)
        sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_3_xml)        
    print(str(sent) + " bytes sent to " + ATAK_IP + " on port " + str(ATAK_PORT))
    time.sleep(2)
