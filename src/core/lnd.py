from protos import lightning_pb2 as ln
from protos import lightning_pb2_grpc as lnrpc

import grpc
import os
import codecs
import binascii

# Due to updated ECDSA generated tls.cert we need to let gRPC know that we need
# to use that cipher suite; otherwise, there will be a handshake error when we
# communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

class LightningNode(object):
    """
    Abstract base class for a Lightning node.
    """

    def pay_invoice(self, invoice):
        raise NotImplementedError("This method should be implemented by subclasses")


class LndNode(LightningNode):
    """
    Class to interact with an LND node over gRPC.
    """

    def __init__(self, cert_path, macaroon_path, host='localhost', port='10009'):
        self.cert_path = cert_path
        self.macaroon_path = macaroon_path
        self.host = host
        self.port = port
        self._grpc_conn = None

        # Load TLS certificate
        with open(os.path.expanduser(self.cert_path), 'rb') as f:
            cert_bytes = f.read()
        self._cert_creds = grpc.ssl_channel_credentials(cert_bytes)

        # Load macaroon
        with open(os.path.expanduser(self.macaroon_path), 'rb') as f:
            macaroon_bytes = f.read()
        self._macaroon = codecs.encode(macaroon_bytes, 'hex').decode('utf-8')

        # Create metadata callback for macaroon
        def metadata_callback(context, callback):
            callback([('macaroon', self._macaroon)], None)

        # Build metadata credentials
        auth_creds = grpc.metadata_call_credentials(metadata_callback)

        # Combine the cert credentials and the macaroon auth credentials
        combined_creds = grpc.composite_channel_credentials(self._cert_creds, auth_creds)

        # Create a secure channel with combined credentials
        channel = grpc.secure_channel(f'{self.host}:{self.port}', combined_creds)

        # Initialize the gRPC connection
        self._grpc_conn = lnrpc.LightningStub(channel)

    def pay_invoice(self, invoice, amt=None):
        """
        Pays a lightning invoice.

        Args:
            invoice (str): The lightning invoice to be paid.
            amt (int): The amount to pay (optional, for partial payments).

        Returns:
            str: The payment preimage in hexadecimal format.
        """
        pay_resp = self._grpc_conn.SendPaymentSync(
            ln.SendRequest(payment_request=invoice, amt=amt)
        )
        pre_image = binascii.hexlify(pay_resp.payment_preimage).decode('utf-8')
        return pre_image

    def send_payment(self, invoice):
        """
        Sends a payment for the given invoice.

        Args:
            invoice (str): The lightning invoice to be paid.

        Returns:
            ln.SendResponse: The response from the payment request.
        """
        return self._grpc_conn.SendPaymentSync(
            ln.SendRequest(payment_request=invoice)
        )

    def decode_invoice(self, invoice):
        """
        Decodes a lightning invoice.

        Args:
            invoice (str): The lightning invoice to decode.

        Returns:
            ln.PayReq: The decoded invoice information.
        """
        req = ln.PayReqString(pay_req=invoice)
        decode_resp = self._grpc_conn.DecodePayReq(req)
        return decode_resp

    def channel_balance(self):
        """
        Retrieves the channel balance.

        Returns:
            ln.ChannelBalanceResponse: The channel balance information.
        """
        return self._grpc_conn.ChannelBalance(ln.ChannelBalanceRequest())

    def wallet_balance(self):
        """
        Retrieves the wallet balance.

        Returns:
            ln.WalletBalanceResponse: The wallet balance information.
        """
        return self._grpc_conn.WalletBalance(ln.WalletBalanceRequest())

    def get_info(self):
        """
        Retrieves information about the LND node.

        Returns:
            ln.GetInfoResponse: The node's information.
        """
        return self._grpc_conn.GetInfo(ln.GetInfoRequest())
