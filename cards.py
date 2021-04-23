class MainCards:
    def __init__(self, img, name, link):
        self.img, self.name, self.link = img, name, link
        self.lenght = len(CARDS[self.link])


class CardOfLesson:
    def __init__(self, color, source, link, name):
        self.color, self.source, self.link, self.name = color, source, link, name


CARDS = {'math': (
    CardOfLesson('#DC8754', '123-numbers.svg', '/math/sequences',
                 'Последовательности'),
    CardOfLesson('#A858D6', 'cone.svg', '/math/stereometry', 'Стереометрия')),
    'physics': (
        CardOfLesson('#EB6A7D', 'wave.svg', '/physics/elec',
                     'Электромагнитные волны'),
        CardOfLesson('#00A8AB', 'atom.svg', '/physics/atomic-structure',
                     'Строение атома')),
    'computers': (CardOfLesson('#71D780', 'binary.svg', '/computers/binary',
                               'Двоичная система'),
                  CardOfLesson('#5660FF', 'processor.svg', '/computers/cpu', 'Процессор'))
}
