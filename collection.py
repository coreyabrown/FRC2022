import csv
from mmap import ALLOCATIONGRANULARITY
import os
import datetime
import vari as v

# Get all events up to today
allEvents = v.tba.events(v.year, "simple")
events = []

for event in allEvents:
    startDateString = event["start_date"]
    startDateValues = startDateString.split("-")
    startDate = datetime.date(int(startDateValues[0]), int(startDateValues[1]), int(startDateValues[2]))
    if startDate < datetime.date.today() and startDate > datetime.date(2022,3,1):
        eventKey = event["key"]
        events.append(eventKey)

# Create csv for data
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ["Event ID", "Match ID", "Alliance Color", "Team 1", "Team 2", "Team 3", "Overall Score", "Overall Difference", "Auto Score", "Auto Difference", "Hangar Score", "Hangar Difference", "Penalty Score", "Penalty Difference", "Result"]
    writer.writerow(header)

    for event in events:
        eventID = event
        eventMatches = v.tba.event_matches(event)

        # Get Matches from each event
        for match in eventMatches:
            matchID = match["key"]
            if match["actual_time"] == None:
                break

            # Get match results
            for alliance in match["alliances"]:
                allianceColor = alliance
                if allianceColor == v.blue:
                    oppositeAlliance = v.red
                else:
                     oppositeAlliance = v.blue

                teamOne = match["alliances"][allianceColor]["team_keys"][0]
                teamTwo = match["alliances"][allianceColor]["team_keys"][1]
                teamThree = match["alliances"][allianceColor]["team_keys"][2]
                autoScore = match["score_breakdown"][allianceColor]["autoCargoPoints"] + match["score_breakdown"][allianceColor]["autoTaxiPoints"]
                overallScore = match["alliances"][allianceColor]["score"]
                hangarScore = match["score_breakdown"][allianceColor]["endgamePoints"]
                penaltyScore = match["score_breakdown"][allianceColor]["foulPoints"]
                if match["winning_alliance"] == allianceColor:
                    result = "Win"
                elif (match["winning_alliance"] == v.red or match["winning_alliance"] == v.blue) and match["winning_alliance"] != allianceColor:
                    result = "Loss"
                else:
                    result = "Tie"
                
                # Get differences
                overallDiff = match["alliances"][allianceColor]["score"] - match["alliances"][oppositeAlliance]["score"]
                autoDiff = match["score_breakdown"][allianceColor]["autoCargoPoints"] + match["score_breakdown"][allianceColor]["autoTaxiPoints"] - match["score_breakdown"][oppositeAlliance]["autoCargoPoints"] - match["score_breakdown"][oppositeAlliance]["autoTaxiPoints"]
                hangarDiff = match["score_breakdown"][allianceColor]["endgamePoints"] - match["score_breakdown"][oppositeAlliance]["endgamePoints"]
                penaltyDiff = match["score_breakdown"][allianceColor]["foulPoints"] - match["score_breakdown"][oppositeAlliance]["foulPoints"]

                # Write match results
                row = [eventID, matchID, allianceColor, teamOne, teamTwo, teamThree, overallScore, overallDiff, autoScore, autoDiff, hangarScore, hangarDiff, penaltyScore, penaltyDiff, result]
                print(row)
                writer.writerow(row)

