class Team:
    def __init__(self, bans=[], baron_kills=0, dominion_score=0.0, dragon_kills=0, first_baron=False, first_blood=False, first_dragon=False, first_inhibitor=False, first_rift_herald=False, first_tower=False, inhibitor_kills=0, participants=[], rift_herald_kills=0, tower_kills=0, win=False):
        self.bans = bans
        self.baron_kills = baron_kills
        self.dominion_score = dominion_score
        self.dragon_kills = dragon_kills
        self.first_baron = first_baron
        self.first_blood = first_blood
        self.first_dragon = first_dragon
        self.first_inhibitor = first_inhibitor
        self.first_rift_herald = first_rift_herald
        self.first_tower = first_tower
        self.inhibitor_kills = inhibitor_kills
        self.participants = participants
        self.rift_herald_kills = rift_herald_kills
        self.tower_kills = tower_kills
        self.win = win


class ParticipantStats:
    def __init__(
        self,
        assists: int,
        baron_kills: int,
        consumables_purchased: int,
        deaths: int,
        double_kills: int,
        dragon_kills: int,
        gold_earned: int,
        gold_spent: int,
        inhibitor_kills: int,
        inhibitors_lost: int,
        items: list,
        kda: float,
        kills: int,
        level: int,
        longest_time_spent_living: int,
        penta_kills: int,
        quadra_kills: int,
        time_CCing_others: int,
        total_damage_dealt: int,
        total_damage_dealt_to_champions: int,
        total_damage_shielded_on_teammates: int,
        total_damage_taken: int,
        total_heal: int,
        total_heals_on_teammates: int,
        total_minions_killed: int,
        total_time_cc_dealt: int,
        total_units_healed: int,
        triple_kills: int,
        turret_kills: int,
        turrets_lost: int,
        unreal_kills: int,
        win: bool
    ):
        self.assists = assists
        self.baron_kills = baron_kills
        self.consumables_purchased = consumables_purchased
        self.deaths = deaths
        self.double_kills = double_kills
        self.dragon_kills = dragon_kills
        self.gold_earned = gold_earned
        self.gold_spent = gold_spent
        self.inhibitor_kills = inhibitor_kills
        self.inhibitors_lost = inhibitors_lost
        self.items = items
        self.kda = kda
        self.kills = kills
        self.level = level
        self.longest_time_spent_living = longest_time_spent_living
        self.penta_kills = penta_kills
        self.quadra_kills = quadra_kills
        self.time_CCing_others = time_CCing_others
        self.total_damage_dealt = total_damage_dealt
        self.total_damage_dealt_to_champions = total_damage_dealt_to_champions
        self.total_damage_shielded_on_teammates = total_damage_shielded_on_teammates
        self.total_damage_taken = total_damage_taken
        self.total_heal = total_heal
        self.total_heals_on_teammates = total_heals_on_teammates
        self.total_minions_killed = total_minions_killed
        self.total_time_cc_dealt = total_time_cc_dealt
        self.total_units_healed = total_units_healed
        self.triple_kills = triple_kills
        self.turret_kills = turret_kills
        self.turrets_lost = turrets_lost
        self.unreal_kills = unreal_kills
        self.win = win


class Participant:
    def __init__(self, champion: str, puuid: str, individual_position: str, is_bot: bool, lane: str, role: str, stats: ParticipantStats, summoner_name: str, team: str):
        self.champion = champion
        self.puuid = puuid
        self.individual_position = individual_position
        self.is_bot = is_bot
        self.lane = lane
        self.role = role
        self.stats = stats
        self.summoner_name = summoner_name
        self.team = team
