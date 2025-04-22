import math
import random

# Constants
Q_LIMIT = 100
BUSY = 1
IDLE = 0

class SimulationState:
    def __init__(self):
        self.next_event_type = 0
        self.num_custs_delayed = 0
        self.num_delays_required = 0
        self.num_events = 2
        self.num_in_q = 0
        self.server_status = IDLE
        self.area_num_in_q = 0.0
        self.area_server_status = 0.0
        self.mean_interarrival = 0.0
        self.mean_service = 0.0
        self.sim_time = 0.0
        self.time_arrival = [0.0] * (Q_LIMIT + 1)
        self.time_last_event = 0.0
        self.time_next_event = [0.0] * 3
        self.total_of_delays = 0.0

        self.infile = None
        self.outfile = None

# Function to generate exponential random variates
def expon(mean):
    return -mean * math.log(random.random())

# Initialize simulation state
def initialize(state):
    state.sim_time = 0.0
    state.server_status = IDLE
    state.num_in_q = 0
    state.time_last_event = 0.0
    state.num_custs_delayed = 0
    state.total_of_delays = 0.0
    state.area_num_in_q = 0.0
    state.area_server_status = 0.0

    # Schedule the first arrival using exponential distribution
    state.time_next_event[1] = state.sim_time + expon(state.mean_interarrival)
    
    # Departure time is initially set to infinity (no customer in service)
    state.time_next_event[2] = float('inf')

# Determine the next event type and advance simulation time
def timing(state):
    min_time_next_event = float('inf')
    state.next_event_type = 0

    for i in range(1, state.num_events + 1):
        if state.time_next_event[i] < min_time_next_event:
            min_time_next_event = state.time_next_event[i]
            state.next_event_type = i

    if state.next_event_type == 0:
        raise Exception(f"Event list empty at time {state.sim_time:.2f}")

    # Advance simulation time to the next event
    state.sim_time = min_time_next_event

# Handle customer arrival
def arrive(state):
    # Schedule the next arrival using exponential distribution
    state.time_next_event[1] = state.sim_time + expon(state.mean_interarrival)

    if state.server_status == BUSY:
        state.num_in_q += 1

        if state.num_in_q > Q_LIMIT:
            raise Exception(f"Queue overflow at time {state.sim_time:.2f}")

        state.time_arrival[state.num_in_q] = state.sim_time
    else:
        delay = 0.0
        state.total_of_delays += delay
        state.num_custs_delayed += 1
        state.server_status = BUSY

        # Schedule a departure using exponential service time
        state.time_next_event[2] = state.sim_time + expon(state.mean_service)

# Handle customer departure
def depart(state):
    if state.num_in_q == 0:
        state.server_status = IDLE
        state.time_next_event[2] = float('inf')
    else:
        state.num_in_q -= 1
        delay = state.sim_time - state.time_arrival[1]
        state.total_of_delays += delay
        state.num_custs_delayed += 1

        # Schedule next departure using exponential distribution
        state.time_next_event[2] = state.sim_time + expon(state.mean_service)

        for i in range(1, state.num_in_q + 1):
            state.time_arrival[i] = state.time_arrival[i + 1]

# Update statistical accumulators
def update_time_avg_stats(state):
    time_since_last_event = state.sim_time - state.time_last_event
    state.time_last_event = state.sim_time

    state.area_num_in_q += state.num_in_q * time_since_last_event
    state.area_server_status += state.server_status * time_since_last_event

# Generate final report
def report(state):
    state.outfile.write("\nSingle-server queueing system\n\n")
    state.outfile.write(f"Mean interarrival time {state.mean_interarrival:11.3f} minutes\n")
    state.outfile.write(f"Mean service time     {state.mean_service:11.3f} minutes\n")
    state.outfile.write(f"Number of customers   {state.num_delays_required:11d}\n\n")

    state.outfile.write(f"Average delay in queue     {state.total_of_delays / state.num_custs_delayed:11.3f} minutes\n")
    state.outfile.write(f"Average number in queue    {state.area_num_in_q / state.sim_time:11.3f}\n")
    state.outfile.write(f"Server utilization         {state.area_server_status / state.sim_time:11.3f}\n")
    state.outfile.write(f"Time simulation ended      {state.sim_time:11.3f} minutes\n")

# Main driver
def main():
    state = SimulationState()

    try:
        state.infile = open("mm1.in", "r")
        state.outfile = open("mm1.out", "w")

        input_line = state.infile.readline().strip()

        if not input_line:
            raise ValueError("Input file is empty or improperly formatted.")

        values = list(map(float, input_line.split()))

        if len(values) < 3:
            raise ValueError(f"Not enough values in input file. Expected 3 values, got {len(values)}.")

        state.mean_interarrival, state.mean_service, num_delays = values
        state.num_delays_required = int(num_delays)

        initialize(state)

        while state.num_custs_delayed < state.num_delays_required:
            timing(state)
            update_time_avg_stats(state)

            if state.next_event_type == 1:
                arrive(state)
            elif state.next_event_type == 2:
                depart(state)

        report(state)

    except FileNotFoundError:
        print("Error: Could not find mm1.in input file.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    finally:
        if state.infile:
            state.infile.close()
        if state.outfile:
            state.outfile.close()

if __name__ == "__main__":
    main()
