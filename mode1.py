from landsites import Land
from data_structures.hash_table import LinearProbeTable

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = sorted(sites, key=lambda site: site.gold / site.guardians if site.guardians > 0 else float('inf'), reverse=True)
        self.adventurers = adventurers
        self.s_dict = LinearProbeTable() # for easy access
        for site in sites:
            self.s_dict.__setitem__(site.name, site)

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_sites = []
        remaining_adventurers = self.adventurers

        for site in self.sites:
            if remaining_adventurers <= 0:
                break

            if site.guardians > 0:
                ci = min(site.guardians, remaining_adventurers)
                selected_sites.append((site, ci))
                remaining_adventurers -= ci

        return selected_sites

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        rewards = []

        for adventurers in adventure_numbers:
            total_reward = 0.0
            remaining_adventurers = adventurers

            for site in self.sites:
                if remaining_adventurers <= 0:
                    break

                elif site.guardians > 0:
                    ci = min(site.guardians, remaining_adventurers)
                    reward = min((ci * site.gold) / site.guardians, site.gold)
                    total_reward += reward
                    remaining_adventurers -= ci

            rewards.append(total_reward)

        return rewards

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """

        if self.s_dict.__contains__(land.name) == True:
            site = self.s_dict.__getitem__(land.name)
            site.gold = new_reward
            site.guardians = new_guardians
        else:
            raise ValueError("Land not found")


if __name__ == '__main__':
    a = Land("A", 400, 100)
    b = Land("B", 300, 150)
    c = Land("C", 100, 5)
    d = Land("D", 350, 90)
    e = Land("E", 300, 100)
    # Create deepcopies of the sites
    sites = [a, b, c, d, e]

    nav = Mode1Navigator(sites,200)

    print(nav.sites_dict.get("A"))
    nav.update_site(a, 55.8, 22)
    print(nav.sites_dict.get("A"))
    print(nav.s_dict.__getitem__("A"))
    print(nav.sites)