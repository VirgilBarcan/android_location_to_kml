import process_input
import json
import simplekml

def read_json(file_path):
    with open(file_path) as data_file:
        data = json.load(data_file)
        return data

def json_to_kml(input_file_path, output_file_path):
    # Create an instance of Kml
    kml = simplekml.Kml(open=1)

    # Import data from JSON
    data = read_json(input_file_path)["data"]

    # Create a point for each city. The points' properties are assigned after the point is created
    datalen = len(data)
    print(datalen)

    for i in range(0, datalen):
        pnt = kml.newpoint()
        pnt.name = str(i)

        tokens = data[i]["gps"].split(';')
        lat = str(tokens[0]).replace(',', '.')
        lon = str(tokens[1]).replace(',', '.')

        acc = ""
        et = ""
        alt = ""
        vel = ""
        bear = ""

        if 'acc' in data[i]:
            acc = data[i]["acc"]

        if 'et' in data[i]:
            et = data[i]["et"]

        if 'alt' in data[i]:
            alt = data[i]["alt"]

        if 'vel' in data[i]:
            vel = data[i]["vel"]

        if 'bear' in data[i]:
            bear = data[i]["bear"]

        pnt.description = "Coords: " + lat + " " + lon + "\nacc: " + acc + "\net: " + et + \
                          "\nalt: " + alt + "\nvel: " + vel + "\nbear" + bear
        pnt.coords = [(lon, lat)]

    # Save the KML
    kml.save(output_file_path)


# Process the input
process_input.process_file('/home/virgil/workspace/PycharmProjects/android_location_to_kml/Data/LocationDataFile_2016_03_28__15_57_28.txt')

# Run function
json_to_kml('/home/virgil/workspace/PycharmProjects/android_location_to_kml/Data/LocationDataFile_2016_03_28__15_57_28.json',
            '/home/virgil/workspace/PycharmProjects/android_location_to_kml/Output/2016_03_28__15_57_28.kml')

# Process the input
process_input.process_file('/home/virgil/workspace/PycharmProjects/android_location_to_kml/Data/LocationDataFile_2016_03_28__16_22_43.txt')
# Run function
json_to_kml('/home/virgil/workspace/PycharmProjects/android_location_to_kml/Data/LocationDataFile_2016_03_28__16_22_43.json',
            '/home/virgil/workspace/PycharmProjects/android_location_to_kml/Output/2016_03_28__16_22_43.kml')