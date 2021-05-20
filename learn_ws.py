class KnnWs:
    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.y_test = None
        print('thanks for using knn_ws')

    def train(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        print("train", self.x_train, self.y_train)

    def predict(self, y_test):
        self.y_test = y_test
        print("predict", self.y_test)

    @staticmethod
    def no_use():
        print("you can do nothing")


class BayesWs:
    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.y_test = None
        print('thanks for using bayes_ws')

    def train(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        print("train", self.x_train, self.y_train)

    def predict(self, y_test):
        self.y_test = y_test
        print("predict", self.y_test)
