import requests
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod


@dataclass
class Product:
    category: int
    title: str
    price: float
    quantity: int


class AbstractRequest(ABC):
    @abstractmethod
    def get(self, resource, id=None):
        pass

    # @abstractmethod
    # def post(self, resource, data):
    #     pass

    # @abstractmethod
    # def delete(self, resource, id):
    #     pass

    # @abstractmethod
    # def update(self, resource, id, data):
    #     pass


class ProductRequest(AbstractRequest):
    __HOST = 'http://10.117.9.207/'
    __resource = 'product/'

    def get(self, id=None):
        if id is not None:
            return requests.get(self.__HOST + self.__resource + str(id)).json()
        return requests.get(self.__HOST + self.__resource).json()


request = ProductRequest()
product = request.get(4)

# p = asdict(Product(3, 'asdfasdf', '341234', 2))
# print(p)
