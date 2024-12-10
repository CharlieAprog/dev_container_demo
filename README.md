# Python Dev Container Demo

This project demonstrates the use of Docker dev containers with Python, showcasing easy dependency management using pipenv. It includes a simple data analysis module with various popular Python libraries.

## Features
- Docker dev container configuration
- Dependency management with pipenv
- Example data analysis module using pandas, numpy, matplotlib, and scikit-learn
- Unit tests with pytest
- Code formatting with black
- Linting with flake8

## Dependencies
The project includes the following main dependencies:
- pandas: Data manipulation and analysis
- numpy: Numerical computing
- matplotlib: Data visualization
- seaborn: Statistical data visualization
- scikit-learn: Machine learning tools

Development dependencies:
- pytest: Testing framework
- black: Code formatter
- flake8: Linter

## Prerequisites
- Docker Desktop installed and running
- Your preferred IDE (VS Code, PyCharm Professional, or IntelliJ IDEA Ultimate)
- Git (optional, for version control)

## Setup and Running Instructions

### Command Line Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd dev-container-demo
   ```

2. Build and start the dev container:
   ```bash
   docker build -f .devcontainer/Dockerfile -t python-dev-demo .
   docker run -it --rm -v "$(pwd):/workspace" python-dev-demo bash
   ```

3. Inside the container, install dependencies:
   ```bash
   pipenv install --dev
   ```

4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

### Visual Studio Code Setup
1. Install the "Remote - Containers" extension in VS Code
2. Open the project folder in VS Code
3. When prompted, click "Reopen in Container" or:
   - Press F1 (or Cmd/Ctrl + Shift + P)
   - Type "Remote-Containers: Reopen in Container"
   - Press Enter
4. VS Code will automatically:
   - Build the dev container
   - Install dependencies
   - Configure the Python environment
   - Install recommended extensions

### PyCharm Professional Setup
1. Open the project in PyCharm Professional
2. Go to File → Settings → Build, Execution, Deployment → Docker
   - Click '+' to add Docker configuration
   - Test connection to ensure Docker is properly configured
3. Right-click on the project in the Project Explorer
4. Select "New" → "Docker DevContainer"
5. Choose "From Existing Configuration Files"
6. Select the `.devcontainer` folder
7. Click "OK" to build and start the dev container
8. PyCharm will index the project and set up the Python interpreter

### IntelliJ IDEA Ultimate Setup
1. Install the "Python" and "Docker" plugins if not already installed
2. Open the project in IntelliJ IDEA
3. Go to File → Settings → Build, Execution, Deployment → Docker
   - Configure Docker connection if not already set up
4. Right-click on the project in the Project Explorer
5. Select "Dev Containers" → "Open in Dev Container"
6. Select the `.devcontainer` configuration
7. Wait for the container to build and start

## Verifying the Setup
Regardless of your chosen environment, you can verify the setup by:

1. Opening a terminal in your dev container

2. Verify you're in a Linux environment:
   ```bash
   # Show Linux distribution and version
   cat /etc/os-release
   
   # Show Linux kernel version
   uname -a
   
   # Show CPU information
   cat /proc/cpuinfo
   
   # Show memory information
   free -h
   
   # Show disk space
   df -h
   ```
   These commands are Linux-specific and will only work inside the container, not on your Mac host system!

3. Running the tests:
   ```bash
   pipenv run pytest
   ```
   
## Troubleshooting
- If the container fails to build, ensure Docker Desktop is running
- For VS Code, ensure the Remote - Containers extension is installed
- For PyCharm/IntelliJ, verify Docker integration is properly configured
- Check Docker daemon connectivity with `docker info`
- Verify the .devcontainer configuration files are in the correct location
- For volume mounting issues, ensure proper permissions on the project directory

## Additional Notes
- The dev container configuration can be customized in `.devcontainer/devcontainer.json`
- Additional VS Code extensions can be added to the `extensions` array in `devcontainer.json`
- Python dependencies can be managed through the Pipfile
- The container configuration is compatible with GitHub Codespaces

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.