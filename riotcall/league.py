#!/usr/bin/env python3

import requests
import sys
from pprint import pprint

# Current base URL for V3 NA queries
nabase = 'https://na1.api.riotgames.com'

# Base URL for V2.x NA (And some 1.x NA) queries
na2base = 'https://na.api.riotgames.com'

staticbase = 'https://global.api.pvp.net'
key = 'api_key=RGAPI-5593b315-1fc8-4ad8-be9e-45474b1f7308'

# Note on these calls: Many will 404 if the requested info is "invalid". For example,
# if you request ranked info on an unranked summoner, while the request is valid, there
# is no information to pull and thus the RESTful call 404's. Please keep this in mind
# when parsing responses.


# Champion Mastery V3
def mastery_by_summoner(sID):
    """
   Mastery by Summoner

    :param sID: Summoner ID
    :return: Mastery points for Summoner sorted in descending order
    """
    url = nabase + '/lol/champion-mastery/v3/champion-masteries/by-summoner/' + str(sID) + '?' + key
    r = requests.get(url)
    return r


def mastery_by_champ(sID,cID):
    """
    Mastery by Champion

    :param sID: Summoner ID
    :param cID: Champion ID
    :return: A summoner's Mastery Score for a given champ
    """
    url = nabase + '/lol/champion-mastery/v3/champion-masteries/by-summoner/' + str(sID) + \
          '/by-champion/' + str(cID) + '?' + '?' + key
    r = requests.get(url)
    return r


def total_mastery(sID):
    """
    Total Mastery

    :param sID: Summoner ID
    :return: The total mastery score of a summoner as an int
    """
    url = nabase + '/lol/champion-mastery/v3/scores/by-summoner/' + str(sID) + '?' + '?' + key
    r = requests.get(url)
    return r


# Champion V3 (Status info: Free to Play, botEnabled etc.)
def champ_status_all():
    """
    Champ Status All

    :return: Status info on every champ
    """
    url = nabase + '/lol/platform/v3/champions' + '?' + '?' + key
    r = requests.get(url)
    return r


def champ_status_spec(cID):
    """
    Champ Status Specific

    :param cID: Champion ID
    :return: Info on a specific champion
    """
    url = nabase + '/lol/platform/v3/champions/' + str(cID) + '?' + key
    r = requests.get(url)
    return r


# League V3
def league_by_summoner(sID):
    """
    League by Summoner

    :param sID: Summoner ID
    :return: Full League info for given summoner
    """
    url = nabase + '/lol/league/v3/leagues/by-summoner/' + str(sID) + '?' + key
    r = requests.get(url)
    return r


def spec_league_by_summ(sID):
    """
    Specific League by Summoner

    :param sID: Summoner ID
    :return: League info for only the given summoner
    """
    url = nabase + '/lol/league/v3/positions/by-summoner/' + str(sID) + '?' + key
    r = requests.get(url)
    return r


def challenger(qtype):
    """
    Challenger
    
    :param qtype: queue type (solo, flex, or treeline)
    :return: League info for NA Challenger
    """
    url = nabase + '/lol/league/v3/challengerleagues/by-queue/'
    if str(qtype) == 'solo':
        url += 'RANKED_SOLO_5X5'
    elif str(qtype) == 'flex':
        url += 'RANKED_FLEX_SR'
    elif str(qtype) == 'treeline':
        url += 'RANKED_FLEX_TT'
    else:
        sys.stderr.write('Invalid Queue Type\n')
        return 0
    url = url + '?' + key
    r = requests.get(url)
    return r


