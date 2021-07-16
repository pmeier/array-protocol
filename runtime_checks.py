from consumer import VendoredArrayProtocol
from provider import ArrayImplementation


assert isinstance(ArrayImplementation(), VendoredArrayProtocol)
