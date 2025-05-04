from abc import ABC, abstractmethod

class TCPIPlayer(ABC):
    @abstractmethod
    def layer_info(self):
        pass

class ApplicationLayer(TCPIPlayer):
    def layer_info(self):
        return "Application Layer, Presentation Layer, Session Layer merupakan layer 4."

class TransportLayer(TCPIPlayer):
    def layer_info(self):
        return "Transport Layer merupakan layer 3."

class NetworkLayer(TCPIPlayer):
    def layer_info(self):
        return "Network Layer merupakan layer 2."

class NetworkAccessLayer(TCPIPlayer):
    def layer_info(self):
        return "Data Link Layer, Phisical Layer merupakan layer 1."

class TCPIPlayerFactory:
    @staticmethod
    def create_layer(layer_type):
        if layer_type == "application":
            return ApplicationLayer()
        elif layer_type == "transport":
            return TransportLayer()
        elif layer_type == "network":
            return NetworkLayer()
        elif layer_type == "networkaccess":
            return NetworkAccessLayer()
        else:
            raise ValueError(f"Unknown OSI layer type: {layer_type}")

if __name__ == "__main__":
    layer_type = input("Masukkan TCP/IP Layer (application/transport/network/networkaccess): ").strip().lower()
    
    osi_layer = TCPIPlayerFactory.create_layer(layer_type)
    print(osi_layer.layer_info())