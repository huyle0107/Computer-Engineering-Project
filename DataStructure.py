def print_node_details(node):
    current_node = node
    while current_node:
        print(f"Node ID: {current_node.ID}")
        current_sensor = current_node.sensor
        while current_sensor:
            print(f"  Sensor ID: {current_sensor.ID}, Sensor Data: {current_sensor.current_data}, Sensor buffer: {current_sensor.buffer}")
            current_sensor = current_sensor.next
        current_node = current_node.node  # Move to the next node

class NodeSensor:
    def __init__(self, sensorID, data):
        self.ID = sensorID
        self.current_data = data 
        self.size = 0
        self.buffer = [0] * 10
        self.next = None
        
    def setup_buffer(self,data):
        if self.size < 10:
            self.buffer[self.size] = data
            self.size += 1
        if self.size == 10:
            # Calculate mean
            mean = sum(self.buffer) / self.size
            # Calculate varriance
            variance = sum((x - mean) ** 2 for x in self.buffer) / self.size
            self.size = 0
            if variance < 5:
                self.current_data = mean
        return self.current_data


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
            return  data

        # Find the corresponding node using nodeID
        current_node = root_node
        while current_node and current_node.ID != nodeID:
            if not current_node.node:
                # Node doesn't exist, create a new node
                current_node.node = Node()
                current_node.node.ID = nodeID
                current_node.node.sensor = NodeSensor(sensorID, data)
                return  data
            current_node = current_node.node
        
        if current_node:
            # Check if the node already has a sensor with the same ID
            current_sensor = current_node.sensor
            while current_sensor:
                if current_sensor.ID == sensorID:
                    # Sensor with the same ID found, update its data
                    return  current_sensor.setup_buffer(data)

                if not current_sensor.next:
                    break  # Reached the last sensor in the list
                current_sensor = current_sensor.next

            # No existing sensor with the same ID, create a new one
            current_sensor.next = NodeSensor(sensorID, data)
            return data

root_node = Node()
