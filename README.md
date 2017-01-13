# Kairos
Isochron analysis of the city of SP

### Planejamento do Projeto

- [x] Processar GTFS para grafo

    - [x] GTFS raw para SQL (veja instruções no to_SQL, confira usando Explore Database.ipynb) 
    
    - [x] A estrura do Grafo deve ser tal que:
    
        - [x] direcional 
        
        - [x] Nodes devem conter: trip_id{horário de parada}, localizacao (lat, long), stop_id 
        
        - [x] Edges devem conter: tempo de viagem, trip_id 

- [ ] Busca bruta usando Dijkstra algorithm modificado

- [ ] Localizar GTFS num mapa usando javascript

- [ ] Invetar jeito de calcular isocrona em mapa de rua - caminhada
- [ ] Merge o GTFS com o das ruas

- [ ] Calcular indíce de locomoção para SP

