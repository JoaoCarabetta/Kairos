import networkx as nx
import sqlite3
import pandas as pd
import time


def getpath(nested_dict, value, prepath=()):
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value: # found value
            return path
        elif hasattr(v, 'items'): # v is a dict
            p = getpath(v, value, path) # recursive call
            if p is not None:
                return p

def main(total):

    conn = sqlite3.connect('/Users/Admin/Documents/Projects/Kairos/Kairos/data/GTFS.db')

    t = time.time() - total
    print('{} seconds to read SQL'.format(time.time() - total))


    stops = pd.read_sql_query('SELECT * FROM gtfs_stops', conn)
    stops_time = pd.read_sql_query('SELECT * FROM gtfs_stop_times', conn)
    frequencies = pd.read_sql_query('SELECT * FROM gtfs_frequencies', conn)
    stops_time_first = stops_time[stops_time['stop_sequence'] == 1].reset_index(drop=True)

    MG = nx.MultiDiGraph()


    for i, row in stops.iterrows():
        MG.add_node(row['stop_id'], location={'long': row['stop_lon'], 'lat': row['stop_lat']})

    stops_time.sort_values(by=['trip_id', 'stop_sequence'], inplace=True)

    t = time.time() - t
    print('{} seconds to add stops'.format(t))

    for i, row in stops_time.iterrows():

        if i + 1 < len(stops_time):
            partida, chegada = stops_time.iloc[i], stops_time.iloc[i + 1]

        if chegada['trip_id'] == partida['trip_id']:
            MG.add_edge(partida['stop_id'], chegada['stop_id'],
                        attr={
                            'tempo'  : chegada['departure_time_seconds'] - partida['arrival_time_seconds'],
                            'trip_id': chegada['trip_id']}
                      )

    t = time.time() - t
    print('{} seconds to add edges'.format(t))

    for i, row in stops_time_first.iterrows():

        if i % 100 == 0:
            #print('id', i)
            pass

        lista = []
        lista.append(row['arrival_time_seconds'])
        trip = frequencies[frequencies['trip_id'] == row['trip_id']]

        rodou = 0
        fullday = 0

        if len(trip[(trip["start_time_seconds"] <= lista[0]) &
                (trip["end_time_seconds"] + 60 >= lista[0])]) > 0:

            # Para baixo
            while 1:

                ultimo = lista[-1]
                timetable = trip[(trip["start_time_seconds"] <= ultimo) &
                                 (trip["end_time_seconds"] + 60 >= ultimo)]

                if len(timetable) > 0:

                    soma = timetable['headway_secs'].values[0] + ultimo

                    if rodou == 1 and soma > lista[0]:
                        fullday = 1
                        #print('fullday')
                        break

                    else:
                        if soma <= 86340:
                            lista.append(soma)
                        else:
                            rodou = 1
                            lista.append(soma - 86340)

                else:
                    break

            # Para cima
            while fullday == 0:

                primeiro = lista[0]
                timetable_atual = trip[(trip["start_time_seconds"] <= primeiro)
                                       & (trip["end_time_seconds"] + 60 >= primeiro)]

                if timetable_atual['start_time_seconds'].values[0] == 0:
                    timetable_anterior = trip[trip['end_time_seconds'] == 82740]
                else:
                    timetable_anterior = trip[(trip['end_time_seconds']) ==
                                              timetable_atual['start_time_seconds'].values[0] - 60]

                # com timetable anterior
                if len(timetable_anterior) > 0:

                    subt = primeiro - timetable_anterior['headway_secs'].values[0]
                    if subt < 0:
                        subt = subt + 82740

                    # se dentro da timetable anterior
                    if subt <= timetable_anterior['end_time_seconds'].values[0]:
                        lista.insert(0, subt)
                    else:
                        lista.insert(0, primeiro - timetable_atual['headway_secs'].values[0])

                # se dentro da timetable atual mas timetable anterior inexistente

                elif ((primeiro - timetable_atual['headway_secs'].values[0]) >=
                          timetable_atual['start_time_seconds'].values[0]):

                    lista.insert(0, primeiro - timetable_atual['headway_secs'].values[0])

                else:
                    break

            if 'viagens' in MG.node[row['stop_id']]:
                MG.node[row['stop_id']]['viagens'][row['trip_id']] = lista
            else:
                MG.node[row['stop_id']]['viagens'] = {row['trip_id']: lista}

        else:
            #print('pulou')
            pass

    t = time.time() - t
    print('{} seconds to get timetable for first stops'.format(t))

    for i, row in stops_time_first.iterrows():

        if i % 100 == 0:
            #print(i)
            pass

        trip_id = row['trip_id']
        stop_id_velho = row['stop_id']

        outputs_set = []
        j = 0

        while 1:

            output = getpath(MG.edge[stop_id_velho], trip_id)  # get path in edge dict to stop_id

            if output == None or output in outputs_set:  # if no path or already visited, break
                break
            else:
                outputs_set.append(output)

            stop_id_novo, number, *oi = output  # distribuir variáveis

            # get previous timetable
            try:
                timetable = MG.node[stop_id_velho]['viagens'][trip_id]
            except KeyError:
                #print(stop_id_velho)
                continue

            # get trip time
            trip_time = MG.edge[stop_id_velho][stop_id_novo][number]['attr']['tempo']

            # generate new timetable
            newtimetable = [i + trip_time for i in MG.node[stop_id_velho]['viagens'][trip_id]]

            # append new timetable to stop
            if 'viagens' in MG.node[stop_id_novo]:
                MG.node[stop_id_novo]['viagens'][trip_id] = newtimetable
            else:
                MG.node[stop_id_novo]['viagens'] = {trip_id: newtimetable}

            # replace stop_ids
            stop_id_velho = stop_id_novo

            j = j + 1
    t = time.time() - t
    print('{} seconds to add timetable to all stops'.format(t))

    nx.write_gexf(MG, '/Users/Admin/Documents/Projects/Kairos/Kairos/graphs/sp_final.gexf')

    t = time.time() - t
    print('{} seconds to write file'.format(t))

if __name__ == '__main__':
    t = time.time()
    print('Generating Graph based on SQL file...')
    main(t)

    t = time.time() - t
    print('{} seconds to do all'.format(t))