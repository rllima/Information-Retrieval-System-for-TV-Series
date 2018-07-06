import sys
import json as js


class Node:
    def __init__(self):
        self.next = {}
        self.word_marker = False

    def add_item(self, string):
        if len(string) == 0:
            self.word_marker = True
            return

        key = string[0]
        string = string[1:]

        if key in self.next:
            self.next[key].add_item(string)
        
        else:
            node = Node()
            self.next[key] = node
            node.add_item(string)

    def dfs(self, sofar = None):
        if self.next.keys() == []:
            print("MATCH:" +  sofar)
        if self.word_marker == True:
            print("MATCH:" + sofar)
        for key in self.next.keys():
            self.next[key].dfs(sofar+key)
    def search(self,string,sofar =""):
        if len(string) > 0:
            key = string[0]
            string = string[1:]
            if key in self.next:
                sofar = sofar+key
                self.next[key].search(string, sofar)
            else:
                print ("NO MATCH")
        else:
            if self.word_marker == True:
                print("MATCH: " + sofar)
            for key in self.next.keys():
                self.next[key].dfs(sofar+key)
    

if __name__ == '__main__':
        
    with open("auto_complete/title_series.json") as fr: #for cast autocomplete change for 'autocomplete/cast_series.json'
        data = js.load(fr)
    tree = Node()
    for name in data['name_series']:  #In case cast use 'cast_name'
        tree.add_item(name)
    print ("Input:")
    input=input()
    tree.search(input)

    