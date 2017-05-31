#!/usr/bin/env python3

import requests
import sys
from pprint import pprint

# Current base URL for V3 NA queries
nabase = 'https://na1.api.riotgames.com'


# Note on these calls: Many will 404 if the requested info is "invalid". For example,
# if you request ranked info on an unranked summoner, while the request is valid, there
# is no information to pull and thus the RESTful call 404's. Please keep this in mind
# when parsing responses.

# Champion Mastery V3
def mastery(key, sID, cID=None):
   """
   Mastery

   :param key: API key
   :param sID: Summoner ID
   :param cID: Champion ID*
   :return: A summoner's champion mastery report, cID will show only that champ
   """
   if cID is not None:
      url = nabase + '/lol/champion-mastery/v3/champion-masteries/by-summoner/' \
       + str(sID) + '/by-champion/' + str(cID) + '?api_key='
   else:
      url = nabase + '/lol/champion-mastery/v3/champion-masteries/by-summoner/' \
       + str(sID) + '?api_key='
   url += key
   r = requests.get(url)
   return r


def total_mastery(key, sID):
    """
    Total Mastery

    :param key: API key
    :param sID: Summoner ID
    :return: The total mastery score of a summoner as an int
    """
    url = nabase + '/lol/champion-mastery/v3/scores/by-summoner/' + str(sID) + \
      '?api_key=' + key
    r = requests.get(url)
    return r


# Champion V3 (Status info: Free to Play, botEnabled etc.)
def champ_status(key, cID=None):
    """
    Champ Status

    :param key: API key
    :param cID: Champion ID
    :return: Info on a specific champion if cID is given, or all champs if not
    """
    if cID is not None:
        url = nabase + '/lol/platform/v3/champions/' + str(cID) + '?api_key='
    else:
        url = nabase + '/lol/platform/v3/champions' + '?api_key='
    url += key
    r = requests.get(url)
    return r


# League V3
def league_by_summoner(key, sID):
    """
    League by Summoner

    :param key: API key
    :param sID: Summoner ID
    :return: Full League info for given summoner
    """
    url = nabase + '/lol/league/v3/leagues/by-summoner/' + str(sID) + '?api_key=' + key
    r = requests.get(url)
    return r


def spec_league_by_summoner(key, sID):
    """
    Specific League by Summoner

    :param key: API key
    :param sID: Summoner ID
    :return: League info for only the given summoner
    """
    url = nabase + '/lol/league/v3/positions/by-summoner/' + str(sID) + '?api_key=' + key
    r = requests.get(url)
    return r


def challenger(key, qtype):
    """
    Challenger

    :param key: API key
    :param qtype: queue type (solo, flex, or treeline)
    :return: League info for NA Challenger
    """
    url = nabase + '/lol/league/v3/challengerleagues/by-queue/'
    if str(qtype) == 'solo':
        url += 'RANKED_SOLO_5x5'
    elif str(qtype) == 'flex':
        url += 'RANKED_FLEX_SR'
    elif str(qtype) == 'treeline':
        url += 'RANKED_FLEX_TT'
    else:
        sys.stderr.write('Invalid Queue Type\n')
        return 0
    url = url + '?api_key=' + key
    r = requests.get(url)
    return r


def master(key, qtype):
    """
    Master

    :param key: API key
    :param qtype: queue type (solo, flex, or treeline)
    :return: League info for NA Master
    """
    url = nabase + '/lol/league/v3/masterleagues/by-queue/'
    if str(qtype) == 'solo':
        url += 'RANKED_SOLO_5x5'
    elif str(qtype) == 'flex':
        url += 'RANKED_FLEX_SR'
    elif str(qtype) == 'treeline':
        url += 'RANKED_FLEX_TT'
    else:
        sys.stderr.write('Invalid Queue Type\n')
        return 0
    url = url + '?api_key=' + key
    r = requests.get(url)
    return r


# Status V3
def shard_data(key):
    """
    Shard Data

    :param key: API key
    :return: Status data for NA Servers
    """
    url = nabase + '/lol/status/v3/shard-data' + '?api_key=' + key
    r = requests.get(url)
    return r


