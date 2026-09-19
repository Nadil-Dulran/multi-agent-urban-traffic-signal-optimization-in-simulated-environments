import os
import traci

sumo_cfg = os.path.abspath("scenarios/grid3x3/grid3x3.sumo.cfg")

sumo_cmd = [
    "sumo",
    "-c",
    sumo_cfg,
]

traci.start(sumo_cmd)

print("SUMO connected successfully!")
print("Simulation time:", traci.simulation.getTime())
print("Vehicles:", len(traci.vehicle.getIDList()))

for _ in range(10):
    traci.simulationStep()

print("After 10 steps:")
print("Simulation time:", traci.simulation.getTime())
print("Vehicles:", len(traci.vehicle.getIDList()))

traci.close()

print("TraCI test completed successfully!")
