states_needed = set(["a", "b", "c", "d", "e", "f", "g", "h"])

stations = {}

stations["k1"] = set(["a", "b", "c"])
stations["k2"] = set(["c", "d", "e"])
stations["k3"] = set(["f", "g", "h"])
stations["k4"] = set(["a", "b", "c", "d"])
stations["k5"] = set(["e", "f", "g", "h"])

final_stations = set()

while states_needed:
    best_station = None
    states_not_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_not_covered):
            best_station = station
            states_not_covered = covered

    states_needed -= states_not_covered
    final_stations.add(best_station)

print(final_stations)
