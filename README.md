# Update Libs

    A simple Python script to list all installed pip packages and upgrade them to their latest versions.

    ## Usage

    1. Clone or download this repository.
    2. Run the script:

        ```
        python update_libs.py
        ```

    3. The script will:
        - Save the list of installed packages to `installed_packages.txt`.
        - Read the package names from the file.
        - Upgrade each package using pip.

    ## Requirements

    - Python 3.x
    - pip

    ## Notes

    - Run the script in an environment where you have permission to upgrade packages.
    - Consider using a virtual environment to avoid affecting system-wide packages.

    ## Disclaimer

    Use at your own risk. Upgrading all packages may cause compatibility issues in some projects.