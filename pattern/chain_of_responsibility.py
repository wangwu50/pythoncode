import abc


# 责任链模式,仿照java的filter设计
class Filter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_filter(self, request, response, chain):
        pass


class Chain:
    filter_list = []
    currentPosition = 0

    def do_filter(self, request, response):
        if self.currentPosition == len(self.filter_list):
            print(request, response)
            return
        self.currentPosition += 1
        next_filter = self.filter_list[self.currentPosition - 1]
        next_filter.do_filter(request, response, self)

    def add_filter(self, f: Filter):
        self.filter_list.append(f)


class HtmlFilter(Filter):
    def do_filter(self, request, response, filter_chain):
        print('html filter start!')
        filter_chain.do_filter(request, response)
        print('html filter end!')


class TextFilter(Filter):
    def do_filter(self, request, response, filter_chain):
        print('text filter start!')
        filter_chain.do_filter(request, response)
        print('text filter end!')


class Filter2(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_next(self, http_method, chain2):
        pass


class Chain2:
    filter_list = []
    current_position = 0

    def do_next(self, method):
        if self.current_position == len(self.filter_list):
            method()
            return
        self.current_position += 1
        next_filter = self.filter_list[self.current_position - 1]
        next_filter.do_next(method, self)

    def add_filter(self, f: Filter2):
        self.filter_list.append(f)


class HtmlFilter2(Filter2):
    def do_next(self, http_method, chain2):
        print('html filter start!')
        chain2.do_next(http_method)
        print('html filter end!')


if __name__ == '__main__':
    chain = Chain2()
    html_f = HtmlFilter2()
    chain.add_filter(html_f)


    def print_hello():
        print('hello world')


    chain.do_next(print_hello)
