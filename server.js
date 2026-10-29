const button = document.getElementById("runButton");

button.addEventListener("click", function () {
    const name = document.getElementById("name").value.trim();
    const cpu = Number(document.getElementById("cpu").value);
    const ram = Number(document.getElementById("ram").value);
    const result = document.getElementById("result");

    if (
        name === "" ||
        !Number.isInteger(cpu) ||
        !Number.isInteger(ram) ||
        cpu <= 0 ||
        ram <= 0
    ) {
        result.textContent =
            "Please enter a name and valid CPU and RAM values.";
        return;
    }

    if (cpu > 8 || ram > 16) {
        result.textContent =
            "This container exceeds the capacity of one server.";
        return;
    }

    result.textContent =
        name + ": Details accepted! Next, we will connect the Python placement algorithm.";
});