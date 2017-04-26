#!/usr/bin/env python3

import requests
import sys
from pprint import pprint

# Current base URL for V3 NA queries
nabase = 'https://na1.api.riotgames.com'

# Base URL for V2.x NA (And some 1.x NA) queries
na2base = 'https://na.api.riotgames.com'

staticbase = 'https://global.api.pvp.net'
key = '?api_key=RGAPI-ddf555c2-a61f-4196-82d2-c9beebf25bd0'

# Note on these calls: Many will 404 if the requested info is "invalid". For example,
# if you request ranked info on an unranked summoner, while the request is valid, there
# is no information to pull and thus the RESTful call 404's. Please keep this in mind
# when parsing responses.


# Champion Mastery V3
# Mastery by Summoner - Returns Mastery points for Summoner sorted in descending order
# Arg: sID - Summoner ID
def mastery_by_summoner(sID):
    url = nabase + '/lol/champion-mastery/v3/champion-masteries/by-summoner/' + str(sID) + key
    r = requests.get(url)
    return r


# Mastery by Champion - Returns a summoner's Mastery points for a given champion
# Args: sID - Summoner ID   cID - Champion ID
def mastery_by_champ(sID,cID):
    url = nabase + '/lol/champion-mastery/v3/champion-masteries/by-summoner/' + str(sID) + \
          '/by-champion/' + str(cID) + key
    r = requests.get(url)
    return r


# Total Mastery - Returns the total mastery score of a summoner
# Args: sID - Summoner ID
def total_mastery(sID):
    url = nabase + '/lol/champion-mastery/v3/scores/by-summoner/' + str(sID) + key
    r = requests.get(url)
    return r


# Champion V3 (Status info: Free to Play, botEnabled etc.)
# Champ Status All - Returns info on every champion
def champ_status_all():
    url = nabase + '/lol/platform/v3/champions' + key
    r = requests.get(url)
    return r


# Champ Status Spec - Returns info on specified champion
# Args: cID - Champion ID
def champ_status_spec(cID):
    url = nabase + '/lol/platform/v3/champions/' + str(cID) + key
    r = requests.get(url)
    return r


# League V2.5
# League by Summoner - Returns all info on every league given summoner is in
# Args: sID - Summoner ID
def league_by_summoner(sID):
    url = na2base + '/api/lol/NA/v2.5/league/by-summoner/' + str(sID) + key
    r = requests.get(url)
    return r


# Specific League by Summoner - Returns league info specific to the sID only
# Args - sID - Summoner ID
def spec_league_by_summ(sID):
    url = na2base + '/api/lol/NA/v2.5/league/by-summoner/' + str(sID) + '/entry' + key
    r = requests.get(url)
    return r


# Challenger - Returns info on all Challenger Leagues
# Args: qtype - solo or flex queue
def challenger(qtype):
    url = na2base + '/api/lol/NA/v2.5/league/challenger'
    if str(qtype) == 'solo':
        url += '?type=RANKED_SOLO_5X5'
    elif str(qtype) == 'flex':
        url += '?type=RANKED_FLEX_SR'
    else:
        sys.stderr.write('Invalid Queue Type\n')
        return 0
    url += '&api_key=RGAPI-ddf555c2-a61f-4196-82d2-c9beebf25bd0'
    r = requests.get(url)
    return r


# Master - Returns info on all Master Leagues
# Args: qtype - solo or flex queue
def master(qtype):
    url = na2base + '/api/lol/NA/v2.5/league/master'
    if str(qtype) == 'solo':
        url += '?type=RANKED_SOLO_5x5'
    elif str(qtype) == 'flex':
        url += '?type=RANKED_FLEX_SR'
    else:
        sys.stderr.write('Invalid Queue Type\n')
        return 0
    url += '&api_key=RGAPI-ddf555c2-a61f-4196-82d2-c9beebf25bd0'
    r = requests.get(url)
    return r


# LOL Status V3
# Shard Data - returns Status data for NA aspects
def shard_data():
    url = nabase + '/lol/status/v3/shard-data' + key
    r = requests.get(url)
    return r


# Masteries V3
# Mastery Pages - returns mastery pages for given summoner
# Args: sID - Summoner ID
def mastery_pages(sID):
    url = nabase + '/lol/platform/v3/masteries/by-summoner/' + str(sID) + key
    r = requests.get(url)
    return r


# Match V2.2
# Match - returns information on a given match
# Args: maID - Match ID
def match(maID):
    url = na2base + '/api/lol/NA/v2.2/match/' + str(maID) + key
    r = requests.get(url)
    return r


# Match V2.2
# MatchList - returns a list of recent match for a given summoner
# Args: sID - Summoner ID
def matchlist(sID):
    url = na2base + '/api/lol/NA/v2.2/matchlist/by-summoner/' + str(sID) + key
    r = requests.get(url)
    return r


# Runes V3
# Rune Pages - returns a list of rune pages for a given summoner
# Args: sID - Summoner ID
def rune_pages(sID):
    url = nabase + '/lol/platform/v3/runes/by-summoner/' + str(sID) + key
    r = requests.get(url)
    return r


