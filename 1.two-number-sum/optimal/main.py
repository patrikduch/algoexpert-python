def twoNumberSum(array, targetSum):
   i = 0

   potential_match = 0
   dict_matches = {}

   while i<len(array):
      potential_match = targetSum - array[i] 

      if dict_matches.get(potential_match):

         return [potential_match, array[i]]

      dict_matches[array[i]] = True

      i += 1


   return []


array = [1,2,3]


test = twoNumberSum(array, 3)

print(test)