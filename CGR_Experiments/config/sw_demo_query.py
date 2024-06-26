sw_demo_query  = [
  {
      'constraint':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Starship)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) RETURN ID(a),ID(b),ID(c)",
      'violation':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Starship)-[r:APPEARED_IN {deleted:false}]->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) AND FILTRI RETURN a,p,b,r,c",
      'new_constraint':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Starship)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) AND FILTRI RETURN ID(a),ID(b),ID(c)",
      'explanation':"A character that pilots a starship that appeared in a film should have appeared in the film (there should exist the edge APPEARED_IN between the character and the film)",
      'create_constraint':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Starship)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) MERGE (a)-[:BELONGS]->(v1:Violation {solved:false, locked:false, nodes: ID(a)+','+ID(b)+','+ID(c)+','+ID(p)+','+ID(r),labels:'a,b,c,p,r', type:0})<-[:BELONGS]-(b) MERGE (v1)<-[:BELONGS]-(c)",
      'check_new_violation':"MATCH (a)-[:BELONGS]->(v1:Violation {solved:False})<-[:BELONGS]-(b), (c)-[:BELONGS]->(v2) WHERE FILTRI AND ID(v1)=ID(v2) RETURN ID(a),ID(b),ID(c)",
      'create_new_violation':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Starship)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) AND FILTRI CREATE (a)-[:BELONGS]->(v1:Violation {solved:false, locked:false, nodes: ID(a)+','+ID(b)+','+ID(c)+','+ID(p)+','+ID(r),labels:'a,b,c,p,r', type:0})<-[:BELONGS]-(b) CREATE (v1)<-[:BELONGS]-(c) RETURN v1",
      'ids':['ID(a)','ID(b)','ID(c)'],
      'possible_repairs':[          
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'explanation':"Delete edge PILOT"},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'explanation':"Delete edge APPEARED_IN"},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'explanation':"Delete both edges APPEARED_IN and PILOT"},
    ],
    'delete_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ],
    'update_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ],
    'num_op_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ],
     'schema_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':3},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ]
   },
  {
      'constraint':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Vehicle)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) RETURN ID(a),ID(b),ID(c)",
      'violation':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Vehicle)-[r:APPEARED_IN {deleted:false}]->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) AND FILTRI RETURN a,p,b,r,c",
      'new_constraint':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Vehicle)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) AND FILTRI RETURN ID(a),ID(b),ID(c)",
      'explanation':"A character that pilots a Vehicle that appeared in a film should have appeared in the film (there should exist the edge APPEARED_IN between the character and the film",
      'create_constraint':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Vehicle)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) MERGE (a)-[:BELONGS]->(v1:Violation {solved:false, locked:false, nodes: ID(a)+','+ID(b)+','+ID(c)+','+ID(p)+','+ID(r),labels:'a,b,c,p,r', type:1})<-[:BELONGS]-(b) MERGE (v1)<-[:BELONGS]-(c);",
      'check_new_violation':"MATCH (a)-[:BELONGS]->(v1:Violation {solved:False})<-[:BELONGS]-(b), (c)-[:BELONGS]->(v2) WHERE FILTRI AND ID(v1)=ID(v2) RETURN ID(a),ID(b),ID(c)",
      'create_new_violation':"MATCH (a:Character)-[p:PILOT {deleted:false}]->(b:Vehicle)-[r:APPEARED_IN {deleted:false}] ->(c:Film) WHERE not (a)-[:APPEARED_IN {deleted:false}]->(c) AND FILTRI CREATE (a)-[:BELONGS]->(v1:Violation {solved:false, locked:false, nodes: ID(a)+','+ID(b)+','+ID(c)+','+ID(p)+','+ID(r),labels:'a,b,c,p,r', type:1})<-[:BELONGS]-(b) CREATE (v1)<-[:BELONGS]-(c) RETURN v1",
      'ids':['ID(a)','ID(b)','ID(c)'],
      'possible_repairs':[          
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'explanation':"Delete edge PILOT"},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'explanation':"Delete edge APPEARED_IN"},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'explanation':"Delete both edges APPEARED_IN and PILOT"},
    ],
    'delete_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ],
    'update_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ],
    'num_op_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ],
     'schema_preferred':[
          {'repair':"MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score': 1},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':3},
          {'repair':"MATCH ()-[r:APPEARED_IN {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:PILOT {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
    ]
   },
   {
      'constraint':"MATCH (a:Species)<-[p:OF {deleted:false}]-(b:Character)-[r:PILOT {deleted:false}]->(c:Starship) WHERE a.average_height>c.height RETURN ID(a),ID(b),ID(c)",
      'violation':"MATCH (a:Species)<-[p:OF {deleted:false}]-(b:Character)-[r:PILOT {deleted:false}]->(c:Starship) WHERE a.average_height>c.height AND FILTRI RETURN a,p,b,r,c",
      'new_constraint':"MATCH (a:Species)<-[p:OF {deleted:false}]-(b:Character)-[r:PILOT {deleted:false}]->(c:Starship) WHERE a.average_height>c.height AND FILTRI RETURN ID(a),ID(b),ID(c)",
      'explanation':"A character that pilots a Starship should have a species with an average height smaller than the Starship's height",
      'create_constraint':"MATCH (a:Species)<-[p:OF {deleted:false}]-(b:Character)-[r:PILOT {deleted:false}]->(c:Starship) WHERE a.average_height>c.height MERGE (a)-[:BELONGS]->(v1:Violation {solved:false, locked:false, nodes: ID(a)+','+ID(b)+','+ID(c)+','+ID(p)+','+ID(r),labels:'a,b,c,p,r', type:2})<-[:BELONGS]-(b) MERGE (v1)<-[:BELONGS]-(c)",
      'check_new_violation':"MATCH (a)-[:BELONGS]->(v1:Violation {solved:False})<-[:BELONGS]-(b), (c)-[:BELONGS]->(v2) WHERE FILTRI AND ID(v1)=ID(v2) RETURN ID(a),ID(b),ID(c)",
      'create_new_violation':"MATCH (a:Species)<-[p:OF {deleted:false}]-(b:Character)-[r:PILOT {deleted:false}]->(c:Starship) WHERE a.average_height>c.height AND FILTRI CREATE (a)-[:BELONGS]->(v1:Violation {solved:false, locked:false, nodes: ID(a)+','+ID(b)+','+ID(c)+','+ID(p)+','+ID(r),labels:'a,b,c,p,r', type:2})<-[:BELONGS]-(b) CREATE (v1)<-[:BELONGS]-(c) RETURN v1",
      'ids':['ID(a)','ID(b)','ID(c)'],
      'possible_repairs':[          
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'explanation':"Delete edge OF"},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'explanation':"Delete edge PILOT"},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'explanation':"Delete both edges OF and PILOT"},
          {'repair':"MATCH (a:Species) WHERE ID(a)=FILTRI SET a.average_height=INPUT",'explanation':"Update average height of the species to"},
          {'repair':"MATCH (c:Starship) WHERE ID(c)=FILTRI SET c.height=INPUT",'explanation':"Update height of the Starship to"},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species) WHERE ID(a)=FILTRI SET a.average_height=INPUT",'explanation':"Delete edge OF and Update average height of the species to"},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (a:Species) WHERE ID(a)=FILTRI SET a.average_height=INPUT",'explanation':"Delete edge PILOT and Update average height of the species to"},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species) WHERE ID(a)=FILTRI SET a.average_height=INPUT",'explanation':"Delete both edges OF and PILOT and Update average height of the species to"},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship) WHERE ID(c)=FILTRI SET c.height=INPUT",'explanation':"Delete edge OF and Update height of the Starship to"},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (c:Starship) WHERE ID(c)=FILTRI SET c.height=INPUT",'explanation':"Delete edge PILOT and Update height of the Starship to"},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship) WHERE ID(c)=FILTRI SET c.height=INPUT",'explanation':"Delete both edges OF and PILOT and Update height of the vehicle to"},
    ],
    'delete_preferred':[
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
          {'repair':"MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':5},
          {'repair':"MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':5},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':3},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':3},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':4},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':3},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':3},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':4},
    ],
    'update_preferred':[
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':4},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':4},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':5},
          {'repair':"MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':1},
          {'repair':"MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':1},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':3},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':3},
    ],
    'num_op_preferred':[
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':1},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':2},
          {'repair':"MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':1},
          {'repair':"MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':1},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':3},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':3},
    ],
    'schema_preferred':[
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':4},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True",'score':4},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True",'score':5},
          {'repair':"MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':3},
          {'repair':"MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':1},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':6},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':6},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (a:Species),(b:Character) WHERE ID(a)=FILTRIA AND ID(b)=FILTRIB SET a.average_height=b.height",'score':7},
          {'repair':"MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':2},
          {'repair':"MATCH ()-[r:PILOT {deleted:false}]->() WHERE ID(r)=FILTRI SET r.updated=True, r.deleted=True UNION MATCH ()-[p:OF {deleted:false}]->() WHERE ID(p)=FILTRI SET p.updated=True, p.deleted=True UNION MATCH (c:Starship),(a:Species) WHERE ID(c)=FILTRIC AND ID(a)=FILTRIA SET c.height=a.average_height+1",'score':4},
    ]
   },
 ]