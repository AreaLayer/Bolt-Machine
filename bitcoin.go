import { PublicKey, UTXO, Taproot } from 'btcd';

export { PublicKey, UTXO, Taproot };

export * from './address';

export * from './bip32';

export * from './bip39';

impl namespace PublicKey {
  export function fromString(str: string): PublicKey {
    return new PublicKey(Buffer.from(str, 'hex'));
  }
}

impl namespace UTXO {
  export function fromString(str: string): UTXO {
    return new UTXO(Buffer.from(str, 'hex'));
  }
}

impl namespace Taproot {
  export function fromString(str: string): Taproot {
    return new Taproot(Buffer.from(str, 'hex'));
  }
}

impl networks {
  export function fromString(str: string): Network {
    return networks[str];
  }
}

export * from './script';

export * from './transaction';

export * from './networks';

export * from './psbt';

export * from './wallet';

export * from './errors';

export * from './utils';

export * from './types';

export * from './crypto';