# Masteries V3
def mastery_pages(key, sID):
    """
    Masteries

    :param key: API key
    :param sID: Summoner ID
    :return: Mastery Pages for the given summoner
    """
    url = nabase + '/lol/platform/v3/masteries/by-summoner/' + str(sID) + \
      '?api_key=' + key
    r = requests.get(url)
    return r


# Runes V3
def rune_pages(key, sID):
    """
    Rune Pages

    :param key: API key
    :param sID: Summoner ID
    :return: a list of rune pages for the summoner
    """
    url = nabase + '/lol/platform/v3/runes/by-summoner/' + str(sID) + \
      '?api_key=' + key
    r = requests.get(url)
    return r


# Match V3
def match(key, maID):
    """
    Match

    :param key: API key
    :param maID: match ID
    :return: Information on the given match
    """
    url = nabase + '/lol/match/v3/matches/' + str(maID) + '?api_key=' + key
    r = requests.get(url)
    return r


def timeline(key, maID):
    """
    Timeline

    :param key: API key
    :param maID: match ID
    :return: Full timeline for the given match
    """
    url = nabase + '/lol/match/v3/timelines/by-match/' + str(maID) + \
      '?api_key=' + key
    r = requests.get(url)
    return r


# TODO add support for full parameter options
def matchlist(key, aID):
    """
    Matchlist

    :param key: API key
    :param aID: account ID
    :return: Full matchlist of given summoner
    """
    url = nabase + '/lol/match/v3/matchlists/by-account/' + str(aID)+ \
      '?api_key=' + key
    r = requests.get(url)
    return r


def recent_matchlist(key, aID):
    """
    Recent Matchlist

    :param key: API key
    :param aID: account ID
    :return: Mathlist of last 20 games
    """
    url = nabase + '/lol/match/v3/matchlists/by-account/' + str(aID) + \
      '/recent' + '?api_key=' + key
    r = requests.get(url)
    return r


def tournament_mathlist(key, tCode):
    """
    Tournament Matchlist

    :param key: API key
    :param tCode: Tournament Code
    :return: A list of match IDs by tournament
    """
    url = nabase + '/lol/match/v3/matches/by-tournament-code/' + str(tCode) + \
     '/ids' + '?api_key=' + key
    r = requests.get(url)
    return r


def tournament_match(key, tCode, maID):
    """
    Tournament Match

    :param key: API key
    :param tCode: Tournament Code
    :param maID: Match ID
    :return: a match's info from a tournament
    """
    url = nabase + '/lol/match/v3/matches/' + str(maID) + '/by-tournament-' + \
      'code/' + str(tCode) + '?api_key=' + key
    r = requests.get(url)
    return r


# Spectator V3
def current_game(key, sID):
    """
    Current Game

    :param key: API key
    :param sID: Summoner ID
    :return: Info on the game a summoner is in, if possible
    """
    url = nabase + '/lol/spectator/v3/active-games/by-summoner/' + str(sID) + \
      '?api_key=' + key
    r = requests.get(url)
    return r


def featured_games(key):
   """
   Featured Games

   :param key: API key
   :retun: List of featured Games
   """
   url = nabase + '/lol/spectator/v3/featured-games' + '?api_key=' + key
   r = requests.get(url)
   return r


# Static Data V3
def champ_static(key, cID=None):
    """
    Champ Static

    :param key: API key
    :param cID: Champion ID*
    :return: Static champion data
    """
    if cID is not None:
        url = nabase + '/lol/static-data/v3/champions/' + str(cID) + '?api_key='
    else:
        url = nabase + '/lol/static-data/v3/champions' + '?api_key='
    url += key
    r = requests.get(url)
    return r


def item_static(key, iID=None):
    """
    Item Static

    :param key: API key
    :param iID: Item ID*
    :return: Static item information
    """
    if iID is not None:
        url = nabase + '/lol/static-data/v3/items/' + str(iID) + '?api_key='
    else:
        url = nabase + '/lol/static-data/v3/items' + '?api_key='
    url += key
    r = requests.get(url)
    return r


