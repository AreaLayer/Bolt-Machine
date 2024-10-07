
# Bolt Machine

## Overview
This Python program demonstrates an algorithm for managing channels in a Lightning Network. It uses various modules to perform actions such as opening, closing, replacing channels, and finding better inbound liquidity. The program incorporates APIs from Ollama  for enhanced functionality.

## Prerequisites

To run this program, you need to have the following prerequisites installed:
- Python 3.9+
- Ollama API key
- LND (Lightning Network Daemon) configured and running the latest version
- LND Node and CLN soon

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AreaLayer/Bolt-Machine.git
   ```

2. Change into the project directory:
   ```bash
   cd your-bolt-machine
   ```

3. Install the necessary Python packages:
   ```bash
   pip install ollama 
   pip install lnd-grpc
   ```

## Configuration
1. Set up Ollama API:
   - Obtain an Ollama API key from the Ollama website.
   - Replace `"YOUR_OLLAMA_API_KEY"` in the code with your actual API key.

2. Set up LND:
   - Ensure LND is properly installed and running.
   - Configure the LND connection details (host, port, TLS certificate) in the code.

## Usage
1. Open a terminal and navigate to the project directory.

2. Run the Python program:
   ```bash
   python main.py
   ```

3. The program will simulate the AI performing actions based on a random selection. The available actions are:
   - 0: OpenChannel
   - 1: CloseChannel
   - 2: ReplaceChannel
   - 3: FindBetterInboundLiquidity

## License
This project is licensed under the [MIT License](LICENSE).
