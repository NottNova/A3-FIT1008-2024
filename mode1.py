from landsites import Land
from data_structures.bst import BinarySearchTree
from data_structures.heap import MaxHeap

class Mode1Navigator:
    """
    Student- JOEL GEORGE
    This class initializes the Mode 1 Navigator with the given land sites and number of adventurers.
    For the sites - Lists were used as it is iterable and remains constant however the heap data structure was implemented to sort the data. With heaps a desired priority can be given to sort the elements and with retrieval can normally be at worst complexity of O(logn).
    for the sites_bst - binary search tree (BST)was used as the complexity to find an item is O(logn). This was preferred rather than a hash table as the complexity is lower, and we would also have to consider for O(hash) as well. Please note that a new method has been put into the heap file called is_empty to check whether the heap is empty. When testing for the testcases please use the heap fie that has been provided. Overall both the method of select_sites_from_adventure_numbers and update_site use the heap implemented sorted list while the update_site uses the BST to ensure that the site that we are trying to update indeed exists.

    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        BEST CASE - O(1) - Where there is no site in the sites list.
        WOST CASE - O(N log N) - where the log n is to add and get_max all the elements to the heap and n is the number of sites bringing the total complexity to that
        """
        self.sites = []
        self.adventurers = adventurers
        self.sites_BST = BinarySearchTree()

        for site in sites:
            self.sites_BST.__setitem__(site.name, site)

        heap = MaxHeap(len(sites))

        for site in sites:
            ratio_key = site.gold / site.guardians
            key_val_pair = (ratio_key, site)
            heap.add(key_val_pair)

        while heap.is_empty() == False: # Estabished new is_empty method in the heap data structure
            max_val = heap.get_max()
            self.sites.append(max_val[1])


    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case

        BEST CASE - O(1) - Where there is no site in the sites list.
        WORST CASE - O(N) - where n is basically the loop through the site list and is dependant upon it + the cos of comp but it bring the general complexity to O(n)
        """
        selected_sites = []
        remaining_adventurers = self.adventurers


        for site in self.sites:
            if remaining_adventurers <= 0:
                break

            elif site.guardians > 0:
                ci = min(site.guardians, remaining_adventurers)
                selected_sites.append((site, ci))
                remaining_adventurers -= ci

        return selected_sites

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case

        BEST CASE - O(1) - Where the adventurer number is zero and there are no sites in self.sites
        WORST CASE - O(N^2) - O(A×N) - where A is the length of adventure_numbers and N would be the for loop for the sites
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
        Best Case - O(1)
        Worst Case - O(log N) - Basically O(depth)
        """

        if self.sites_BST.__contains__(land.name) == True:
            site = self.sites_BST.__getitem__(land.name)
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

    x = 4
    while x != 5:
        a = 2
        break



