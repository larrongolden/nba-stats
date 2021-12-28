# import psycopg2
import pandas as pd
# from config import config
from nba_api.stats.static import teams

def enter_password():
    """
    Get password from user
    :return: password
    """
    password = input("Enter database password: ")
    return password


def find_all_teams():
    """
    Find all teams in the NBA
    :return: list of teams
    """
    teams_list = teams.get_teams()
    return teams_list
