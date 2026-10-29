

from copy import deepcopy

server_template = [
    {"name": "Server 1", "cpu": 8, "ram": 16},
    {"name": "Server 2", "cpu": 8, "ram": 16},
    {"name": "Server 3", "cpu": 8, "ram": 16},
]

containers = [
    {"name": "Container A", "cpu": 2, "ram": 4},
    {"name": "Container B", "cpu": 4, "ram": 6},
    {"name": "Container C", "cpu": 3, "ram": 4},
    {"name": "Container D", "cpu": 2, "ram": 2},
    {"name": "Container E", "cpu": 4, "ram": 8},
    {"name": "Container F", "cpu": 1, "ram": 2},
]


def run_placement(algorithm):
    servers = deepcopy(server_template)

    for server in servers:
        server["used_cpu"] = 0
        server["used_ram"] = 0
        server["containers"] = []

    for container in containers:
        candidates = []

        for server in servers:
            free_cpu = server["cpu"] - server["used_cpu"]
            free_ram = server["ram"] - server["used_ram"]

            if (container["cpu"] <= free_cpu
                    and container["ram"] <= free_ram):

                if algorithm == "First Fit":
                    candidates.append((0, server))
                    break

                # Best Fit: minimize normalized remaining capacity
                remaining_cpu = (
                    free_cpu - container["cpu"]
                ) / server["cpu"]

                remaining_ram = (
                    free_ram - container["ram"]
                ) / server["ram"]

                score = remaining_cpu + remaining_ram
                candidates.append((score, server))

        if candidates:
            chosen_server = min(
                candidates, key=lambda item: item[0]
            )[1]

            chosen_server["used_cpu"] += container["cpu"]
            chosen_server["used_ram"] += container["ram"]
            chosen_server["containers"].append(container["name"])

            print(
                f"{container['name']} -> {chosen_server['name']}"
            )
        else:
            print(f"{container['name']} -> Not placed")

    return servers


def show_results(algorithm, servers):
    print(f"\n--- {algorithm} RESULTS ---")

    total_cpu = sum(s["cpu"] for s in servers)
    total_ram = sum(s["ram"] for s in servers)
    used_cpu = sum(s["used_cpu"] for s in servers)
    used_ram = sum(s["used_ram"] for s in servers)

    active_servers = 0

    for server in servers:
        if server["containers"]:
            active_servers += 1

        cpu_percent = 100 * server["used_cpu"] / server["cpu"]
        ram_percent = 100 * server["used_ram"] / server["ram"]

        print(f"\n{server['name']}")
        print("Containers:", server["containers"])
        print(f"CPU: {cpu_percent:.1f}%")
        print(f"RAM: {ram_percent:.1f}%")

    print("\nOverall CPU utilization:",
          f"{100 * used_cpu / total_cpu:.1f}%")
    print("Overall RAM utilization:",
          f"{100 * used_ram / total_ram:.1f}%")
    print("Active servers:", active_servers)


first_fit_servers = run_placement("First Fit")
show_results("First Fit", first_fit_servers)

best_fit_servers = run_placement("Best Fit")
show_results("Best Fit", best_fit_servers)
