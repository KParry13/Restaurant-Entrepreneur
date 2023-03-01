from simulation import Simulation

sim = Simulation()
sim.run_simulation()

def write_to_file(message):
    file = open("log.txt", "a")
    file.write (message)
    file.close()

write_to_file("!/n")

