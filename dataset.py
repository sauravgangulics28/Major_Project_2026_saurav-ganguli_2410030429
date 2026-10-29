
import csv
import random

random.seed(42)

with open("container_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "container_cpu",
        "container_ram",
        "server1_free_cpu",
        "server1_free_ram",
        "server2_free_cpu",
        "server2_free_ram",
        "server3_free_cpu",
        "server3_free_ram",
        "best_server"
    ])

    for _ in range(1000):
        container_cpu = random.randint(1, 4)
        container_ram = random.randint(1, 8)

        servers = []

        for _ in range(3):
            free_cpu = random.randint(1, 8)
            free_ram = random.randint(2, 16)
            servers.append((free_cpu, free_ram))

        scores = []

        for cpu, ram in servers:
            if cpu >= container_cpu and ram >= container_ram:
                score = (
                    (cpu - container_cpu) / 8
                    + (ram - container_ram) / 16
                )
            else:
                score = float("inf")

            scores.append(score)

        if min(scores) == float("inf"):
            continue

        best_index = scores.index(min(scores))

        writer.writerow([
            container_cpu,
            container_ram,
            servers[0][0], servers[0][1],
            servers[1][0], servers[1][1],
            servers[2][0], servers[2][1],
            best_index + 1
        ])

print("Dataset created successfully!")
