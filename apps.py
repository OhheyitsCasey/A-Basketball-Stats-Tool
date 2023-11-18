
from constants import TEAMS, PLAYERS
import copy


def create_players(players):
    
    for player in players:
        player["height"] = int(player["height"][0:2])

        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False

        guardians_split = player["guardians"].split("and")
        player["guardians"] = [guardian.strip(" ") for guardian in guardians_split]

    return players


# balance the number of players equally between teams
def draft(players_list):
    
    # creates global variables for teams so they can be accessed in the menu function
    global panthers, bandits, warriors
    experienced = []
    inexperienced = []
    panthers = []
    bandits = []
    warriors = []

    for player in players_list:
        if player["experience"] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)

    for num, player in enumerate(experienced, start = 1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    for num, player in enumerate(inexperienced, start = 1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    return panthers, bandits, warriors


# displays team stats
def display_stats(team, players):

    exp_players = 0
    inexp_players = 0
    height = 0
    names_list = []
    guardians_list = []

    for player in players:
        if player["experience"] is True:
            exp_players += 1
        elif player["experience"] is False:
            inexp_players += 1

        height += player["height"]
        names_list.append(player["name"])
        guardians_list.append(player["guardians"])

    names = ", ".join([str(name) for name in names_list])
    guardians = ", ".join([str(guardian) for sublist in guardians_list for guardian in sublist])

    print("\nDisplaying stats for the {}.\n".format(team))
    print("There are {} players on the team,".format(len(players)))
    print("{} experienced players and {} inexperienced.".format(exp_players, inexp_players))
    print("The average player height is {} inches.\n".format(height / len(players)))
    print("Players:", names, "\n")
    print("Guardians:", guardians, "\n")


def menu(TEAMS, players_list):
   
    create_players(players_list)
    draft(players_list)

    print("\n***** Menu *****")
    
    while True:
        print("""
            Enter "1" to see stats for the Panthers.
            Enter "2" to see stats for the Bandits.
            Enter "3" to see stats for the Warriors.
            Enter "Quit" to exit the program.
        """)

        try:
            response = input("> ")

            if response.lower() == "1":
                display_stats(TEAMS[0], panthers)
                continue
            elif response.lower() == "2":
                display_stats(TEAMS[1], bandits)
                continue
            elif response.lower() == "3":
                display_stats(TEAMS[2], warriors)
                continue
            elif response.lower() == "quit":
                print("Thanks, Goodbye!!")
                break
            else:
                raise ValueError()
        except ValueError as err:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    # run initial function
    menu(TEAMS, copy.deepcopy(PLAYERS))