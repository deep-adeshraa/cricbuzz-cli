from pycricbuzz import cricbuzz


def all_match():
    ma = cricbuzz.Cricbuzz().matches()
    match = []
    for i in ma:
        match.append([i["id"], i['team1']["name"], i["team2"]["name"]])
    return match


def live_score(mid):
    scr = cricbuzz.Cricbuzz().livescore(mid)
    txt = "\n"
    txt += scr["batting"]["team"] + "\n{:<3}-{:2}({:} overs)\n".format(scr["batting"]["score"][0]["runs"],
                                                                       scr["batting"]["score"][0]["wickets"],
                                                                       scr["batting"]["score"][0]["overs"])
    txt += "\n{:17} {:3}({})".format(scr["batting"]["batsman"][0]["name"], scr["batting"]["batsman"][0]["runs"],
                                     scr["batting"]["batsman"][0]["balls"])
    txt += "\n{:17} {:3}({})".format(scr["batting"]["batsman"][1]["name"], scr["batting"]["batsman"][1]["runs"],
                                     scr["batting"]["batsman"][1]["balls"])

    txt += "\n\n" + scr["bowling"]["team"] + "\n{:17}{} overs ({:3}runs)".format(scr["bowling"]["bowler"][0]["name"],
                                                                                 scr["bowling"]["bowler"][0]["overs"],
                                                                                 scr["bowling"]["bowler"][0]["runs"])
    return txt + "\n"


def scorecard(mid):
    card = cricbuzz.Cricbuzz().scorecard(mid)
    title = "{} vs {}\n\n{:15}{}/{}  {}".format(card["scorecard"][0]["batteam"], card["scorecard"][1]["batteam"],
                                                card["scorecard"][0]["batteam"],
                                                card["scorecard"][0]["runs"], card["scorecard"][0]["wickets"],
                                                card["scorecard"][0]["overs"] + " over")
    title += "\n{:15}{}/{}  {}".format(card["scorecard"][1]["batteam"], card["scorecard"][1]["runs"],
                                       card["scorecard"][1]["wickets"],
                                       card["scorecard"][1]["overs"] + " over")
    title += "\n\n{}".format(cricbuzz.Cricbuzz().matchinfo(mid)["status"])
    head = "\n\n{:20} {:3} {:3} {:3} {:3}\n".format('Name', 'R', 'B', '4', '6')
    sty = "----------------------------------\n"
    bats = ""
    for j in range(card["scorecard"][0]["batcard"].__len__()):
        bats += "{:20} {:3} {:3} {:3} {:3}".format(card["scorecard"][0]["batcard"][j]["name"],
                                                   card["scorecard"][0]["batcard"][j]["runs"],
                                                   card["scorecard"][0]["batcard"][j]["balls"],
                                                   card["scorecard"][0]["batcard"][j]["fours"],
                                                   card["scorecard"][0]["batcard"][j]["six"]) + "\n"
    head2 = "\n\n{:20}{:7}{:9}{:7}{:7}\n".format("Name", "overs", "maidens", "Runs", "Wickets")
    bowl = ""

    for i in range(card["scorecard"][0]["bowlcard"].__len__()):
        bowl += "{:20}{:7}{:9}{:7}{:7}".format(card["scorecard"][0]["bowlcard"][i]["name"],
                                               card["scorecard"][0]["bowlcard"][i]["overs"],
                                               card["scorecard"][0]["bowlcard"][i]["maidens"],
                                               card["scorecard"][0]["bowlcard"][i]["runs"],
                                               card["scorecard"][0]["bowlcard"][i]["wickets"]) + "\n"

    bats2 = ""
    for j in range(card["scorecard"][1]["batcard"].__len__()):
        bats2 += "{:20} {:3} {:3} {:3} {:3}".format(card["scorecard"][1]["batcard"][j]["name"],
                                                    card["scorecard"][1]["batcard"][j]["runs"],
                                                    card["scorecard"][1]["batcard"][j]["balls"],
                                                    card["scorecard"][1]["batcard"][j]["fours"],
                                                    card["scorecard"][1]["batcard"][j]["six"]) + "\n"
    bowl2 = ""
    for i in range(card["scorecard"][1]["bowlcard"].__len__()):
        bowl2 += "{:20}{:7}{:9}{:7}{:7}".format(card["scorecard"][1]["bowlcard"][i]["name"],
                                                card["scorecard"][1]["bowlcard"][i]["overs"],
                                                card["scorecard"][1]["bowlcard"][i]["maidens"],
                                                card["scorecard"][1]["bowlcard"][i]["runs"],
                                                card["scorecard"][1]["bowlcard"][i]["wickets"]) + "\n"

    # return cricbuzz.Cricbuzz().matchinfo(mid)
    return "\n" + title + "\n\n" + head + sty + bats + head2 + sty + bowl + head + sty + bats2 + head2 + sty + bowl2


# print(all_match())
# print(live_score("20262"))


def matcinfo(mid):
    info = cricbuzz.Cricbuzz().matchinfo(mid)
    return info["status"]


if __name__ == '__main__':
    print("Available Matches...\n")
    allmatch = all_match()
    for i in range(len(allmatch)):
        print(i + 1, allmatch[i][1], " vs ", allmatch[i][2])

    choice = -1
    while choice < 1 or choice > len(allmatch):
        print("\nEnter Your Number of choice")
        try:
            choice = int(input())
        except:
            print("please enter int")
    matchid = allmatch[choice - 1][0]
    fun = 0
    while fun != 1 and fun != 2:
        print("1. Live score")
        print("2. Full ScoreCard")
        try:
            fun = int(input())
        except:
            print("please enter 1 or 2")

    if fun == 1:
        try:
            yor = "y"
            while (yor is not "n"):
                print(live_score(matchid))
                yor = input("enter n for exit and y for refresh\n")
        except:
            print("its not live")
    elif fun == 2:
        try:
            print(scorecard(matchid))
        except:
            print(allmatch[choice - 1][1], " vs ", allmatch[choice - 1][2])
            print(matcinfo(matchid))
