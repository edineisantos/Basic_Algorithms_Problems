## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for part in parts:
            if part not in node.children:
                node.children[part] = RouteTrieNode()
            node = node.children[part]
        node.handler = handler

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for part in parts:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, part):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode()


## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler  
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts = self.split_path(path)
        self.route_trie.insert(parts, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        if path is None:
            path = "/"
        parts = self.split_path(path)
        handler = self.route_trie.find(parts)
        if handler:
            return handler
        else:
            # return the "not found" handler if you added one
            return self.not_found_handler
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        if path is None or path == "":
            return []
        parts = path.strip("/").split("/")
        # Remove empty parts to handle trailing slashes
        return [part for part in parts if part]
    
## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print("\n")

# Test Case 1: Normal input
print("Test Case 1: Normal input")
print(router.lookup("/home/about"))
# Expected Output: 'about handler'

# Test Case 2: Empty string as input
print("Test Case 2: Empty string as input")
print(router.lookup(""))
# Expected Output: 'root handler'

# Test Case 3: None as input
print("Test Case 3: None as input")
print(router.lookup(None))
# Expected Output: 'root handler'

