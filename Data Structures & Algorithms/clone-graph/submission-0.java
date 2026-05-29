class Solution {
    Node[] cloned = new Node[101];

    public Node cloneGraph(Node node) {
        if (node == null) return null;

        if (cloned[node.val] != null) {
            return cloned[node.val];
        }

        Node copy = new Node(node.val);
        cloned[node.val] = copy;

        for (Node neighbor : node.neighbors) {
            copy.neighbors.add(cloneGraph(neighbor));
        }

        return copy;
    }
}