import requests
from bs4 import BeautifulSoup
import csv

with open('samplecsv2.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ',')

    season = 2000
    while season <= 2018:
        x = 1
        while x <=17:
            seasonweek = "http://www.nfl.com/schedules/%s/REG%s" % (season, x)
            page = requests.get(seasonweek)
            print(seasonweek)

            soup = BeautifulSoup(page.content, 'html.parser')

            print("\n\n############ \nWeek %s\n############\n\n" % x)



            nextstep = soup.select(".team-name.away") #works
            #print(nextstep)
            print("Away Teams")
            AwayTeams = []
            for span in nextstep:
               AwayTeams.append(span.text)
            print(AwayTeams)
            print(AwayTeams[0])

            hometeams = soup.select(".team-name.home") #works
            print("\nHome Teams")
            HomeTeams = []
            for span in hometeams:
              HomeTeams.append(span.text)
            print(HomeTeams)

            awayscore = soup.select(".team-score.away") #works
            print("\nAway Score")
            AwayScores = []
            for span in awayscore:
                AwayScores.append(span.text)
            print(AwayScores)

            homescore = soup.select(".team-score.home") #works
            print("\nHome Score")
            HomeScores = []
            for span in homescore:
                HomeScores.append(span.text)
            print(HomeScores)

            '''
            writervar = 0
            while writervar <= 17:
                spamwriter.writerow([season, 'Regular Season', x, AwayTeams[writervar],
                AwayScores[writervar], HomeTeams[writervar],HomeScores[writervar]])
                writervar+=1
            '''
            writervar = 0
            for data in AwayTeams:
                spamwriter.writerow([season, 'Regular Season', x, data,
                AwayScores[writervar], HomeTeams[writervar],HomeScores[writervar]])
                writervar+=1

            x+=1

        ###############################
        #now for post season
        ###############################
        seasonweek = "http://www.nfl.com/schedules/%s/POST" % season
        page = requests.get(seasonweek)
        print(seasonweek)
        soup = BeautifulSoup(page.content, 'html.parser')

        print("\n\n\n##########\n##########\nPostSeason\n##########\n##########\n\n\n")

        nextstep = soup.select(".team-name.away") #works
        #print(nextstep)
        print("Away Teams")
        AwayTeamsPS = []
        for span in nextstep:
           AwayTeamsPS.append(span.text)
        print(AwayTeamsPS)


        hometeams = soup.select(".team-name.home") #works
        print("\nHome Teams")
        HomeTeamsPS = []
        for span in hometeams:
          HomeTeamsPS.append(span.text)
        print(HomeTeamsPS)

        awayscore = soup.select(".team-score.away") #works
        AwayScoresPS = []
        print("\nAway Score")
        for span in awayscore:
            AwayScoresPS.append(span.text)
        print(AwayScoresPS)

        homescore = soup.select(".team-score.home") #works
        HomeScoresPS = []
        print("\nHome Score")
        for span in homescore:
            HomeScoresPS.append(span.text)
        print(HomeScoresPS)

        writervar = 0
        for data in AwayTeamsPS:
            spamwriter.writerow([season, 'Post-Season', x, data,
            AwayScoresPS[writervar], HomeTeamsPS[writervar],HomeScoresPS[writervar]])
            writervar+=1

        season+=1
        print("##\n##\n##\n##\n##\n##\n")
