# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class LogicGate(metaclass=ABCMeta):
    """逻辑门"""

    def __init__(self, label):
        self.__label = label
        self.__output = None

    @property
    def label(self):
        """获得逻辑门的标签"""
        return self.__label

    def get_output(self):
        """获得逻辑门的输出"""
        self.__output = self.perform_gate_logic()
        return self.__output

    @abstractmethod
    def set_next_pin(self, source):
        """设置获得输入的引脚"""

    @abstractmethod
    def perform_gate_logic(self):
        """具体的逻辑运算"""


class UnaryGate(LogicGate, metaclass=ABCMeta):
    """一个输入的逻辑门"""

    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        """获得引脚的输入值"""
        if self.pin is None:
            return int(input(f'Enter Pin input for gate {self.label}-->'))
        else:
            return self.pin.from_gate.get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print('Error, No Empty Pin!')


class BinaryGate(LogicGate, metaclass=ABCMeta):
    """两个输入的逻辑门"""

    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        """获得引脚A的输入值"""
        if self.pin_a is None:
            return int(input(f'Enter Pin A input for gate {self.label}-->'))
        else:
            return self.pin_a.from_gate.get_output()

    def get_pin_b(self):
        """获得引脚B的输入值"""
        if self.pin_b is None:
            return int(input(f'Enter Pin B input for gate {self.label}-->'))
        else:
            return self.pin_b.from_gate.get_output()

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            print('Error, No Empty Pin!')


class AndGate(BinaryGate):
    """与门"""

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """或门"""

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    """非门"""

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return 0 if self.get_pin() == 1 else 1


class NAndGate(AndGate):
    """与非门"""

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return int(not super().perform_gate_logic())


class NOrGate(OrGate):
    """或非门"""

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return int(not super().perform_gate_logic())


class XOrGate(BinaryGate):
    """异或门"""

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a != b:
            return 1
        else:
            return 0


class Connector:
    """连接器"""

    def __init__(self, from_gate: LogicGate, to_gate: LogicGate):
        self.__from_gate = from_gate
        self.__to_gate = to_gate
        to_gate.set_next_pin(self)

    @property
    def from_gate(self):
        return self.__from_gate

    @property
    def to_gate(self):
        return self.__to_gate


if __name__ == '__main__':
    ag1 = AndGate('AndGate1')
    ag2 = AndGate('AndGate2')
    og1 = OrGate('OrGate1')
    ng1 = NotGate('NotGate1')
    c1 = Connector(ag1, og1)
    c2 = Connector(ag2, og1)
    c3 = Connector(og1, ng1)
    print(ng1.get_output())

    nag1 = NAndGate('NAndGate1')
    print(nag1.get_output())
    nog1 = NOrGate('NOrGate1')
    print(nog1.get_output())
    xog1 = XOrGate('XOrGate1')
    print(xog1.get_output())
