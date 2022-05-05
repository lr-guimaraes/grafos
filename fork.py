'''Leandro Ricardo Guimarães
    Gabrielle Batista
    Javier '''

from random import randint

class fork:
    def __init__(self):
        self.element[20][20] # Create a table with 20 vertex
        self.bool[20][20] #Checks the amount of the edges
        self.rand #gambiarra number random

        # Used to edges
        self.data
        self.next_data = None

    def random(self):
        self.rand = randint(1,1000)

    def createVertex(self):
        for i in range(20):
            for j in range(20):
                self.element[i][j] = self.rand

#a qnt de adjacencia é aleatória
#pode definir um ponto inicial

    def createEdge(self):
        test1 = True
        test2 = True

        rand1 = randint(0,20)
        rand2 = randint(0,20)

        while (test1 == True):
            if (self.bool[rand1][rand2] < 3): #create edge in vertex
                self.data = self.element[rand1][rand2] 
               
                rand3 = randint(0,20)
                rand4 = randint(0,20)

                if(self.bool[rand3][rand4] < 3): #create edge in vertex
                    self.next_data = self.element[rand3][rand4]
                    self.bool[rand1][rand2] += 1
                    self.bool[rand3][rand4] += 1
                else:
                    test2 = False
            else:
                test1 = False


    def newVertex(self):
         self.element.append(self.random())
         self.bool.append(0)


    '''def newEdge(self):
        if test'''
    def Print(self):
        for i in range(20):
            for j in range(20):
                print()

def main():

    fork.createVertex()
    fork.createEdge()

    while True:

        vertex = input("Want add new Vertex {Y/N}:")
        if (vertex.isupper() == "Y"):
            fork.newVertex()
        else:
            False

        '''edge = input("Want add new edge {Y/N}:")
            if (edge.isupper() == "Y"):
            fork.newEdege()
        else:
            False
        '''
        print(fork.fork())

if __name__ == '__main__':
    main()
