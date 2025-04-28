from abc import ABC, abstractmethod

# Abstract Product
class OSILayer(ABC):
    @abstractmethod
    def get_layer_info(self):
        pass

# Concrete Products
class ApplicationLayer(OSILayer):
    def get_layer_info(self):
        return "This is the Application Layer (Layer 7)."

class TransportLayer(OSILayer):
    def get_layer_info(self):
        return "This is the Transport Layer (Layer 4)."

class NetworkLayer(OSILayer):
    def get_layer_info(self):
        return "This is the Network Layer (Layer 3)."

class DataLinkLayer(OSILayer):
    def get_layer_info(self):
        return "This is the Data Link Layer (Layer 2)."

class PhysicalLayer(OSILayer):
    def get_layer_info(self):
        return "This is the Physical Layer (Layer 1)."

# Factory Class
class OSILayerFactory:
    @staticmethod
    def create_layer(layer_type):
        if layer_type == "application":
            return ApplicationLayer()
        elif layer_type == "transport":
            return TransportLayer()
        elif layer_type == "network":
            return NetworkLayer()
        elif layer_type == "data_link":
            return DataLinkLayer()
        elif layer_type == "physical":
            return PhysicalLayer()
        else:
            raise ValueError(f"Unknown OSI layer type: {layer_type}")

# Main Program
if __name__ == "__main__":
    layer_type = input("Enter the OSI layer you want to create (application/transport/network/data_link/physical): ").strip().lower()
    
    osi_layer = OSILayerFactory.create_layer(layer_type)
    print(osi_layer.get_layer_info())