import csv
import json

def genStartJson(row):
    IMEI = row[0]
    VIN = row[1]
    ID_Voucher = row[2]
    ID_Trip = row[3]
    Timestamp_GMT = row[4]
    Timezone = row[5]
    Record_Type = row[6]
    Lat = row[7]
    Lon = row[8]
    Bearing = row[9]
    Num_Sat = row[10]
    Fix = row[11]
    Average_X = row[12]
    Average_Y = row[13]
    Average_Z = row[14]
    Readings_X_List = row[15]
    Readings_Y_List = row[16]
    Reading_Z_List = row[17]
    Average_Lon = row[18]
    Average_Lat = row[19]
    Average_Ver = row[20]
    Readings_Lon_List = row[21]
    Readings_Lat_List = row[22]
    Readings_Ver_List = row[23]
    Engine_Coolant_Temp = row[24]
    Engine_Rpm = row[25]
    Speed = row[26]
    Mafr = row[27]
    Road_Type = row[28]
    Road_Speed_Limit = row[29]

    start = {
        "TimeZone": Timezone,
        "Lat": Lat,
        "Lon": Lon,
        "Bearing": Bearing,
        "Num_Sat": Num_Sat,
        "Fix": Fix,
        "Average_X": Average_X,
        "Average_Y": Average_Y,
        "Average_Z": Average_Z,
        "Readings_X_List": Readings_X_List,
        "Readings_Y_List": Readings_Y_List,
        "Readings_Z_List": Reading_Z_List,
        "Average_Lon": Average_Lon,
        "Average_Lat": Average_Lat,
        "Average_Ver": Average_Ver,
        "Readings_Lon_List": Readings_Lon_List,
        "Readings_Lat_Lst": Readings_Lat_List,
        "Readings_Ver_List": Readings_Ver_List,
        "Engine_Coolant_Temp": Engine_Coolant_Temp,
        "Engine_Rpm": Engine_Rpm,
        "Speed": Speed,
        "Mafr": Mafr,
        "Road_Type": Road_Type
    }
    return json.dump(start) 
def genEndJson(arr):
    Timezone = row[5]
    Record_Type = row[6]
    Lat = row[7]
    Lon = row[8]
    Bearing = row[9]
    Num_Sat = row[10]
    Fix = row[11]
    Average_X = row[12]
    Average_Y = row[13]
    Average_Z = row[14]
    Readings_X_List = row[15]
    Readings_Y_List = row[16]
    Reading_Z_List = row[17]
    Average_Lon = row[18]
    Average_Lat = row[19]
    Average_Ver = row[20]
    Readings_Lon_List = row[21]
    Readings_Lat_List = row[22]
    Readings_Ver_List = row[23]
    Engine_Coolant_Temp = row[24]
    Engine_Rpm = row[25]
    Speed = row[26]
    Mafr = row[27]
    Road_Type = row[28]
    Road_Speed_Limit = row[29]

    end = {
        "Timezone": Timezone,
        'Lat': Lat,
        'Lon': Lon,
        'Bearing': Bearing,
        'Num_Sat': Num_Sat,
        'Fix': Fix,
        'Average_X': Average_X,
        'Average_Y': Average_Y,
        'Average_Z': Average_Z,
        'Readings_X_List': Readings_X_List,
        'Readings_Y_List': Readings_Y_List,
        'Readings_Z_List': Reading_Z_List,
        'Average_Lon': Average_Lon,
        'Average_Lat': Average_Lat,
        'Average_Ver': Average_Ver,
        'Readings_Lon_List': Readings_Lon_List,
        'Readings_Lat_Lst': Readings_Lat_List,
        'Readings_Ver_List': Readings_Ver_List,
        'Engine_Coolant_Temp': Engine_Coolant_Temp,
        'Engine_Rpm': Engine_Rpm,
        'Speed': Speed,
        'Mafr': Mafr,
        'Road_Type': Road_Type,
        'Raod_Speed_Limit': Road_Speed_Limit,
    }
    json.dump(end)

def genDriveJson(row):
    Timestamp_GMT = row[4]
    Timezone = row[5]
    Record_Type = row[6]
    Lat = row[7]
    Lon = row[8]
    Bearing = row[9]
    Num_Sat = row[10]
    Fix = row[11]
    Average_X = row[12]
    Average_Y = row[13]
    Average_Z = row[14]
    Readings_X_List = row[15]
    Readings_Y_List = row[16]
    Reading_Z_List = row[17]
    Average_Lon = row[18]
    Average_Lat = row[19]
    Average_Ver = row[20]
    Readings_Lon_List = row[21]
    Readings_Lat_List = row[22]
    Readings_Ver_List = row[23]
    Engine_Coolant_Temp = row[24]
    Engine_Rpm = row[25]
    Speed = row[26]
    Mafr = row[27]
    Road_Type = row[28]
    Road_Speed_Limit = row[29]
    
    row: {
            "TimeZone": Timezone,
            "Lat": Lat,
            "Lon": Lon,
            "Bearing": Bearing,
            "Num_Sat": Num_Sat,
            "Fix": Fix,
            "Average_X": Average_X,
            "Average_Y": Average_Y,
            "Average_Z": Average_Z,
            "Readings_X_List": Readings_X_List,
            "Readings_Y_List": Readings_Y_List,
            "Readings_Z_List": Reading_Z_List,
            "Average_Lon": Average_Lon,
            "Average_Lat": Average_Lat,
            "Average_Ver": Average_Ver,
            "Readings_Lon_List": Readings_Lon_List,
            "Readings_Lat_Lst": Readings_Lat_List,
            "Readings_Ver_List": Readings_Ver_List,
            "Engine_Coolant_Temp": Engine_Coolant_Temp,
            "Engine_Rpm": Engine_Rpm,
            "Speed": Speed,
            "Mafr": Mafr,
            "Road_Type": Road_Type
    }

currentTrip = {
    'start': {},
    'trip_record': [],
    'end': {},
}
allTrips = []
        
with open('octo-sample.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';')    
    for row in filereader:
            Record_Type = row[6]            
            if Record_Type == '240':
                currentTrip['start'] = genStartJson(row)                
            elif Record_Type == '159':
                currentTrip['trip_record'].append(genDriveJson(row))
            else:
                currentTrip['end'] = genEndJson(row)
                allTrips.append(json.dump(currentTrip))
                currentTrip = {
                    'start': {},
                    'trip_record': [],
                    'end': {},
                }
                
        # IMEI = row[0]
        # VIN = row[1]
        # ID_Voucher = row[2]
        # ID_Trip = row[3]
        # Timestamp_GMT = row[4]
        # Timezone = row[5]
        # Record_Type = row[6]
        # Lat = row[7]
        # Lon = row[8]
        # Bearing = row[9]
        # Num_Sat = row[10]
        # Fix = row[11]
        # Average_X = row[12]
        # Average_Y = row[13]
        # Average_Z = row[14]
        # Readings_X_List = row[15]
        # Readings_Y_List = row[16]
        # Reading_Z_List = row[17]
        # Average_Lon = row[18]
        # Average_Lat = row[19]
        # Average_Ver = row[20]
        # Readings_Lon_List = row[21]
        # Readings_Lat_List = row[22]
        # Readings_Ver_List = row[23]
        # Engine_Coolant_Temp = row[24]
        # Engine_Rpm = row[25]
        # Speed = row[26]
        # Mafr = row[27]
        # Road_Type = row[28]
        # Road_Speed_Limit = row[29]