def master(qtype):
    """
    Master

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
    url = url + '?' + key
    r = requests.get(url)
    return r


# LOL Status V3
def shard_data():
    """
    Shard Data

    :return: Status data for NA Servers
    """
    url = nabase + '/lol/status/v3/shard-data' + '?' + key
    r = requests.get(url)
    return r


# Masteries V3
def mastery_pages(sID):
    """
    Masteries

    :param sID: Summoner ID
    :return: Mastery Pages for the given summoner
    """
    url = nabase + '/lol/platform/v3/masteries/by-summoner/' + str(sID) + '?' + key
    r = requests.get(url)
    return r


# Match V3
def match(maID):
    """
    Match

    :param maID: match ID
    :return: Information on the given match
    """
    url = nabase + '/lol/match/v3/matches/' + str(maID) + '?' + key
    r = requests.get(url)
    return r


def timeline(maID):
    """
    Timeline

    :param maID: match ID
    :return: Full timeline for the given match
    """
    url = nabase + '/lol/match/v3/timelines/by-match/' + str(maID) + '?' + key
    r = requests.get(url)
    return r


# TODO add support for full parameter options
def matchlist(aID):
    """
    Matchlist

    :param aID: account ID
    :return: Full matchlist of given summoner
    """
    url = nabase + '/lol/match/v3/matchlists/by-account/' + str(aID)+ '?' + key
    r = requests.get(url)
    return r


def recent_matchlist(aID):
    """
    Recent Matchlist

    :param aID: account ID
    :return: Mathlist of last 20 games
    """
    url = nabase + '/lol/match/v3/matchlists/by-account/' + str(aID) + '/recent' + '?' + key
    r = requests.get(url)
    return r


def tournament_mathlist(tCode):
    """
    Tournament Matchlist

    :param tCode: Tournament Code
    :return: A list of match IDs by tournament
    """
    url = nabase + '/lol/match/v3/matches/by-tournament-code/' + str(tCode) + '/ids' + '?' + key
    r = requests.get(url)
    return r


def tournament_match(tCode, maID):
    """
    Tournament Match

    :param tCode: Tournament Code
    :param maID: Match ID
    :return: a match's info from a tournament
    """
    url = nabase + '/lol/match/v3/matches/' + str(maID) + '/by-tournament-code/' + str(tCode) + '?' + key
    r = requests.get(url)
    return r


# Runes V3
def rune_pages(sID):
    """
    Rune Pages

    :param sID: Summoner ID
    :return: a list of rune pages for the summoner
    """
    url = nabase + '/lol/platform/v3/runes/by-summoner/' + str(sID) + '?' + key
    r = requests.get(url)
    return r


# Spectator V3
# Current Game - returns game information for given summoner's active game
# Args: sID - Summoner ID
def current_game(sID):
    """
    Current Game

    :param sID: Summoner ID
    :return: Info on the game a summoner is in, if possible
    """
    url = nabase + '/lol/spectator/v3/active-games/by-summoner/' + str(sID) + '?' + key
    r = requests.get(url)
    return r


# Featured Games - returns information on the current featured games
# Args - N/A
def featured_games():
    url = nabase + '/lol/spectator/v3/featured-games' + '?' + key
    r = requests.get(url)
    return r


# Static Data V3
def champ_static(cID=None):
    """
    Champ Static

    :param cID: Champion ID*
    :return: Static champion data
    """
    if cID is not None:
        url = nabase + '/lol/static-data/v3/champions/' + str(cID)
    else:
        url = nabase + '/lol/static-data/v3/champions'
    url += key
    r = requests.get(url)
    return r


def item_static(iID=None):
    """
    Item Static

    :param iID: Item ID*
    :return: Static item information
    """
    if iID is not None:
        url = nabase + '/lol/static-data/v3/items/' + str(iID)
    else:
        url = nabase + '/lol/static-data/v3/items'
    url += key
    r = requests.get(url)
    return r


def mastery_static(mID=None):
    """
    Mastery Static

    :param mID: Mastery ID*
    :return: Static mastery information
    """
    if mID is not None:
        url = nabase + '/lol/static-data/v3/masteries/' + str(mID)
    else:
        url = nabase + '/lol/static-data/v3/masteries'
    url += key
    r = requests.get(url)
    return r


def rune_static(rID=None):
    """
    Rune Static

    :param rID: Rune ID*
    :return: Static rune information
    """
    if rID is not None:
        url = nabase + '/lol/static-data/v3/runes/' + str(rID)
    else:
        url = nabase + '/lol/static-data/v3/runes'
    url += key
    r = requests.get(url)
    return r


def spell_static(ssID=None):
    """
    Spell Static

    :param ssID: Summoner Spell ID*
    :return: Static summoner spell information
    """
    if ssID is not None:
        url = nabase + '/lol/static-data/v3/summoner-spells/' + str(ssID)
    else:
        url = nabase + '/lol/static-data/v3/summoner-spells'
    url += key
    r = requests.get(url)
    return r


def string_static(lang=None):
    """
    String Static

    :param lang: Language Code
    :return: Returns strings localized to given language (default is English)
    """
    if lang is not None:
        url = nabase + '/lol/static-data/v3/language-strings' + '?locale=' + str(lang) + '&'
    else:
        url = nabase + '/lol/static-data/v3/language-strings' + '?'
    url += key
    r = requests.get(url)
    return r


def lang_static():
    """
    Lang Static

    :return: a list of language codes
    """
    url = nabase + '/lol/static-data/v3/languages' + '?' + key
    r = requests.get(url)
    return r


def map_static():
    """
    Map Static

    :return: Info on all maps
    """
    url = nabase + '/lol/static-data/v3/maps' + '?' + key
    r = requests.get(url)
    return r


def icon_static():
    """
    Icon Static

    :return: returns info on all profile icons
    """
    url = nabase + '/lol/static-data/v3/profile-icons' + '?' + key
    r = requests.get(url)
    return r


def realm_static():
    """
    Realm Static

    :return: Info on endpoint version numbers
    """
    url = nabase + '/lol/static-data/v3/realms' + '?' + key
    r = requests.get(url)
    return r


def version_static():
    """
    Version Static

    :return: Info on game version numbers
    """
    url = nabase + '/lol/static-data/v3/versions' + '?' + key
    r = requests.get(url)
    return r


# Summoner V3
def summoner_by_account(aID):
    """
    Summoner by Account

    :param aID: account ID
    :return: All summoner info for account
    """
    url = nabase + '/lol/summoner/v3/summoners/by-account/' + str(aID) + '?' + key
    r = requests.get(url)
    return r


def summoner_by_name(sName):
    """
    Summoner by Name

    :param sName: Summoner name
    :return: Info on given summoner
    """
    url = nabase + '/lol/summoner/v3/summoners/by-name/' + str(sName) + '?' + key
    r = requests.get(url)
    return r


def summoner_by_id(sID):
    """
    Summoner by ID

    :param sID: Summoner ID
    :return: Info on the given summoner
    """
    url = nabase + '/lol/summoner/v3/summoners/' + str(sID) + '?' + key
    r = requests.get(url)
    return r


# Test Printer - pretty prints response for testing purposes
# Args: resp - REST response object
def test_printer(resp):
    pprint(resp.json())
    return 0
