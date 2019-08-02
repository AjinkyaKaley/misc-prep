from collections import defaultdict
from enum import Enum
class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda:None)
        self.method = None
        self.isEnd = False


class Constanst(Enum):
    NOT_FOUND = "404"
    ROOT = "/"
    REGEX = "X"
    DELIMITER = "/"
class UrlRouteMatching:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, path, method):
        crawler = self.root
        if path == Constanst.ROOT.value:
            crawler.method = method
            crawler.isEnd = True
            return
        actions = path.split(Constanst.DELIMITER.value)
        for action in actions:
            if action == '' or action == Constanst.ROOT.value:
                continue
            if not action in crawler.children:
                crawler.children[action] = TrieNode()
            crawler = crawler.children[action]
        crawler.method = method
        crawler.isEnd = True

    def dispatchMethod(self, route, crawler):
        if not crawler:
            return Constanst.NOT_FOUND.value
        if route == []:
            return crawler.method if crawler.method else Constanst.NOT_FOUND.value
        path = route[0]
        method = self.dispatchMethod(route[1:], crawler.children[path])
        if Constanst.REGEX.value in crawler.children and method == Constanst.NOT_FOUND.value:
            method = self.dispatchMethod(
                route[1:], crawler.children[Constanst.REGEX.value])
        return method

def main():
    urlRouteMatching = UrlRouteMatching()
    pathPattern =[
        "/ rootEndpoint",
        "/v1/user userRootEndpointV1",
        "/v2/user userRootEndpointV2",
        "/v1/user/friends userFriendsEndpoint",
        "/v1/user/lists userListsEndpoint",
        "/v2/user/X userEndpoint",
        "/v2/user/X/friends userFriendsEndpoint",
        "/v2/user/X/lists userListsEndpoint",
        "/v2/user/X/lists/X userListIdEndpoint",
        "/v3/friends userFriendsEndpoint",
        "/v3/X/lists userListsEndpoint",
        "/settings settingsEndpoint"
    ]

    for line in pathPattern:
        pathName, method = map(str, line.strip().split(" "))
        urlRouteMatching.insert(pathName, method)

    urlRoutes =[
        # "home",
        # "home/about"
        "/user",
        "/user/friends",
        "/user/123",
        "/user/123/friends",
        "/user/123/friends/zzz",
        "/user/friends/friends",
        "/",
        "/abc/lists",
        "/settings",
        "/123/bbb"
    ]
    for line in urlRoutes:
        if line == Constanst.ROOT.value:
            print(urlRouteMatching.root.method)
        else:
            if line.startswith(Constanst.ROOT.value):
                line = line[len(Constanst.DELIMITER.value):]
            line = line.split(Constanst.DELIMITER.value)
            # line.insert(0, "/")
            print(urlRouteMatching.dispatchMethod(line, urlRouteMatching.root))
if __name__ == "__main__":
    main()
