
class Solution :

	def strangePrinter(self,s) :
		memo = {}
		def util(i,j) :
			if i > j :
				return 0 
			if (i,j) not in memo :
				crntChars = set(s[i:j+1])
				if len(crntChars) == 1 :
					val  =  1
				else :
					val = float("inf")
					temp = []
					while len(crntChars) != 0 :
						crntChar = crntChars.pop()
						rep = []
						for idx,SChar in zip(range(i,j+1),s[i:j+1]) :
							if SChar != crntChar :
								if len(temp) == 0 or temp[-1][1] < idx - 1 :
									temp.append([idx,idx -1 ])
									rep.append("")
								temp[-1][1] += 1
								rep[-1] += SChar
							else :
								if len(rep) == 0 or rep[-1][-1] != crntChars :
									rep.append("")
								rep[-1] += "-"
						rep = "".join(rep)
						# print(f"breaking {s[i:j+1]} for {crntChar} into {rep}")
						print(s[i:j+1],crntChar)
						print(rep)
						crntVal =  1
						while len(temp) != 0 :
							crntVal += util(*temp.pop())
						val = min(crntVal,val)
				memo[(i,j)] = val 
				print(s[i:j+1],val)
			return memo[(i,j)]
		return util(0,len(s) - 1)

