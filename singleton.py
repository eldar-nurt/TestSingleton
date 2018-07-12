# from selenium import webdriver

#
# class SingletonWebDriver(webdriver):
#     __instance = None
#
#     @staticmethod
#     def inst():
#         if SingletonWebDriver.__instance is None:
#             SingletonWebDriver.__instance = SingletonWebDriver()
#         return SingletonWebDriver.__instance
#
#     # single call check
#     def __init__(self):
#         self = self.webdriver


class Singleton(object):
    _instance = None

    def __new__(*cls, class_, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *cls, **kwargs)
        return class_._instance


# class MyClass(Singleton, BaseClass):
#     pass

