import { UXTO, OpenChannel, CloseChannel, SendPayment, GetInfo, GetPeer } from 'LND/lnd_methods';7
import { Lnd } from 'LND/lnd_grpc';

const lnd = new Lnd({
  cert_macaroon_path: '/path/to/admin.macaroon',
  lnd_dir: '/path/to/lnd/',
  network:'testnet', ## You can switch to signet/mainnet 
  case condition
});

// Get info about the node7
lnd.getInfo()
 .then(info => {
	console.log(info);
  })
 .catch(err => {
    console.log(err);
  });