def mastery_static(key, mID=None):
    """
    Mastery Static

    :param key: API key
    :param mID: Mastery ID*
    :return: Static mastery information
    """
    if mID is not None:
        url = nabase + '/lol/static-data/v3/masteries/' + str(mID) + '?api_key='
    else:
        url = nabase + '/lol/static-data/v3/masteries' + '?api_key='
    url += key
    r = requests.get(url)
    return r


def rune_static(key, rID=None):
    """
    Rune Static

    :param key: API key
    :param rID: Rune ID*
    :return: Static rune information
    """
    if rID is not None:
        url = nabase + '/lol/static-data/v3/runes/' + str(rID) + '?api_key='
    else:
        url = nabase + '/lol/static-data/v3/runes' + '?api_key='
    url += key
    r = requests.get(url)
    return r


def spell_static(key, ssID=None):
    """
    Spell Static

    :param key: API key
    :param ssID: Summoner Spell ID*
    :return: Static summoner spell information
    """
    if ssID is not None:
        url = nabase + '/lol/static-data/v3/summoner-spells/' + \
         str(ssID) + '?api_key='
    else:
        url = nabase + '/lol/static-data/v3/summoner-spells' + '?api_key='
    url += key
    r = requests.get(url)
    return r


def string_static(key, lang=None):
    """
    String Static

    :param key: API key
    :param lang: Language Code
    :return: Returns strings localized to given language (default is English)
    """
    if lang is not None:
        url = nabase + '/lol/static-data/v3/language-strings' + '?locale=' + \
         str(lang) + '&api_key='
    else:
        url = nabase + '/lol/static-data/v3/language-strings' + '?api_key='
    url += key
    r = requests.get(url)
    return r


def lang_static(key):
    """
    Lang Static

    :param key: API key
    :return: a list of language codes
    """
    url = nabase + '/lol/static-data/v3/languages' + '?api_key=' + key
    r = requests.get(url)
    return r


def map_static(key):
    """
    Map Static

    :param key: API key
    :return: Info on all maps
    """
    url = nabase + '/lol/static-data/v3/maps' + '?api_key=' + key
    r = requests.get(url)
    return r


def icon_static(key):
    """
    Icon Static

    :param key: API key
    :return: returns info on all profile icons
    """
    url = nabase + '/lol/static-data/v3/profile-icons' + '?api_key=' + key
    r = requests.get(url)
    return r


def realm_static(key):
    """
    Realm Static

    :param key: API key
    :return: Info on endpoint version numbers
    """
    url = nabase + '/lol/static-data/v3/realms' + '?api_key=' + key
    r = requests.get(url)
    return r


def version_static(key):
    """
    Version Static

    :param key: API key
    :return: Info on game version numbers
    """
    url = nabase + '/lol/static-data/v3/versions' + '?api_key=' + key
    r = requests.get(url)
    return r


# Summoner V3
def summoner_by_account(key, aID):
    """
    Summoner by Account

    :param key: API key
    :param aID: account ID
    :return: All summoner info for account
    """
    url = nabase + '/lol/summoner/v3/summoners/by-account/' + str(aID) + \
      '?api_key=' + key
    r = requests.get(url)
    return r


def summoner_by_name(key, sName):
    """
    Summoner by Name

    :param sName: Summoner name
    :param key: API key
    :return: Info on given summoner
    """
    url = nabase + '/lol/summoner/v3/summoners/by-name/' + str(sName) + \
      '?api_key=' + key
    r = requests.get(url)
    return r


def summoner_by_id(key, sID):
    """
    Summoner by ID

    :param sID: Summoner ID
    :param key: API key
    :return: Info on the given summoner
    """
    url = nabase + '/lol/summoner/v3/summoners/' + str(sID) + '?api_key=' + key
    r = requests.get(url)
    return r


# Test Printer - pretty prints response for testing purposes
# Args: resp - REST response object
def test_printer(resp):
    pprint(resp.json())
    return 0
