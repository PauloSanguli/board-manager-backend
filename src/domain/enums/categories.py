from enum import Enum

from typing import Optional


class Categories(Enum):
    """categories of veichles"""
    A: Optional(str) = "motos,ciclomotores"
    B: Optional(str) = "carros-ligeiros,motos-leves"
    C: Optional(str) = "camiões"
    D: Optional(str) = "ônibus"
    E: Optional(str) = "combinações"
    AM: Optional(str) = "ciclomotores,motociclos-ligeiros"
    B1: Optional(str) = "triciclos,quadriciclos-leves"
    F: Optional(str) = "tratores-agrícolas"
    G: Optional(str) = "veículos-condução-geral"
