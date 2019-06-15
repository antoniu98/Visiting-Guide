import googlemaps
from datetime import datetime
import csv
import pyttsx3
import wikipedia
import webbrowser

def parse_csv():
    with open('places.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='\n')
        rez_list = []
        for idx, place in enumerate(readCSV):
            rez_list.append(place[0])
            if(idx >= 5):
                break
        l = []
        for idx,x in enumerate(rez_list):
            if idx <= 1:
                continue
            l.append(x)
    return l

def my_speak_cloud(my_message):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    engine.say('{}'.format(my_message))
    engine.runAndWait()
    #rate = engine.getProperty('rate')

def main():
    file = open("address.txt", "r")
    dest = file.read()
    # list parse
    l = []
    l = parse_csv()
    # gmaps
    gmaps = googlemaps.Client(key='AIzaSyB3Ksh8kaMa1AF2Ewp0ojAKVgzAwsezb1w')
    now = datetime.now()

    directions_result = gmaps.directions(dest,
                                         dest,
                                         departure_time = now,
                                         waypoints = l,
                                         optimize_waypoints = True)

    y = str(directions_result)
    a = []
    for gzuz in range (y.find("'waypoint_order':")+10, len(y)):
        if y[gzuz].isdigit():
            a.append(int(y[gzuz]))

    url = "https://www.google.com/maps/dir/"
    url += dest
    url += "/"

    message = ""
    for i in a:
        #print(l[i])
        url += l[i]
        url += "/"
        aux = wikipedia.summary(l[i])
        message += aux

    url += dest
    x = url.replace(" ","+")
    webbrowser.open(x)
    my_speak_cloud(message)

if __name__ == "__main__":
    main()