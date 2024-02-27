class TrainSystem:
    def __init__(location):
        location.trainsG = {
            # lrt1
            'Roosevelt': ['Balintawak'],
            'Balintawak': ['Roosevelt', 'Monumento'],
            'Monumento': ['Balintawak', '5th Avenue'],
            '5th Avenue': ['Monumento', 'R. Papa'],
            'R. Papa': ['5th Avenue', 'Abad Santos'],
            'Abad Santos': ['R. Papa', 'Blumentritt'],
            'Blumentritt': ['Abad Santos', 'Tayuman'],
            'Tayuman': ['Blumentritt', 'Bambang'],
            'Bambang': ['Tayuman', 'Donoteo Jose'],
            'Donoteo Jose': ['Bambang', 'Carriedo', 'Recto'],
            'Carriedo': ['Donoteo Jose', 'Central Terminal'],
            'Central Terminal': ['Carriedo', 'United Nations'],
            'United Nations': ['Central Terminal', 'Pedro Gil'],
            'Pedro Gil': ['United Nations', 'Quirino'],
            'Quirino': ['Pedro Gil', 'Vito Cruz'],
            'Vito Cruz': ['Quirino', 'Gil Puyat'],
            'Gil Puyat': ['Vito Cruz', 'Libertad'],
            'Libertad': ['Gil Puyat', 'EDSA'],
            'EDSA': ['Libertad', 'Baclaran'],
            'Baclaran': ['EDSA'],

            # lrt2
            'Antipolo': ['Marikina- Pasig'],
            'Marikina- Pasig': ['Santolan', 'Antipolo'],
            'Santolan': ['Katipunan'],
            'Katipunan': ['Santolan', 'Anonas'],
            'Anonas': ['Katipunan', 'Araneta Center-Cubao'],
            'Araneta Center-Cubao': ['Anonas', 'Betty Go-Belmonte', 'Kamuning', 'Araneta Center-Cubao', 'Santolan-Annapolis'],
            'Betty Go-Belmonte': ['Araneta Center-Cubao', 'Gilmore'],
            'Gilmore': ['Betty Go-Belmonte', 'J. Ruiz'],
            'J. Ruiz': ['Gilmore', 'V. Mapa'],
            'V. Mapa': ['J. Ruiz', 'Pureza'],
            'Pureza': ['V. Mapa', 'Legarda'],
            'Legarda': ['Pureza', 'Recto'],
            'Recto': ['Donoteo Jose', 'Legarda'],

            # mrt3
            'North Avenue': ['Quezon Avenue'],
            'Quezon Avenue': ['North Avenue', 'Kamuning'],
            'Kamuning': ['Quezon Avenue', 'Araneta Center-Cubao'],
            'Araneta Center-Cubao': ['Kamuning', 'Santolan-Annapolis', 'Araneta Center-Cubao', 'Anonas', 'Betty Go-Belmonte'],
            'Santolan-Annapolis': ['Araneta Center-Cubao', 'Ortigas'],
            'Ortigas': ['Santolan-Annapolis', 'Shaw Boulevard'],
            'Shaw Boulevard': ['Ortigas', 'Boni'],
            'Boni': ['Shaw Boulevard', 'Guadalupe'],
            'Guadalupe': ['Boni', 'Buendia'],
            'Buendia': ['Guadalupe', 'Ayala'],
            'Ayala': ['Buendia', 'Magallanes'],
            'Magallanes': ['Ayala', 'Taft Avenue'],
            'Taft Avenue': ['Magallanes', 'EDSA']
        }
        location.stored_value_fare = 13  # stored value beep card
        location.single_journey_fare = 15  # single journey beep card

    def sp(self, network, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in network:
            return None
        shortest = None
        for station in network[start]:
            if station not in path:
                newpath = self.sp(network, station, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def trainArrival(self, station):
        if station in lrt1_stations:
            return 'LRT1'
        elif station in lrt2_stations:
            return 'LRT2'
        elif station in mrt3_stations:
            return 'MRT3'
        else:
            return None
    def calculate_fare(self, stations_passed, card_type, trains_taken):
      fare = 0
      if card_type == 'a':
          fare += self.stored_value_fare * len(trains_taken)
          fare += (stations_passed - 1) * len(trains_taken)  # Adding 1 peso for each station after the first
      elif card_type =='b':
          fare += self.single_journey_fare * len(trains_taken)
          fare += (stations_passed // 2) * len(trains_taken) * 5  # Adding 5 pesos for every 2 stations
      return fare


    def find_shortest_path(self, start_station, end_station):
        path = self.sp(self.trainsG, start_station, end_station)
        return path

def RunTS():
    line = "===================================================="
    train_system = TrainSystem()
    start_station = input("When entering a location ensure that it's the full name of the station\nand also the first letter should be in Capital\n\nEx: Pasig-Marikina or Anonas\n" + line  + ("\nEnter start station: "))
    end_station = input("Enter end station: ")
    print(line)
    card_type = input("\nEnter type of beep card:(Press the either a or b)\nStored value (a)  Single Journey (b): ")
    print (line)
    path = train_system.find_shortest_path(start_station, end_station)
    if path:
        print("Shortest path from", start_station, "to", end_station, ":")
        stations_passed = len(path)
        trains_taken = set()
        for i in range(len(path)):
            station = path[i]
            train = train_system.trainArrival(station)
            if train:
                trains_taken.add(train)
            print(f"{station} ({train})", end=" -> " if i < len(path) - 1 else "\n")

        total_fare = train_system.calculate_fare(stations_passed, card_type, trains_taken)
        print(line+(f"\nStations passed: {stations_passed}"))
        print(line+(f"\nDifferent trains taken: {len(trains_taken)}"))
        print(line+(f"\nTotal fare: {total_fare} pesos"))
    else:
        print(line +"\nNo path found from", start_station, "to", end_station)

lrt1_stations = set([
    'Roosevelt', 'Balintawak', 'Monumento', '5th Avenue', 'R. Papa', 'Abad Santos',
    'Blumentritt', 'Tayuman', 'Bambang', 'Doroteo Jose', 'Carriedo', 'Central Terminal',
    'United Nations', 'Pedro Gil', 'Quirino', 'Vito Cruz', 'Gil Puyat', 'Libertad',
    'EDSA', 'Baclaran'
])

lrt2_stations = set([
   'Antipolo','Marikina- Pasig', 'Santolan', 'Katipunan', 'Anonas', 'Araneta Center-Cubao', 'Betty Go-Belmonte',
    'Gilmore', 'J. Ruiz', 'V. Mapa', 'Pureza', 'Legarda', 'Recto'
])

mrt3_stations = set([
    'North Avenue', 'Quezon Avenue', 'Kamuning', 'Araneta Center-Cubao',
    'Santolan-Annapolis', 'Ortigas', 'Shaw Boulevard', 'Boni', 'Guadalupe',
    'Buendia', 'Ayala', 'Magallanes', 'Taft Avenue'
])

RunTS()
