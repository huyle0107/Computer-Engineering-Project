def print_node_details(node):
    current_node = node
    while current_node:
        print(f"Node ID: {current_node.ID}")
        current_sensor = current_node.sensor
        while current_sensor:
            print(f"  Sensor ID: {current_sensor.ID}, Sensor Data: {current_sensor.buffer}")
            current_sensor = current_sensor.next
        current_node = current_node.node  # Move to the next node

class NodeSensor:
    def __init__(self, sensorID, data):
        self.ID = sensorID
        self.receive_data = data
        self.size = 0
        self.buffer = [0] * 10
        self.next = None
        self.setup_buffer()  # Call another function to set up the buffer

    def setup_buffer(self):
        if self.size < 10:
            self.buffer[self.size] = self.receive_data
            self.size += 1
        else:
            for i in range(9):
                self.buffer[i] = self.buffer[i + 1]
            self.buffer[9] = self.receive_data
            # Not check varriance 
        
        

class Node:
    def __init__(self):
        self.ID = None
        self.sensor = None  # This is a NodeSensor
        self.node = None    # This is a Node

    def updateNode(self, nodeID, sensorID, data):
        global root_node  # Make sure root_node is used from outside the function

        if not root_node.ID:
            root_node.ID = nodeID
            root_node.sensor = NodeSensor(sensorID, data)
            return

        # Find the corresponding node using nodeID
        current_node = root_node
        while current_node and current_node.ID != nodeID:
            if not current_node.node:
                # Node doesn't exist, create a new node
                current_node.node = Node()
                current_node.node.ID = nodeID
                current_node.node.sensor = NodeSensor(sensorID, data)
                return
            current_node = current_node.node
        
        if current_node:
            # Check if the node already has a sensor with the same ID
            current_sensor = current_node.sensor
            while current_sensor:
                if current_sensor.ID == sensorID:
                    # Sensor with the same ID found, update its data
                    current_sensor.receive_data = data
                    current_sensor.setup_buffer()
                    return

                if not current_sensor.next:
                    break  # Reached the last sensor in the list
                current_sensor = current_sensor.next

            # No existing sensor with the same ID, create a new one
            current_sensor.next = NodeSensor(sensorID, data)

        

# Example usage
root_node = Node()

while(1):
    nodeID = int(input("Nhập Node ID: "))
    sensorID = int(input("Nhập Sensor ID: "))
    data = int(input("Nhập Sensor Data: "))
    root_node.updateNode(nodeID,sensorID,data)
    print_node_details(root_node)


