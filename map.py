from dataclasses import dataclass
import pygame, pytmx, pyscroll
from player import Player


@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup


class MapManager:

    def __init__(self, win, player):
        # "house" -> Map("house", walls, group)
        self.win = win
        self.player = player
        self.maps = dict()
        self.current_map = "carte_principale"

    def register_map(self, name):
        # charger le map
        tmx_data = pytmx.util_pygame.load_pygame(f'{name}.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.win.get_size())
        map_layer.zoom = 2

        # définir une liste qui va stocker les murs
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer un joueur
        player_position = tmx_data.get_object_by_name('birth_point')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

        # définir le rectangle de la collision pour entrer dans le portail
        portal = tmx_data.get_object_by_name('exit_dungeon')
        self.portal_rect = pygame.Rect(portal.x, portal.y, portal.width, portal.height)