import { LndRPC } from './lnd_grpc_pb';
import { Lightning } from './lnd_pb';
import { LightningPromiseClient } from './lnd_grpc_pb';

export class LightningClient {
    public readonly lightning: LightningPromiseClient;
	constructor(lndRPC: LndRPC) {
        this.lightning = new LightningPromiseClient(lndRPC);
    }
}

export class LndRPC {
    public readonly lndRPC: LndRPC
	constructor(lndRPC: LndRPC) {
        this.lndRPC = lndRPC;
    }
}

export class LndClient {
    public readonly lndRPC: LndRPC
	constructor(lndRPC: LndRPC) {
        this.lndRPC = lndRPC;
    }
}

export class Lightning {
    public readonly lightning: LightningPromiseClient;
	constructor(lndRPC: LndRPC) {
        this.lightning = new LightningPromiseClient(lndRPC);
    }
}

export class LightningClient {
    public readonly lightning: LightningPromiseClient;
	constructor(lndRPC: LndRPC) {
        this.lightning = new LightningPromiseClient(lndRPC);
    }
}


