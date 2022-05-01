import cv2
import numpy as np
class MinimumSpanningTree():
    def __init__(self, v = 5 , graph = [], noEdge = 0, total = 0,result = []):
        self.v = v
        self.total = total 
        self.graph = graph 
        self.noEdge = noEdge
        self.result = result
    
    def openImg(self,rep, img):
        img = cv2.imread(img, 1)
        cv2.imshow(rep, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def openVideo(self, vid,fra):
        cap = cv2.VideoCapture(vid)
     
        if (cap.isOpened()== False): 
            print("Error opening video  file")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow(fra, frame)
                if cv2.waitKey(25) & 0xFF == ord('q') :
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    def prims(self):
        inf = 1111111
        # grafları komşuluk matrisiyle temsil ettik
        self.graph =[[0, 9, 57, 0, 0], 
                    [9, 0, 59, 91, 24], 
                    [57, 59, 0, 15, 66], 
                    [0, 91, 15, 0, 13], 
                    [0, 24, 66, 13, 0]] 

        selectNode = [False for node in range(self.v)]
        self.result = [[0 for column in range(self.v)]
                    for row in range(self.v)]
    
        while ( False in selectNode ):
            min = inf
            start = 0
            end = 0
            for i in range(self.v):
                if selectNode[i]:
                    for j in range(self.v):
                     
                        if ((not selectNode[j]) and self.graph[i][j]>0 ):
                            if min > self.graph[i][j]:
                                min = self.graph[i][j]
                                start = i
                                end = j 
            
            selectNode[end] = True
            self.result[start][end] = min
            if min == inf:
                self.result[start][end] = 0
            
            self.noEdge += 1
            self.result[end][start] = self.result[start][end]
            self.total += self.result[start][end]
        for i in range(len(self.result)):
            for j in range(0+i, len(self.result)):
                if self.result[i][j] != 0:
                    print(" {} - {} vertex arası ağırlık: {} ".format(i,j,self.result[i][j]) )
                    
        print("Kenarların ağırlıkları toplamı:",format(self.total))

    # Kruskal Algorithms Started
    
    def addEdgeToKruskal(self, node1, node2, weight):
        self.graph.append([node1, node2, weight])
    
    def findSubtree(self, parent, i):
        if parent[i] == i :
            return i 
        return self.findSubtree(parent, parent[i]) # recursive function
        
    def connectSubtree(self, parent, sizeOfSubtree, x, y):
        xroot = self.findSubtree(parent, x)
        yroot = self.findSubtree(parent, y)
        if sizeOfSubtree[xroot] < sizeOfSubtree[yroot] :
            parent[xroot] = yroot
        elif sizeOfSubtree [xroot] > sizeOfSubtree[yroot] :
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            sizeOfSubtree[xroot] += 1
    def kruskal(self):
        self.total = 0
        self.v = 9
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2]) # kenarları ağırlıklarına göre sıraladık
        parent = []
        sizeOfSubtree = []
        for node in range(self.v):
            parent.append(node)
            sizeOfSubtree.append(0)

        while e < (self.v - 1):
            node1, node2, weight = self.graph[i]
            i += 1 
            x = self.findSubtree(parent, node1)
            y = self.findSubtree(parent, node2)

            if x != y:
                e += 1
                self.result.append([node1, node2, weight])
                self.connectSubtree(parent, sizeOfSubtree, x, y )
        for node1, node2, weight in self.result:
            print(' {} - {} vertex arası ağırlık: {} '.format(node1,node2,weight))
            self.total += weight
        print("Kenarların ağırlıkları toplamı:" ,format(self.total))
    