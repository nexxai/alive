def save_results(alive, filename):
    with open(filename, "w") as f:
        for h in sorted(alive):
            f.write(h + "\n")
