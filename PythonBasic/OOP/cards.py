import random


class CardDeck:
    # ** Опишите атрибут класса __slots__
    def __init__(self):
        self.__cards = []
        self.__suites = {'Hearts', 'Diamonds', 'Clubs', 'Spades'}
        self.__values = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}

    # ** Определение строкового представления объекта
    def __repr__(self):
        # Используйте ', '.join(), также map(str, self.cards) либо генератор
        pass

    # Определение метода индексации
    def __getitem__(self, index):
        try:
            return self.cards[index]
        except (IndexError, ValueError, TypeError) as e:
            print(e)

    # Определение проверки длины колоды карт
    def __len__(self):
        return len(self.cards)

    # ** Определение проверки на наличие карты в колоде
    def __contains__(self, item):
        # Обойдите элементы свойства cards, проверьте их масть и значение        
        pass

    # ** Взять верхнюю карту из колоды
    def __withdraw_card_from_top(self):
        pass

    # ** Взять набор карт сверху из колоды
    def __withdraw_card_set(self, count):
        try:
            if count > len(self):
                raise IndexError('the deck hasn\'t so much cards')
            elif count < 1:
                raise IndexError('card set length must be at least 1')
        except IndexError as e:
            print(e)
        else:
            # ** Добавьте карты с помощью метода self.__withdraw_card_from_top()
            # можно использовать генератор списка
            card_set = []
            return card_set
    
    # Публичный метод-интерфейс для запуска скрытых методов
    def withdraw_card(self, value=None):
        if type(value) is int:
            self.__withdraw_card_set(value)
        elif value is not None:
            print('Please enter a number of play cards')
        else:
            self.__withdraw_card_from_top()

    # ** Перетасовать колоду карт
    def shuffle_deck(self):
        # random.shuffle()
        pass

    # ** Определите сеттер:
    @property
    def cards(self):
        return self.__cards

    # ** Определите только геттеры:
    @property
    def suites(self):
        pass

    @property
    def values(self):
        pass


class Card(CardDeck):
    # ** Опишите атрибут класса __slots__
    def __init__(self, **kwargs):
        try:
            self.__card_deck = kwargs['deck']
            self._suit = kwargs['suit']
            self._value = str(kwargs['value'])
        except KeyError:
            print('Please enter suit, value and deck')
        else:
            # ** Проверки на валидность созданной карты
            try:
                # Является ли объект колоды карт колодой карт для данной игры?
                if not isinstance(self.card_deck, self.__class__.__bases__[0]):
                    raise TypeError('this is not a correct card deck')
                # ** Допустима ли указанная масть для указанной колоды карт?
                # ** Допустимо ли указанное значение для указанной колоды карт?
                # ** Есть ли уже такая карта в указанной колоде карт?
            except (ValueError, TypeError) as e:
                print(e)
            else:
                # Добавление валидной карты в колоду карт
                self.card_deck.cards = self

    # ** Определение строкового представления объекта
    def __repr__(self):
        return ''

    # ** Определение операции равенства двух карт
    def __eq__(self, value):
        pass

    # ** Определение длины объекта карты
    def __len__(self):
        return 1

    # Определение проверки на масть и значение карты
    def __contains__(self, item):
        return any((self.value == item, self.suit == item))

    # ** Взять указанную карту из колоды карт
    def withdraw_card(self, value=None):
        pass
    
    # ** Перенаправление на метод экземпляра колоды карт
    def shuffle_deck(self):
        pass

    # Определите только геттер:
    @property
    def card_deck(self):
        return None

    # Определите геттеры, сеттеры и делитеры:
    @property
    def suit(self):
        return None

    @property
    def value(self):
        return None
