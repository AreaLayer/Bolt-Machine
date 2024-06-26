import { CLI } from './cli';
import { CLI_VERSION } from './version';

CLI.run(CLI_VERSION);

class CLI {
	constructor() {
		console.log('Hello World');
	}
	run(version) {
		console.log('Hello World');
	}

}
class CLI_VERSION {
	constructor() {
		console.log('Hello World');
	}

	run(version) {
		console.log('Hello World');
	}

	get_version() {
		return '1.0.0';
		console.log('Hello World');
	}
