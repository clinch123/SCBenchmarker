# number of in-game ticks in one second real time
TICKS_PER_SECOND = 22.4

# file extension
SC2REPLAY = 'SC2Replay'

# server constants
FLASK_CONFIG = 'config.py'
INDEX_HTML = 'index.html.jinja'
ANALYZE_HTML = 'analyze.html.jinja'
OWN_REPLAY_TAG = 'own_replay'
BENCH_REPLAY_TAG = 'bench_replay'
SAVED_REPLAYS_TAG = 'saved_replay'

# aliases for units in different modes, set to the same unit
ALIASES = {
    'WarpPrismPhasing': 'WarpPrism',
    'WarpGate': 'Gateway',
    'SiegeTankSieged': 'SiegeTank',
    'SupplyDepotLowered': 'SupplyDepot',
    'LiberatorAG': 'Liberator',
    'WidowMineBurrowed': 'WidowMine',
    'ObserverSiegeMode': 'Observer',
    'OverlordTransport': 'DropperLord',
    'LurkerDenMP': 'LurkerDen',
    'LurkerMP': 'Lurker',
    'SwarmHostMP': 'SwarmHost'
}

# blacklist specific entries from showing up.
BLACKLIST = [
    'Egg',
    'Larva',
    'CreepTumorBurrowed',
    'RavagerCocoon',
    'CreepTumor',
    'LurkerMPEgg',
    'LocustMP',
    'LocustMPFlying',
    'LocustMPPrecursor',
    'BroodLordCocoon',
    'BroodlingEscort',
    'Broodling',
    'BanelingCocoon',
    'OverlordCocoon',
    'TransportOverlordCocoon',
    'CreepTumorQueen'
]
