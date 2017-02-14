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

- [x] Busca bruta usando Dijkstra algorithm modificado
    - [x] Implementar algoritmo sem walk
    - [x] Implementar algo com walk
   

- [ ] Busca usando método aleatório
    - [x] Busca de pontos próximos para fazer transferencia
    - [x] Caminhar aleatoriamente pelas linhas de transporte
    - [ ] Fazer vários testes para ver se os resultados tem significado

- [ ] Como calcular bordas da isocrona dado os pontos

- [ ] Merge o GTFS com o das ruas
 
- [ ] Adicionar tipo de transporte nos edges

- [ ] Calcular indíce de mobilidade urbana para SP

