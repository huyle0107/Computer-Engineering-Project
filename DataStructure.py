def print_node_details(node):
    current_node = node
    while current_node:
        print(f"Node ID: {current_node.ID}")
        current_sensor = current_node.sensor
        while current_sensor:
            print(f"  Sensor ID: {current_sensor.ID}, Sensor Data: {current_sensor.sensor_data}")
            current_sensor = current_sensor.next
        current_node = current_node.node  # Move to the next node

class NodeSensor:
    def __init__(self, sensorID, data):
        self.ID = sensorID
        self.sensor_data = data
        self.next = None

class Node:
    def __init__(self):
        self.ID = None
        self.sensor = None  # This is a NodeSensor
        self.node = None    # This is a Node

    def updateNode(self, nodeID, sensorID, data):
        global root_node  # Make sure root_node is used from outside the function

        if not root_node:
            root_node = Node()
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
                    current_sensor.sensor_data = data
                    return

                if not current_sensor.next:
                    break  # Reached the last sensor in the list
                current_sensor = current_sensor.next

            # No existing sensor with the same ID, create a new one
            current_sensor.next = NodeSensor(sensorID, data)

        

# Example usage
root_node = None

while(1):
    nodeID = int(input("Nhập Node ID: "))
    sensorID = int(input("Nhập Sensor ID: "))
    data = int(input("Nhập Sensor Data: "))
    if not root_node:
        root_node = Node()
        root_node.ID = nodeID
        root_node.sensor = NodeSensor(sensorID, data)
    else:
        root_node.updateNode(nodeID,sensorID,data)
    print_node_details(root_node)


