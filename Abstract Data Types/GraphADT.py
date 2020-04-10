Functions:
insertVertex(K Key);
insertEdge(Vertex v1, Vertex v2, K Key);  //maybe data

removeVertex(Vertex v);
removeEdge(Vertex v1, Vertex v2);

incidentEdges(Vertex v);  //what are the incident edges
areAdjacent(Vertex v1, Vertex v2);  //see if two vertices  are adjacent

origin(Edge e);   //IF graph is directional
destination(Edge e); //IF graph is directional
