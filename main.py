# Definition for singly-linked list
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to remove duplicates
def removeDuplicates(head):
    # Check if the linked list is empty
    if head is None:
        return head

    # Set the current node to the head of the list
    current_node = head

    # Loop through the linked list and compare each node to the subsequent node
    while current_node is not None:
        # Set the subsequent node to the node after the current node
        subsequent_node = current_node.next

        # Store the reference of the current node
        previous_node = current_node

        # Loop through subsequent nodes and compare the value to the current node
        while subsequent_node is not None:
            # If a duplicate is found
            if current_node.val == subsequent_node.val:
                # Store the reference of the subsequent node
                temp = subsequent_node

                # Point the previous node to the node after the duplicate
                previous_node.next = temp.next

                # Move the subsequent node one position forward
                subsequent_node = temp.next

            # If no duplicate is found, move the previous and subsequent node one position forward
            else:
                previous_node = subsequent_node
                subsequent_node = subsequent_node.next

        # Set the current node to the node one position ahead
        current_node = current_node.next

    # Return the reference to the head of the updated linked list
    return head