# Kairos
Isochron analysis of the city of SP

### Info

- O grafo que contém todos os stops com o timetable de SP está em *graphs/sp_final.gexf*
- Para ler os grafo de maneira correta use o script em *scripts/read_graph.py*

### Planejamento do Projeto

- [x] Processar GTFS para grafo

    - [x] GTFS raw para SQL (veja instruções no to_SQL, confira usando Explore Database.ipynb) 
    
    - [x] A estrura do Grafo deve ser tal que:
    
        - [x] direcional 
        
        - [x] Nodes devem conter: trip_id{horário de parada}, localizacao (lat, long), stop_id 
        
        - [x] Edges devem conter: tempo de viagem, trip_id 

- [x] Visualização do mapa
    - [x] Plotar mapa
    - [x] Plotar pontos de onibus no mapa

- [ ] Busca bruta usando Dijkstra algorithm modificado

- [ ] Localizar GTFS num mapa usando javascript

- [ ] Invetar jeito de calcular isocrona em mapa de rua - caminhada
- [ ] Merge o GTFS com o das ruas

- [ ] Calcular indíce de locomoção para SP

