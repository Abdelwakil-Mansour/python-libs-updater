import subprocess

def save_pip_list(filename="installed_packages.txt"):
    with open(filename, "w") as f:
        subprocess.run(["pip", "list"], stdout=f, text=True)

def get_packages_from_file(filename="installed_packages.txt"):
    packages = []
    with open(filename) as f:
        lines = f.readlines()
        # Skip the header lines (first 2 lines)
        for line in lines[2:]:
            # Each line: package_name version
            if line.strip():
                package_name = line.split()[0]
                packages.append(package_name)
    return packages

def upgrade_packages(packages):
    for package in packages:
        print(f"Upgrading {package}...")
        subprocess.run(["pip", "install", "--upgrade", package])

if __name__ == "__main__":
    file_name = "installed_packages.txt"
    save_pip_list(file_name)
    packages = get_packages_from_file(file_name)
    upgrade_packages(packages)
