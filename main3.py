from laba3 import Players

def main():
    file_name = "playstation_players.csv"  
    stats = Players(file_name)
    stats.plot_country_distribution()


if __name__ == "__main__":
    main()