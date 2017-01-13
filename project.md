Planejamento do Projeto

- Processar GTFS para grafo

    - GTFS raw para SQL (veja instruções no to_SQL, confira usando Explore Database.ipynb) OK
    
    - A estrura do Grafo deve ser tal que:
    
        - direcional OK
        
        - Nodes devem conter: trip_id{horário de parada}, localizacao (lat, long), stop_id OK
        
        - Edges devem conter: tempo de viagem, trip_id OK

- Busca bruta usando Dijkstra algorithm modificado

- Localizar GTFS num mapa usando javascript

- Invetar jeito de calcular isocrona em mapa de rua - caminhada
- Merge o GTFS com o das ruas

--Calcular indíce de locomoção para SP
