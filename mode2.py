from typing import List, Tuple, Union
from landsites import Land
from data_structures.heap import MaxHeap
from data_structures.bst import BinarySearchTree, BSTInOrderIterator

class Mode2Navigator:
    """
    Student- JOEL GEORGE
    This class initializes the Mode 2 Navigator with the number of teams and also estblishes binary tree to use.
    For the sites - Lists were used as it is iterable and remains constant however the heap data structure was implemented to sort the data. With heaps a desired priority can be given to sort the elements and with retrieval can normally be at worst complexity of O(logn).
    for the sites_bst - binary search tree (BST)was used as the complexity to find an item is O(logn). This was preferred rather than a hash table as the complexity is lower, and we would also have to consider for O(hash) as well.
    For the add_site a Binary tree was used to store the existing sites as it stores in O(log n) time
    For simulate_day each of the team was went through and for each team the sites_BST was iterated through and a Max heap was created from there the highes priority value was taken and site was updated and tge action was recorded
    Compute_score method was created as a method to call simulate_day could be incorporated into that method but code complexity would decrease by splitting out the two tasks.
    """
    def __init__(self, n_teams: int) -> None:
        """
        Student-TODO: Best/Worst Case
        Best & Worst Case = O(1)
        """
        self.n_teams = n_teams
        self.sites_BST = BinarySearchTree()

    def add_sites(self, sites: List[Land]) -> None:
        """
        Student-TODO: Best/Worst Case
        Best Case - O(1)
        Worst Case - O(N log N) - Basically O(depth) for contains, delete, set item and the N would equate to the number of sites to be added through
        """

        for site in sites:
            if self.sites_BST.__contains__(site.name):
                self.sites_BST.__delitem__(site.name) # If the same site is found in the already existing list then it deletes the item and then re-adds to update that item
            self.sites_BST.__setitem__(site.name, site)


    def simulate_day(self, adventurer_size: int) -> List[Tuple[Union[Land, None], int]]:
        """
        Student-TODO: Best/Worst Case
        Best Case - O(1) - If there was 0 teams established hen it would be O(1)
        Worst Case - O(N^2 log N) - the two for loops to iterate over and to add through to Heap is O(depth) which basically equals O(N x N x log N)
        """
        actions = []
        remaining_adventurers_per_team = [adventurer_size] * self.n_teams

        for team in range(self.n_teams):
            score_heap_1 = MaxHeap(len(self.sites_BST))


            for pair in self.sites_BST:
                idx = pair.key
                site = pair.item
                scores = self.compute_score(site, remaining_adventurers_per_team[team])
                data_store = (scores[0], idx, site)
                # complexity of O(log n) to add to the heap
                score_heap_1.add(data_store)


            # Select the best site
            top_heap = score_heap_1.get_max()
            best_site = top_heap[2]

            score, remaining_adventurers, reward = self.compute_score(best_site, remaining_adventurers_per_team[team])

            # Update the site's state
            ci = min(best_site.guardians, remaining_adventurers_per_team[team])#
            best_site.gold -= reward
            best_site.guardians -= ci

            # Record the action
            actions.append((best_site, ci))
            remaining_adventurers_per_team[team] = remaining_adventurers
        return actions

    def compute_score(self, site: Land, remaining_adventurers: int) -> Tuple[float, int, float]:
        """
        Student-TODO: Best/Worst Case
        Best & Worst Case: O(1) - just the cost of comparisons
        """
        if site.guardians == 0:
            return 2.5 * remaining_adventurers, remaining_adventurers, 0

        ci = min(site.guardians, remaining_adventurers)
        reward = min((ci * site.gold) / site.guardians, site.gold)
        remaining_adventurers -= ci
        score = 2.5 * remaining_adventurers + reward

        return score, remaining_adventurers, reward

if __name__ == '__main__':
    a = Land("A", 400, 100)
    b = Land("B", 300, 150)
    c = Land("C", 100, 5)
    d = Land("D", 350, 90)

    sites = [a, b, c, d]

