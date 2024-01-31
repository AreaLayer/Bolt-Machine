# Bolt Machine

## Overview
This Go program demonstrates an algorithm for managing channels in a Lightning Network. It uses various modules to perform actions such as opening, closing, replacing channels, and finding better inbound liquidity. The program incorporates APIs from OpenAI and Aperture for enhanced functionality.

## Prerequisites

To run this program, you need to have the following prerequisites installed:
- Go programming language (21.6)
- OpenAI API key
- LND (Lightning Network Daemon) configured and running - v0.17.3-beta

## Installation
1. Clone the repository:
git clone https://github.com/your-username/your-repo.git

2. Change into the project directory:
cd your-repo


3. Install the necessary Go packages:
go get -u github.com/openai/openai-go
go get -u github.com/aperture-io/api-go
go get -u github.com/lightningnetwork/lnd


## Configuration
1. Set up OpenAI API:
- Obtain an OpenAI API key from the OpenAI website.
- Replace `"YOUR_OPENAI_API_KEY"` in the code with your actual API key.

2. Set up Aperture API:
- Obtain an Aperture API token from the Aperture website.
- Replace `"YOUR_APERTURE_API_TOKEN"` in the code with your actual API token.

3. Set up LND:
- Ensure LND is properly installed and running.
- Configure the LND connection details (host, port, TLS certificate) in the code.

## Usage
1. Open a terminal and navigate to the project directory.

2. Build the Go program:
go build

3. Run the program:
./your-repo


4. The program will simulate the AI performing actions based on a random selection. The available actions are:
- 0: OpenChannel
- 1: CloseChannel
- 2: ReplaceChannel
- 3: FindBetterInboundLiquidity

## License
This project is licensed under the [MIT License](LICENSE).


