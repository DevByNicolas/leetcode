class Solution:
    def romanToInt(self, s: str) -> int:
        # Table d'association entre chaque caractère romain et sa valeur
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Si l'élément actuel est plus petit que le suivant, on le soustrait
            if i + 1 < n and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                # Sinon, on l'ajoute
                total += values[s[i]]
                
        return total