# Tema L39 Python
# Folosind un arbore binar de cautare implementati o clasa IndexFisier care primeste in constructor un
# nume de fisier. Clasa citeste fisierul (contine doar litere si spatii) si construieste un arbore binar de
# cautare cu cuvintele din fisier. Clasa defineste o singura metoda publica numita “contine” care
# returneaza True sau False in functie de existenta in textul din fisier a unui cuvant primit ca parametru.
# Nota: In Python textele/stringurile (cuvintele) se pot compara tinand cont de ordinea alfabetica a
# literelor folosind aceiasi operator ca in cazul cifrelor (>,<,etc)
# Bonus: Implementati clasa astfel incat obiectul obtinut sa poata permite utilizarea operatorului “in”
# astfel:
# print(“mere” in IndexFisier(“nume_fisier.txt”)) # va afisa True sau False in functie de continutul fisierului

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class IndexFisier:
    def __init__(self, nume_fisier):
        self.root = None
        with open(nume_fisier, 'r') as file:
            content = file.read()
            words = content.split()
            for word in words:
                self.root = self._insert(self.root, word)

    def _insert(self, node, word):
        if node is None:
            return TreeNode(word)
        if word < node.value:
            node.left = self._insert(node.left, word)
        elif word > node.value:
            node.right = self._insert(node.right, word)
        return node

    def contine(self, cuvant):
        return self._search(self.root, cuvant)

    def _search(self, node, cuvant):
        if node is None:
            return False
        if cuvant == node.value:
            return True
        elif cuvant < node.value:
            return self._search(node.left, cuvant)
        else:
            return self._search(node.right, cuvant)

    def __contains__(self, cuvant):
        return self.contine(cuvant)

# Exemplu de utilizare:
index = IndexFisier("nume_fisier.txt")
print("mere" in index)
