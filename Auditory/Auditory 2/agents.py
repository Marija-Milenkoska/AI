"""Да се дефинира класа за Агент кој ја чува својата позиција
(координати x и y) во некој простор. Да се дефинира метод кој го
означува движењето на агентот во просторот. Потоа да се дефинираат
агенти кои имплементираат специфично движење (лево, десно, горе, долу).
 Извршете 5 движења за секој од агентите и испечатете ја позицијата на
 агентот во секој чекор."""

class Agent:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position: ({self.x}, {self.y})'

    def move(self):
        pass

class leftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1

class rightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self):
        self.x += 1

class upAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self):
        self.y += 1

class downAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self):
        self.y -= 1

if __name__ == '__main__':
    la = leftAgent(3, 4)
    print(la)
    for i in range(5):
        la.move()
        print(f"Step: {i}, {la}")
    ra = rightAgent(-2, 3)
    print(ra)
    for i in range(5):
        ra.move()
        print(f'Step: {i}, {ra}')

    ua = upAgent(-2, -3)
    print(ua)
    for i in range(5):
        ua.move()
        print(f'Step: {i}, {ua}')

    da = downAgent(2, 3)
    print(da)
    for i in range(5):
        da.move()
        print(f'Step: {i}, {da}')
