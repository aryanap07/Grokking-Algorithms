def select_stations(states_needed, stations):
    """
    Selects a set of stations that covers all required states
    using a greedy approximation algorithm.

    Parameters:
        states_needed (set): States that must be covered.
        stations (dict): Mapping of station -> covered states.

    Returns:
        set: Selected stations.
    """

    remaining_states = states_needed.copy()
    selected_stations = set()

    while remaining_states:
        best_station = None
        states_covered = set()

        for station, covered_states in stations.items():
            covered = remaining_states & covered_states

            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        if best_station is None:
            raise ValueError("Some states cannot be covered.")

        selected_stations.add(best_station)
        remaining_states -= states_covered

    return selected_stations
    
    
states_needed = {
    "mt", "wa", "or", "id",
    "nv", "ut", "ca", "az"
}

stations = {
    "kone":   {"id", "nv", "ut"},
    "ktwo":   {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour":  {"nv", "ut"},
    "kfive":  {"ca", "az"},
}

result = select_stations(states_needed, stations)

print(result)
