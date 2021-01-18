class TradeEvent:

    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.symbol = ""
        self.price = 0.0
        self.qty = 0.0
        self.time = 0
        self.isBuyerMaker = False

    @staticmethod
    def json_parse(json_wrapper):
        result = TradeEvent()
        result.eventType = json_wrapper.get_string("e")
        result.eventTime = json_wrapper.get_int("E")
        result.symbol = json_wrapper.get_string("s")
        result.price = json_wrapper.get_float("p")
        result.qty = json_wrapper.get_float("q")
        result.time = json_wrapper.get_int("T")
        result.isBuyerMaker = json_wrapper.get_boolean("m")
        return result
