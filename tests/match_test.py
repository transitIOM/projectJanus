from thefuzz import fuzz

def is_match(name1, name2):
        match = fuzz.QRatio(name1, name2)
        print(match)
        if match >= 75:
            return True
        
        return False

class TestClass:
    def test_one(self):
        assert is_match("Peel, B'w'worth, opp Barbary West Cost", "Peel, Ballawattleworth, Barbary West Coast") == True
    def test_two(self):
        assert is_match("Peel Golf Club", "Pulrose Golf Club") == False
    def test_three(self):
        assert is_match("Douglas Gold Club", "Pulrose Golf Club") == True