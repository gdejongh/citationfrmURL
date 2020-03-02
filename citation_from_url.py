from pip._vendor.distlib.compat import raw_input
from pytube import YouTube
import re as r
from datetime import date as d

input = raw_input("Enter YouTube URL:").strip()

format = raw_input("\nFormat Style (Harvard, MLA, APA): ").strip().lower()

yt = YouTube(input)

title = yt.title.strip()

author = yt.author.strip()

description = yt.description

html = yt.watch_html

datePublished = r.search("(?<=Published on )(.*?)(?=</)", html)
datePublished = datePublished.group(0).strip()
yearPublished = datePublished.split(" ")[2]

dayAccessed = d.today().strftime("%d")
monthAccessedNumber = d.today().strftime("%m")
yearAccessed = d.today().strftime("%Y")
dateAccessedmmddyyyy = d.today().strftime("%m/%d/%Y")

months = {
    "01":"Jan",
    "02":"Feb",
    "03":"Mar",
    "04":"Apr",
    "05":"May",
    "06":"Jun",
    "07":"Jul",
    "08":"Aug",
    "09":"Sept",
    "10":"Oct",
    "11":"Nov",
    "12":"Dec"
}

monthAccessedWord = months[monthAccessedNumber]
dateAccessedWord = dayAccessed + " " + monthAccessedWord + " " + yearAccessed

# print(title, " ", author, "\n", description)
# print("\nrating: ", yt.rating)
# print("\ndate: ", datePublished)

def toMLA_format():
    mlaformat = author + "MLA: \"" + title + "\" " + " Online video clip. YouTube.\n YouTube, " + datePublished + ". Web. " + dateAccessedWord
    return mlaformat

def toHarvard_format():
    harvardformat = author + "Harvard: (" + yearPublished + ") " + "''" + title + "''. " + " [online video] " + "Available at: " + input + ". [Accessed " + dateAccessedmmddyyyy + "]"
    return harvardformat

def toAPA_format():
    apaformat = "APA: [" + author + "]. (" + yearAccessed + ", " + monthAccessedWord + " " + dayAccessed + "). " + title + " [Video File]. Retrieved from " + input
    return apaformat

def select_format(format_type):
    if(format_type == "mla"):
        return toMLA_format()
    elif(format_type == "harvard"):
        return toHarvard_format()
    elif(format_type == "apa"):
        return toAPA_format()
    else:
        return "\nThe format type " + format + " is not recognized."


returnStr = select_format(format)


print("\n\n")
print(returnStr)
print("\n\n")