import re

def process_file(file_path):
    f = open(file_path, "r")

    # read the file content
    text = f.read()

    # close the input file
    f.close()

    # replace all ']Location' with ']\nLocation'
    text = re.sub(r']Location', r']\nLocation', text)

    # replace all 'Location[' with '{Location'
    text = re.sub(r'Location\[', r'{', text)

    # replace all ' {Bundle[.*]}' with ''
    text = re.sub(r' \{Bundle.*}', r'', text)

    # replace all ']' with '},'
    text = re.sub(r']', r'},', text)

    # replace all 'gps ' with '"gps":"'
    text = re.sub(r'gps ', r'"gps":"', text)

    # replace all ' acc=' with '", "acc":"'
    text = re.sub(r' acc=', r'", "acc":"', text)

    # replace all ' et=' with '", "et":"'
    text = re.sub(r' et=', r'", "et":"', text)

    # replace all ' alt=' with '", "alt":"'
    text = re.sub(r' alt=', r'", "alt":"', text)

    # replace all ' vel=' with '", "vel":"'
    text = re.sub(r' vel=', r'", "vel":"', text)

    # replace all ' bear=' with '", "bear":"'
    text = re.sub(r' bear=', r'", "bear":"', text)

    # replace all '}' with '"}'
    text = re.sub(r'}', r'"}', text)

    # add '{"data":[' in front of the text
    text = '{"data":[' + text

    # replace ',' in gps with ';'
    text = re.sub(r'"[0-9]*,[0-9]*,', lambda x: x.group()[:-1] + ';', text)

    # add ']}' at the end of the string, removing the ','
    text = text[:-1]  # the remove trick
    text += ']}'
    #print(text)

    # write the JSON to a file in Data
    f = open(file_path[:-3] + 'json', "w")
    f.write(text)


# run the function
#process_file('/home/virgil/workspace/PycharmProjects/android_location_to_kml/Data/LocationDataFile_2016_03_28__15_57_28.txt')
process_file('/home/virgil/workspace/PycharmProjects/android_location_to_kml/Data/LocationDataFile_2016_03_28__16_22_43.txt')