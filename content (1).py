#netflix content finder
#init
import pandas as pd

data = pd.read_csv("Netflix Content - Sheet1.csv")
id = data['id'].tolist() #the number position of each item in an array
type = data['Type'].tolist() #an array of if the items are a movie/tv show
name = data['Title'].tolist() #an array of all the titles of the content
country = data['Country'].tolist() #an array of what countries the content is available in
added = data['Data Added'].tolist() #an array of when the data for the items were added
year = data['Release Year'].tolist() #an array of the dates the content was released
rating = data['Rating'].tolist() #an array of the ratings of each content item
genre = data['Genre'].tolist() #an array of the genre for each content item
filter = [] #empty array I use to filter data

ask = "" #global string I add to and can use in all functions

#functions
def option(ask): #asking if the user wants to see all movies or tv shows
    if ask == "Movie":
        for i in range(len(id)):
            if ask in type[i]:
                filter.append(name[i])
        print(filter)
        print("\n"
              f"Here are all the {ask}s on Netflix")
        filter.clear()
    elif ask == "TV Show":
        for i in range(len(id)):
            if ask in type[i]:
                filter.append(name[i])
        print(filter)
        print(f"Here are all the {ask}s on Netflix")
        filter.clear()
    elif ask != "Movie" or ask != "TV Show":
        print("\n"
              "--> Type one of the options above <--")

def where(question): #asking what country the user is in to show what's available in their country
    global ask
    if question not in country:
        print("\n"
              "--> Try again and check your spelling/capitalization <--")
    else:
        for i in range(len(country)):
            if question in country[i] and ask in type[i]:
                    filter.append(name[i])
        print(filter)
        print("\n"
              f"Here are all the {ask} in {question}")
        filter.clear()

def which(inquiry): #shows the user all the info to the show/movie they input
    if inquiry in name:
        i = name.index(inquiry)
        print("\n",data.loc[i])
    if inquiry not in name:
        print("\n"
              "--> Trying typing the name exactly as shown <--")

#main
while True: #calling all functions in a while True
    thing = input("\n"
            "Welcome to Netflix Content Finder, what would you like to see?:\n"
          "1. all TV Shows/Movies\n"
          "2. Look up all available TV Shows/Movies in your country (- - must do one first or\n"
          "one will show everything available in that country - -)\n"
          "3. Look at the information for a specific piece\n"
          "4. Exit the program\n"
          ">>> ").lower()
    if thing == "1" or thing == "one" or thing == "all":
        ask = input("Do you want to watch a Movie or TV Show? (type exactly as shown): ")
        option(ask)
        continue
    if thing == "2" or thing == "two" or thing == "country":
        question = input("What country are you in? (make sure to spell and capitalize correctly): ")
        where(question)
        continue
    if thing == "3" or thing == "three" or thing == "purpose":
        inquiry = input(f"Which {ask} do you want to look at?: ")
        which(inquiry)
        continue
    if thing == "4" or thing == "four" or thing == "exit":
        print("Okay, goodbye")
        break
    elif (thing != "1" or thing != "one" or thing != "all" or thing != "2" or thing != "two"
          or thing != "country" or thing != "3" or thing != "three" or thing != "purpose"
          or thing != "4" or thing != "four" or thing != "exit"):
        print("\n"
              "--> Type one of the options above <--")

#sources
#Netflix Content Dataset
#dataset sourced from code.org
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://www.kaggle.com/datasets/shivamb/netflix-shows
