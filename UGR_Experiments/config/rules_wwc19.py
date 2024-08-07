rules={"rules":["?a  PLAYED_IN  ?b   => ?a  SCORED_GOAL  ?b",
"?a  SCORED_GOAL  ?b   => ?a  PLAYED_IN  ?b",
"?g  COACH_FOR  ?b  ?g  REPRESENTS  ?a   => ?a  NAMED  ?b",
"?h  FOR  ?b  ?a  NAMED  ?h   => ?a  PARTICIPATED_IN  ?b",
"?g  NAMED  ?a  ?g  PARTICIPATED_IN  ?b   => ?a  FOR  ?b	",
"?a  FOR  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?a  COACH_FOR  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?a  PARTICIPATED_IN  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?a  NAMED  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?g  IN_SQUAD  ?b  ?g  REPRESENTS  ?a   => ?a  NAMED  ?b",
"?h  IN_TOURNAMENT  ?b  ?a  PLAYED_IN  ?h   => ?a  PARTICIPATED_IN  ?b",
"?g  NAMED  ?a  ?g  hasSynth  ?b   => ?a  hasSynth  ?b",
"?a  IN_TOURNAMENT  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?g  COACH_FOR  ?a  ?g  hasSynth  ?b   => ?a  hasSynth  ?b",
"?g  REPRESENTS  ?a  ?g  hasSynth  ?b   => ?a  hasSynth  ?b",
"?a  SCORED_GOAL  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?g  NAMED  ?b  ?a  REPRESENTS  ?g   => ?a  IN_SQUAD  ?b	",
"?a  IN_SQUAD  ?h  ?b  NAMED  ?h   => ?a  REPRESENTS  ?b	",
"?g  PARTICIPATED_IN  ?b  ?g  PLAYED_IN  ?a   => ?a  IN_TOURNAMENT  ?b	",
"?g  SCORED_GOAL  ?a  ?g  hasSynth  ?b   => ?a  hasSynth  ?b",
"?a  IN_SQUAD  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?b  IN_TOURNAMENT  ?h  ?a  PARTICIPATED_IN  ?h   => ?a  PLAYED_IN  ?b",
"?g  PLAYED_IN  ?b  ?g  REPRESENTS  ?a   => ?a  PLAYED_IN  ?b",
"?g  IN_SQUAD  ?a  ?g  hasSynth  ?b   => ?a  hasSynth  ?b",
"?g  REPRESENTS  ?a  ?g  SCORED_GOAL  ?b   => ?a  PLAYED_IN  ?b",
"?g  PLAYED_IN  ?a  ?g  hasSynth  ?b   => ?a  hasSynth  ?b",
"?a  PLAYED_IN  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b",
"?h  PLAYED_IN  ?b  ?a  REPRESENTS  ?h   => ?a  PLAYED_IN  ?b",
"?a  REPRESENTS  ?h  ?h  hasSynth  ?b   => ?a  hasSynth  ?b"],
"queries":["MATCH (a)-[:PLAYED_IN]->(b) MERGE (a)-[:SCORED_GOAL {added:True}]->(b)",
"MATCH (a)-[:SCORED_GOAL]->(b) MERGE (a)-[:PLAYED_IN {added:True}]->(b)",
"MATCH (g)-[:COACH_FOR]->(b)-[:REPRESENTS]->(a) MERGE (a)-[:NAMED {added:True}]->(b)",
"MATCH (h)-[:FOR]->(b)-[:NAMED]->(h) MERGE (a)-[:PARTICIPATED_IN {added:True}]->(b)",
"MATCH (g)-[:NAMED]->(a)-[:PARTICIPATED_IN]->(b) MERGE (a)-[:FOR {added:True}]->(b)",
"MATCH (a)-[:FOR]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (a)-[:COACH_FOR]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (a)-[:PARTICIPATED_IN]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (a)-[:NAMED]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (g)-[:IN_SQUAD]->(b)-[:REPRESENTS]->(a) MERGE (a)-[:NAMED {added:True}]->(b)",
"MATCH (h)-[:IN_TOURNAMENT]->(b)-[:PLAYED_IN]->(h) MERGE (a)-[:PARTICIPATED_IN {added:True}]->(b)",
"MATCH (g)-[:NAMED]->(a) SET a.synth1 = g.synth1, a.updated = True",
"MATCH (a)-[:IN_TOURNAMENT]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (g)-[:COACH_FOR]->(a) SET a.synth1 = g.synth1, a.updated = True",
"MATCH (g)-[:REPRESENTS]->(a) SET a.synth1 = g.synth1, a.updated = True",
"MATCH (a)-[:SCORED_GOAL]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (g)-[:NAMED]->(b)-[:REPRESENTS]->(a) MERGE (a)-[:IN_SQUAD {added:True}]->(b)",
"MATCH (a)-[:IN_SQUAD]-(h)-[:NAMED]->(h) MERGE (a)-[:REPRESENTS {added:True}]->(h)",
"MATCH (g)-[:PARTICIPATED_IN]->(b)-[:PLAYED_IN]->(a) MERGE (a)-[:IN_TOURNAMENT {added:True}]->(b)",
"MATCH (g)-[:SCORED_GOAL]->(a) SET a.synth1 = g.synth1, a.updated = True",
"MATCH (a)-[:IN_SQUAD]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (b)-[:IN_TOURNAMENT]-(h)-[:PARTICIPATED_IN]->(a) MERGE (a)-[:PLAYED_IN {added:True}]->(b)",
"MATCH (g)-[:PLAYED_IN]->(b)-[:REPRESENTS]->(a) MERGE (a)-[:PLAYED_IN {added:True}]->(b)",
"MATCH (g)-[:IN_SQUAD]->(a) SET a.synth1 = g.synth1, a.updated = True",
"MATCH (g)-[:REPRESENTS]->(a)-[:SCORED_GOAL]->(b) MERGE (a)-[:PLAYED_IN {added:True}]->(b)",
"MATCH (g)-[:PLAYED_IN]->(a) SET a.synth1 = g.synth1, a.updated = True",
"MATCH (a)-[:PLAYED_IN]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (h)-[:PLAYED_IN]-(b)-[:REPRESENTS]->(a) MERGE (a)-[:PLAYED_IN {added:True}]->(b)",
"MATCH (a)-[:REPRESENTS]-(h) SET a.synth1 = h.synth1, a.updated = True",
"MATCH (a)-[r:SYNTH]-(b) set r.deleted=True"
]
}