# Spectator V3
# Current Game - returns game information for given summoner's active game
# Args: sID - Summoner ID
def current_game(sID):
    url = nabase + '/lol/spectator/v3/active-games/by-summoner/' + str(sID) + key
    r = requests.get(url)
    return r


# Featured Games - returns information on the current featured games
# Args - N/A
def featured_games():
    url = nabase + '/lol/spectator/v3/featured-games' + key
    r = requests.get(url)
    return r


# Static Data V3
# Champ Static - returns info on an champion, if none specified will give all champions
# Args: cID - Champion ID [optional]
def champ_static(cID=None):
    if cID is not None:
        url = nabase + '/lol/static-data/v3/champions/' + str(cID)
    else:
        url = nabase + '/lol/static-data/v3/champions'
    url += key
    r = requests.get(url)
    return r


# Item Static - returns info on an item, if none specified will give all items
# Args: iID - Item ID [optional]
def item_static(iID=None):
    if iID is not None:
        url = nabase + '/lol/static-data/v3/items/' + str(iID)
    else:
        url = nabase + '/lol/static-data/v3/items'
    url += key
    r = requests.get(url)
    return r


# Mastery Static - returns info on a mastery, if none specified will give all masteries
# Args: mID - Mastery ID [optional]
def mastery_static(mID=None):
    if mID is not None:
        url = nabase + '/lol/static-data/v3/masteries/' + str(mID)
    else:
        url = nabase + '/lol/static-data/v3/masteries'
    url += key
    r = requests.get(url)
    return r


# Rune Static - returns info on a rune, if none specified will give all runes
# Args: rID - Rune ID [optional]
def rune_static(rID=None):
    if rID is not None:
        url = nabase + '/lol/static-data/v3/runes/' + str(rID)
    else:
        url = nabase + '/lol/static-data/v3/runes'
    url += key
    r = requests.get(url)
    return r


# Spell Static - returns info on a summoner spell, if none specified will give all spells
# Args: ssID - Summoner Spell ID [optional]
def spell_static(ssID=None):
    if ssID is not None:
        url = nabase + '/lol/static-data/v3/summoner-spells/' + str(ssID)
    else:
        url = nabase + '/lol/static-data/v3/summoner-spells'
    url += key
    r = requests.get(url)
    return r


# String Static - returns list of strings for the given region
# Args: N/A
def string_static():
    url = nabase + '/lol/static-data/v3/language-strings' + key
    r = requests.get(url)
    return r


# Lang Static - returns list of language codes
# Args: N/A
def lang_static():
    url = nabase + '/lol/static-data/v3/languages' + key
    r = requests.get(url)
    return r


# Map Static - returns information on maps
# Args: N/A
def map_static():
    url = nabase + '/lol/static-data/v3/maps' + key
    r = requests.get(url)
    return r


# Icon Static - returns info on profile icons
# Args: N/A
def icon_static():
    url = nabase + '/lol/static-data/v3/profile-icons' + key
    r = requests.get(url)
    return r


# Realm Static - returns info on Static Info data versions
# Args: N/A
def realm_static():
    url = nabase + '/lol/static-data/v3/realms' + key
    r = requests.get(url)
    return r


# Version Static - returns list of all version numbers
# Args: N/A
def version_static():
    url = nabase + '/lol/static-data/v3/versions' + key
    r = requests.get(url)
    return r


# Stats V1.3
# Ranked Stats - returns ranked stats for given summoner, divided by champion (0 is total for all)
# Args: sID - Summoner ID
def ranked_stats(sID):
    url = na2base + '/api/lol/NA/v1.3/stats/by-summoner/' + str(sID) + '/ranked' + key
    r = requests.get(url)
    return r


# Season Stats - returns season stats for given summoner, divided by queue type
# Args: sID - Summoner ID
def season_stats(sID):
    url = na2base + '/api/lol/NA/v1.3/stats/by-summoner/' + str(sID) + '/summary' + key
    r = requests.get(url)
    return r


# Summoner V3
# Summoner by account - returns info on all related summoners, given the Account id
# Args: aID - Account ID
def summoner_by_account(aID):
    url = nabase + '/lol/summoner/v3/summoners/by-account/' + str(aID) + key
    r = requests.get(url)
    return r


# Summoner by name - returns info on a summoner given the name
# Args: sName - Summoner Name
def summoner_by_name(sName):
    url = nabase + '/lol/summoner/v3/summoners/by-name/' + str(sName) + key
    r = requests.get(url)
    return r


# Summoner by ID - returns info on a summoner given the summoner ID
# Args: sID - Summoner ID
def summoner_by_id(sID):
    url = nabase + '/lol/summoner/v3/summoners/' + str(sID) + key
    r = requests.get(url)
    return r


# Test Printer - pretty prints response for testing purposes
# Args: resp - REST response object
def test_printer(resp):
    pprint(resp.json())
    return 0

