# Yasuo (development phase)

League of legends api wrapper

## Environment variables

RIOT_API_KEY = Riot api key

## Run examples

You need to set an environment variable "RIOT_API_KEY" (or create .env with this key)

### Run all examples
```sh
python run_examples.py
```

### Specific example(s)
```sh
python run_examples.py <examplename1> <examplename2>...
```

To get example list:
```sh
python get_example_list.py
```

# Endpoints 
Everything should be in the same order as in the official docs.
## CLASH
- [ ] `Get players by summoner id`
- [ ] `Get team`
- [ ] `Get tournaments`
- [ ] `Get tournaments by team id`
- [ ] `Get tournament by id`
## CHAMPION-MASTERY-V4
- [x] `Get all champion mastery entries sorted by number of champion points descending.`
- [ ] `Get a champion mastery by player ID and champion ID.`
- [ ] `Get a player's total champion mastery score, which is the sum of individual champion mastery levels.`
## CHAMPION-V3
- [x] `Get champions free rotation.`
- [x] `Retrieve all champions.`
- [x] `Retrieve champion by NAME.`
## LEAGUE-V4
- [ ] `Get the challenger league for given queue.`
- [ ] `Get league entries in all queues for a given summoner ID.`
- [ ] `Get all the league entries.`
- [ ] `Get the grandmaster league of a specific queue.`
- [ ] `Get league with given ID, including inactive entries.`
- [ ] `Get the master league for given queue.`
- [ ] `Get the queues that have positional ranks enabled.` (deprecated June 17th and in `v0.9.10`)
- [ ] `Get league positions in all queues for a given summoner ID.` (deprecated June 17th and in `v0.9.10`)
- [ ] `Get all the positional league entries.` (deprecated June 17th and in `v0.9.10`)
## LOL-STATUS-V3
- [ ] `Get League of Legends status for the given shard.`
- [ ] `Get matchlist for games played on given account ID and platform ID and filtered using given filter parameters, if any.`
- [ ] `Get match timeline by match ID.`
- [ ] `Get match IDs by tournament code.`
- [ ] `Get match by match ID and tournament code.`
## SPECTATOR-V4
- [ ] `Get current game information for the given summoner ID.`
- [ ] `Get list of featured games.`
## SUMMONER-V4
- [x] `Get a summoner by account ID.`
- [x] `Get a summoner by summoner name.`
- [x] `Get a summoner by PUUID.`
- [x] `Get a summoner by summoner ID.`
## TOURNAMENT-STUB-V4
- [ ] `Create a mock tournament code for the given tournament.`
- [ ] `Gets a mock list of lobby events by tournament code.`
- [ ] `Creates a mock tournament provider and returns its ID.`
- [ ] `Creates a mock tournament and returns its ID.`
## TOURNAMENT-V4
- [ ] `Create a tournament code for the given tournament.`
- [ ] `Returns the tournament code DTO associated with a tournament code string.`
- [ ] `Update the pick type, map, spectator type, or allowed summoners for a code.`
- [ ] `Gets a list of lobby events by tournament code.`
- [ ] `Creates a tournament provider and returns its ID.`
- [ ] `Creates a tournament and returns its ID.`

# TFT Endpoints
## TFT-SUMMONER-V1
- [ ] `Get a summoner by account ID.`
- [ ] `Get a summoner by summoner name.`
- [ ] `Get a summoner by PUUID.`
- [ ] `Get a summoner by summoner ID.`
## TFT-MATCH-V1
- [ ] `Get match list by summoner PUUID.`
- [ ] `Get match list details.`
## TFT-LEAGUE-V1
- [ ] `Get the challenger league for given queue.`
- [ ] `Get league entries in all queues for a given summoner ID.`
- [ ] `Get all the league entries.`
- [ ] `Get league with given ID, including inactive entries.`
- [ ] `Get the master league for given queue.`