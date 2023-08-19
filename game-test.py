import unittest
from game import Player, Enemy

class PlayerDamage(unittest.TestCase):
    def setUp(self):
        self.player = Player("mario")
        self.enemy = Enemy("Cactus")

    def test_player_attack(self):
        self.player.attack_enemy(self.enemy)